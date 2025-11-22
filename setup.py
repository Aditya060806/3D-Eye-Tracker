#!/usr/bin/env python3
"""
EyeTracker Setup Script
Run this to install dependencies and test the system
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        return False
    return True

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import cv2
        import numpy as np
        import tkinter as tk
        print("✓ All modules imported successfully")
        print(f"OpenCV version: {cv2.__version__}")
        print(f"NumPy version: {np.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def main():
    print("EyeTracker Setup")
    print("================")
    
    if install_requirements():
        if test_imports():
            print("\n✓ Setup complete! You can now run:")
            print("  python OrloskyPupilDetector.py")
            print("  python OrloskyPupilDetectorLite.py")
            print("  python 3DTracker/Orlosky3DEyeTracker.py")
        else:
            print("\n✗ Setup failed - import errors")
    else:
        print("\n✗ Setup failed - dependency installation")

if __name__ == "__main__":
    main()