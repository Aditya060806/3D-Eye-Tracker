#!/usr/bin/env python3
"""
EyeTracker Runner
Quick launcher for different tracking modes
"""

import os
import sys
import subprocess

def run_basic_tracker():
    """Run basic pupil detector"""
    subprocess.run([sys.executable, "OrloskyPupilDetector.py"])

def run_lite_tracker():
    """Run lite pupil detector"""
    subprocess.run([sys.executable, "OrloskyPupilDetectorLite.py"])

def run_3d_tracker():
    """Run 3D eye tracker"""
    os.chdir("3DTracker")
    subprocess.run([sys.executable, "Orlosky3DEyeTracker.py"])

def main():
    print("EyeTracker Launcher")
    print("==================")
    print("1. Basic Pupil Detector (full features)")
    print("2. Lite Pupil Detector (fast)")
    print("3. 3D Eye Tracker (advanced)")
    print("4. Exit")
    
    while True:
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            run_basic_tracker()
            break
        elif choice == "2":
            run_lite_tracker()
            break
        elif choice == "3":
            run_3d_tracker()
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()