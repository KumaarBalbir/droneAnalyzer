Usage Guide
==========

Installation
-----------

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/yourusername/drone-security-analyst.git
   cd drone-security-analyst

   # Install dependencies
   pip install -e .

Basic Usage
----------

Processing a Video File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.processors.video_processor import VideoProcessor

   # Initialize processor with video file
   processor = VideoProcessor(video_path="path/to/video.mp4")

   # Process video frames
   for frame_data in processor.process_video():
       print(f"Frame {frame_data['frame_id']}: {frame_data['description']}")

Processing Live Stream
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Initialize processor with stream URL
   processor = VideoProcessor(stream_url="rtsp://camera-stream-url")

   # Process live stream
   for frame_data in processor.process_video():
       print(f"Frame {frame_data['frame_id']}: {frame_data['description']}")

Advanced Usage
------------

Configuring Object Detection
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.models.object_detector import ObjectDetector

   # Initialize with custom model
   detector = ObjectDetector(model_path="path/to/model.pt")

   # Configure detection parameters
   detector.confidence_threshold = 0.7
   detector.iou_threshold = 0.5

Querying Historical Data
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.storage.frame_indexer import FrameIndexer

   # Initialize indexer
   indexer = FrameIndexer()

   # Query frames by time range
   frames = indexer.query_frames(
       time_range=(start_time, end_time)
   )

   # Query frames by object type
   frames = indexer.query_frames(
       object_type="person"
   ) 