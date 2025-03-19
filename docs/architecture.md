# System Architecture

## Core Components

1. Data Generation
   - VideoSimulator: Generates simulated video frames with object detections
   - TelemetrySimulator: Produces drone telemetry data

2. Processing Pipeline
   - ObjectDetector: Processes video frames for object detection
   - AlertGenerator: Applies security rules to generate alerts

3. Storage System
   - FrameIndexer: Indexes and stores frame data for querying (as of now in memory storage)
   - Historical data management

4. User Interface
   - Streamlit-based dashboard
   - Real-time updates
   - Query interface

## Data Flow

1. Data Input
   - Video frames from simulator
   - Telemetry data from drone

2. Processing
   - Object detection on frames
   - Rule-based alert generation
   - Data indexing

3. Output
   - Real-time display updates
   - Alert notifications
   - Query results
