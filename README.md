# 3D Eye Tracker
A comprehensive Python-based eye tracking system with multiple tracking modes

## Overview
This repository contains a complete eye tracking solution with basic pupil detection, advanced 3D gaze estimation, and head tracking capabilities. The system is designed for research and development in eye tracking applications.

## Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/Aditya060806/3D-Eye-Tracker.git
cd 3D-Eye-Tracker

# Install dependencies
python setup.py
```

### Running the Tracker
```bash
# Easy launcher with menu
python run.py

# Or run specific trackers directly:
python OrloskyPupilDetector.py          # Full-featured tracker
python OrloskyPupilDetectorLite.py      # Fast lightweight version
python 3DTracker/Orlosky3DEyeTracker.py # Advanced 3D tracking
```

## Features

### Tracking Modes
- **Basic Pupil Detection**: Robust ellipse fitting with multiple thresholding levels
- **3D Eye Tracking**: Real-time gaze vector computation with OpenGL visualization
- **Head Tracking**: MediaPipe-based head pose estimation for mouse control
- **Webcam Integration**: Works with standard USB cameras

### Key Capabilities
- Multi-level binary thresholding for robust pupil detection
- Ray intersection algorithms for 3D gaze estimation
- Real-time performance optimization
- Interactive calibration systems
- Debug modes with visual overlays

## Hardware Requirements
- USB webcam (any standard camera)
- For optimal results: IR eye camera (GC0308 recommended)
- Python 3.7+ environment

## Dependencies
- OpenCV (computer vision)
- NumPy (numerical operations)
- Tkinter (GUI, included with Python)
- MediaPipe (for head tracking)
- PyOpenGL (optional, for 3D visualization)

## Controls
- **SPACE**: Pause/resume
- **Q**: Quit
- **D**: Toggle debug mode
- **C**: Calibrate (3D tracker)

## Project Structure
```
3D-Eye-Tracker/
├── OrloskyPupilDetector.py      # Main pupil detector
├── OrloskyPupilDetectorLite.py  # Lightweight version
├── 3DTracker/                   # Advanced 3D tracking
├── HeadTracker/                 # Head pose tracking
├── FrontCameraTracker/          # Dual-camera setup
├── Webcam3DTracker/             # Webcam-based tracking
├── setup.py                     # Installation script
├── run.py                       # Easy launcher
└── eye_test.mp4                 # Test video
```

## Output
- Real-time video display with tracking overlays
- Gaze vector data (CSV format)
- Unity integration support
- Performance metrics

## License
Open source - see LICENSE file for details

## Contributing
Contributions welcome! Please feel free to submit issues and pull requests.