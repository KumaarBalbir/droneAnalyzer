import streamlit as st
import time

from src.data.video_simulator import VideoSimulator
from src.data.telemetry_simulator import TelemetrySimulator
from src.models.object_detector import ObjectDetector
from src.models.video_summarizer import VideoSummarizer
from src.models.query_agent import QueryAgent
from src.storage.frame_indexer import FrameIndexer
from src.storage.event_logger import EventLogger
from src.alerts.alert_generator import AlertGenerator
from src.processors.frame_processor import FrameProcessor
from src.processors.telemetry_processor import TelemetryProcessor

# Initialize components


@st.cache_resource
def init_components():
    return (
        VideoSimulator(),
        TelemetrySimulator(),
        ObjectDetector(),
        FrameIndexer(),
        EventLogger(),
        AlertGenerator(),
        VideoSummarizer(),
        QueryAgent(FrameIndexer(), EventLogger()),
        FrameProcessor(),
        TelemetryProcessor()
    )


video_sim, telemetry_sim, detector, indexer, event_logger, alert_gen, summarizer, query_agent, frame_processor, telemetry_processor = init_components()

# App title and description
st.title("Drone Security Analyst Agent")
st.write("Real-time security monitoring and analysis system")

# Sidebar controls
st.sidebar.header("Controls")
monitoring_active = st.sidebar.checkbox("Active Monitoring", value=True)
update_interval = st.sidebar.slider("Update Interval (seconds)", 1, 10, 2)

# Initialize session state for question answering
if 'question_history' not in st.session_state:
    st.session_state.question_history = []

# Main display areas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Telemetry")
    telemetry_container = st.empty()

    st.subheader("Latest Frame")
    frame_container = st.empty()

    st.subheader("Video Summary")
    summary_container = st.empty()

with col2:
    st.subheader("Security Alerts")
    alerts_container = st.empty()

    # Enhanced question answering interface
    st.subheader("Ask Questions")
    with st.form(key='question_form'):
        user_question = st.text_input("Ask about objects, events, or alerts:",
                                      key="question_input",
                                      placeholder="e.g., What objects were detected?")
        submit_button = st.form_submit_button("Ask Question")

        if submit_button and user_question:
            answer = query_agent.answer_question(user_question)
            st.session_state.question_history.append({
                'question': user_question,
                'answer': answer
            })

    # Display question history
    if st.session_state.question_history:
        st.subheader("Recent Questions & Answers")
        # Show last 3 Q&As
        for qa in reversed(st.session_state.question_history[-3:]):
            st.write(f"Q: {qa['question']}")
            st.write(f"A: {qa['answer']}")
            st.markdown("---")

# Query interface
st.subheader("Historical Data Query")
query_type = st.selectbox(
    "Search for:", ["person", "car", "truck", "bicycle", "motorcycle"])
if st.button("Search"):
    results = indexer.query_frames(query_type)
    st.write(f"Found {len(results)} matching frames:")
    st.dataframe(results[['timestamp', 'description']])

# Main monitoring loop
while monitoring_active:
    # Get data
    frame = video_sim.generate_frame()
    telemetry = telemetry_sim.generate_telemetry()

    # Process data
    processed_frame = frame_processor.process(frame)
    processed_telemetry = telemetry_processor.process(telemetry)

    # Process frame with detector
    detections = detector.process_frame({'objects': processed_frame.objects})

    # Store data and update summary
    frame_dict = {
        'timestamp': processed_frame.timestamp,
        'frame_id': processed_frame.frame_id,
        'description': processed_frame.description,
        'objects': processed_frame.objects
    }
    telemetry_dict = {
        'timestamp': processed_telemetry.timestamp,
        'location': processed_telemetry.location,
        'altitude': processed_telemetry.altitude,
        'battery': processed_telemetry.battery
    }

    indexer.add_frame(frame_dict)
    summarizer.add_frame(frame_dict)

    # Check for alerts
    new_alerts = alert_gen.check_rules(frame_dict, telemetry_dict)

    # Update displays
    telemetry_container.write({
        "Location": processed_telemetry.location,
        "Altitude": f"{processed_telemetry.altitude:.1f}m",
        "Battery": f"{processed_telemetry.battery}%",
        "Time": processed_telemetry.timestamp.strftime("%H:%M:%S")
    })

    frame_container.write(processed_frame.description)
    summary_container.write(summarizer.generate_summary())
    # Show last 5 alerts
    alerts_container.write("\n".join(alert_gen.alerts[-5:]))

    time.sleep(update_interval)
