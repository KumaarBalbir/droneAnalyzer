import streamlit as st
import time
from datetime import datetime, timedelta

from simulator import DroneSimulator
from detector import ObjectDetector
from data_manager import DataManager
from alert_system import AlertSystem

# Initialize components
@st.cache_resource
def init_components():
    return (
        DroneSimulator(),
        ObjectDetector(),
        DataManager(),
        AlertSystem()
    )

simulator, detector, data_manager, alert_system = init_components()

# App title and description
st.title("Drone Security Analyst Agent")
st.write("Real-time security monitoring and analysis system")

# Sidebar controls
st.sidebar.header("Controls")
monitoring_active = st.sidebar.checkbox("Active Monitoring", value=True)
update_interval = st.sidebar.slider("Update Interval (seconds)", 1, 10, 2)

# Main display areas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Telemetry")
    telemetry_container = st.empty()
    
    st.subheader("Latest Frame")
    frame_container = st.empty()

with col2:
    st.subheader("Security Alerts")
    alerts_container = st.empty()

# Query interface
st.subheader("Historical Data Query")
query_type = st.selectbox("Search for:", ["person", "car", "truck", "bicycle", "motorcycle"])
if st.button("Search"):
    results = data_manager.query_frames(query_type)
    st.write(f"Found {len(results)} matching frames:")
    st.dataframe(results[['timestamp', 'description']])

# Main monitoring loop
while monitoring_active:
    # Generate new data
    telemetry_data = simulator.generate_telemetry()
    frame_data = simulator.generate_frame()
    
    # Process frame with detector
    detections = detector.process_frame({'objects': frame_data.objects})
    
    # Store data
    data_manager.add_frame(frame_data)
    data_manager.add_telemetry(telemetry_data)
    
    # Check for alerts
    new_alerts = alert_system.check_rules(frame_data, telemetry_data)
    
    # Update displays
    telemetry_container.write({
        "Location": telemetry_data.location,
        "Altitude": f"{telemetry_data.altitude:.1f}m",
        "Battery": f"{telemetry_data.battery}%",
        "Time": telemetry_data.timestamp.strftime("%H:%M:%S")
    })
    
    frame_container.write(frame_data.description)
    
    alerts_container.write("\n".join(alert_system.alerts[-5:]))  # Show last 5 alerts
    
    time.sleep(update_interval)
