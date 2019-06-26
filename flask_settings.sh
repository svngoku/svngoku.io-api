#!/bin/bash

# flask settings

export FLASK_APP=home/your-repo/app.py
export FLASK_DEBUG=0

flask run --host=0.0.0.0 --port=80

