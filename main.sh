#!/bin/bash

# Activate the virtual environment
source ~/projects/public/venv/bin/activate

# Run the Python script to generate the site
python3 ~/projects/public/src/main.py

# Navigate to the public directory and start the server
cd public && python3 -m http.server 8888
