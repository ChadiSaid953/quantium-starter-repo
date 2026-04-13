#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run tests
python3 -m pytest test_app.py

# Capture exit code
if [ $? -eq 0 ]; then
    echo "Tests passed ✅"
    exit 0
else
    echo "Tests failed ❌"
    exit 1
fi
