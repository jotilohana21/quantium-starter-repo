#!/bin/bash

# 1. Activate the virtual environment
source activate quantium_env

# 2. Execute the test suite
pytest test_app.py

# 3. Check the status
if [ $? -eq 0 ]; then
    echo "Tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi