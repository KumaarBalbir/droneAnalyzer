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

Local Development
~~~~~~~~~~~
1. Clone the repository
.. code-block:: bash

   git clone https://github.com/KumaarBalbir/droneAnalyzer.git

2. Create a virtual environment
.. code-block:: bash

   sudo apt-get install python3-venv
   python3 -m venv venv
   source venv/bin/activate

3. On Windows
.. code-block:: bash

   python -m venv venv
   venv\Scripts\activate

4. Install uv (a fast Python package manager that acts as a drop-in replacement for pip)
.. code-block:: bash

   pip install uv

5. Install the project dependencies
.. code-block:: bash

   uv pip install -r pyproject.toml

6. Run the project
.. code-block:: bash

   streamlit run main.py --server.port 5000

7. View the project in your browser
.. code-block:: bash

   http://localhost:5000
   
High level architecture
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /docs/source/images/flytbase-overall-flow.png
   :alt: High level architecture
   :width: 100%
   :align: center


Project Structure
---------------

* ``src/processors/`` - Video and frame processing
* ``src/models/`` - Object detection and analysis
* ``src/storage/`` - Frame indexing and event logging
* ``src/alerts/`` - Security alert generation
* ``src/api/`` - Query interface for historical data

For detailed documentation, see :doc:`usage` and :doc:`api`. 