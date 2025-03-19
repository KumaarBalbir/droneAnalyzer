API Reference
=============

Core Components
--------------

Video Processor
~~~~~~~~~~~~~

.. automodule:: src.processors.video_processor
   :members:
   :undoc-members:
   :show-inheritance:

   The VideoProcessor class handles video stream processing and frame analysis.

   Example:
       >>> processor = VideoProcessor(video_path="video.mp4")
       >>> for frame_data in processor.process_video():
       ...     print(frame_data['description'])

Frame Processor
~~~~~~~~~~~~~

.. automodule:: src.processors.frame_processor
   :members:
   :undoc-members:
   :show-inheritance:

   Processes individual video frames and extracts relevant information.

Object Detector
~~~~~~~~~~~~~

.. automodule:: src.models.object_detector
   :members:
   :undoc-members:
   :show-inheritance:

   Detects and classifies objects in video frames using YOLOv8.

Storage Components
----------------

Frame Indexer
~~~~~~~~~~~

.. automodule:: src.storage.frame_indexer
   :members:
   :undoc-members:
   :show-inheritance:

   Indexes and stores video frames for historical analysis.

Event Logger
~~~~~~~~~~

.. automodule:: src.storage.event_logger
   :members:
   :undoc-members:
   :show-inheritance:

   Logs security events and alerts. 