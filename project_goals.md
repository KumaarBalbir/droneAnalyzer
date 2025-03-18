drone-security-analyst/
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
├── docs/                       # Documentation files
│   ├── feature_spec.md         # Feature specification
│   ├── architecture.md         # Detailed architecture
│   └── test_cases.md           # Test documentation
├── src/                        # Source code
│   ├── data/                   # Data simulation
│   │   ├── video_simulator.py  # Simulated video frames
│   │   └── telemetry_simulator.py # Simulated telemetry data
│   ├── processors/             # Data processors
│   │   ├── frame_processor.py  # Process video frames
│   │   └── telemetry_processor.py # Process telemetry data
│   ├── models/                 # AI models
│   │   ├── object_detector.py  # Object detection
│   │   └── event_analyzer.py   # Event analysis
│   ├── rules/                  # Security rules
│   │   ├── rule_engine.py      # Rule processing engine
│   │   └── predefined_rules.py # Security rule definitions
│   ├── storage/                # Storage solutions
│   │   ├── event_logger.py     # Event logging
│   │   └── frame_indexer.py    # Frame indexing system
│   ├── alerts/                 # Alert system
│   │   └── alert_generator.py  # Generate security alerts
│   └── api/                    # API endpoints
│       └── query_interface.py  # Query interface for indexed frames
├── tests/                      # Test scripts
│   ├── test_object_detection.py
│   ├── test_event_analysis.py
│   ├── test_rule_engine.py
│   └── test_frame_indexer.py
├── notebooks/                  # Development notebooks
│   └── prototype_development.ipynb
├── config/                     # Configuration files
│   └── config.yaml             # System configuration
└── main.py                     # Main entry point