Readme
======

Drone Security Analyst
---------------------

A real-time drone security analysis system that processes video streams and telemetry data to detect and analyze security events.

Features
--------

* Real-time video processing and object detection
* Live stream and recorded video support
* Scene understanding using BLIP vision-language model
* Configurable security rules and alerts
* Frame-by-frame indexing for historical analysis

Quick Start
----------

Installation
~~~~~~~~~~~

.. code-block:: bash

   pip install -e .

Basic Usage
~~~~~~~~~~

.. code-block:: python

   from src.processors.video_processor import VideoProcessor

   # Process a video file
   processor = VideoProcessor(video_path="path/to/video.mp4")
   for frame_data in processor.process_video():
       print(f"Frame {frame_data['frame_id']}: {frame_data['description']}")

Project Structure
---------------

* ``src/processors/`` - Video and frame processing
* ``src/models/`` - Object detection and analysis
* ``src/storage/`` - Frame indexing and event logging
* ``src/alerts/`` - Security alert generation
* ``src/api/`` - Query interface for historical data

For detailed documentation, see :doc:`usage` and :doc:`api`. 