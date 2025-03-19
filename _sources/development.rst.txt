Development Guide
===============

Setup Development Environment
---------------------------

1. Clone the repository:
   .. code-block:: bash

      git clone https://github.com/yourusername/drone-security-analyst.git
      cd drone-security-analyst

2. Create and activate virtual environment:
   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Linux/Mac
      # or
      .\venv\Scripts\activate  # Windows

3. Install development dependencies:
   .. code-block:: bash

      pip install -e ".[dev]"

Running Tests
-----------

.. code-block:: bash

   pytest tests/

Building Documentation
-------------------

.. code-block:: bash

   cd docs
   make html

Code Style
---------

This project follows PEP 8 guidelines. Use black for code formatting:

.. code-block:: bash

   black src/ tests/

Contributing
----------

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and documentation
5. Submit a pull request

Architecture Overview
------------------

The system is built with the following components:

* Video Processing Pipeline
* Object Detection System
* Event Analysis Engine
* Storage and Indexing
* Alert Generation 