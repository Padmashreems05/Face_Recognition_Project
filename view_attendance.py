"""
view_attendance.py
==================
Prints today's attendance log in a neat table format.
 
Usage:
    python view_attendance.py
"""
 
import csv
import os
from datetime import datetime
 
 
def view_today_attendance():
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join("attendance_logs", f"attendance_{today}.csv")
 
    if not os.path.exists(log_file):
        print(f"[INFO] No attendance log found for today ({today}).")
        print("       Run face_recognition_attendance.py first.")
        return
 
    print(f"\n{'='*50}")
    print(f"  ATTENDANCE REPORT — {today}")
    print(f"{'='*50}")
    print(f"{'#':<4} {'Name':<25} {'Time':<12} {'Status'}")
    print("-" * 50)
 
    with open(log_file, "r") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            print(f"{i:<4} {row['Name']:<25} {row['Time']:<12} {row['Status']}")
 
    print("=" * 50)
 
 
if __name__ == "__main__":
    view_today_attendance()