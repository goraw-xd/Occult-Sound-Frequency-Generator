#!/usr/bin/env bash
# Install common dependencies for CelestiaTone
# Usage: ./install_dependencies.sh

set -euo pipefail

echo "Installing Python packages..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt || echo "No requirements.txt present"

echo "Node tooling (web app) - run in ui/web_app if needed"
# cd ui/web_app && npm install

# Optional: compile C++ DSP components
# python setup/build_dsp_engine.py

echo "Dependency installation script finished. Review output for errors."
