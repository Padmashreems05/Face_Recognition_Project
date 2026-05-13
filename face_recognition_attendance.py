"""
Face Recognition Attendance System
====================================
Author  : [Your Name]
Project : Real-Time Face Recognition using OpenCV + face_recognition
Purpose : Automated attendance logging with live webcam feed
"""

import cv2
import face_recognition
import numpy as np
import os
import csv
from datetime import datetime


# ─────────────────────────────────────────────
#  STEP 1 : Load known faces from /known_faces
# ─────────────────────────────────────────────
def load_known_faces(known_faces_dir="known_faces"):
    """
    Reads every image in the known_faces folder.
    File name (without extension) = person's name.
    Returns two lists: encodings and corresponding names.
    """
    known_encodings = []
    known_names = []

    print("\n[INFO] Loading known faces...")

    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            filepath = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(filepath)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                print(f"  [WARN] No face found in {filename} — skipping.")
                continue

            encoding = encodings[0]
            name = os.path.splitext(filename)[0].replace("_", " ").title()
            known_encodings.append(encoding)
            known_names.append(name)
            print(f"  [OK]   Loaded: {name}")

    print(f"[INFO] {len(known_names)} face(s) loaded.\n")
    return known_encodings, known_names


# ─────────────────────────────────────────────
#  STEP 2 : Attendance logger (CSV)
# ─────────────────────────────────────────────
def log_attendance(name, log_dir="attendance_logs"):
    """
    Writes a timestamped entry to today's CSV file.
    Prevents duplicate entries for the same person per session.
    """
    os.makedirs(log_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"attendance_{today}.csv")

    # Read existing records to avoid duplicates
    already_logged = set()
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if row:
                    already_logged.add(row[0])

    if name not in already_logged:
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            if os.path.getsize(log_file) == 0:
                writer.writerow(["Name", "Date", "Time", "Status"])
            timestamp = datetime.now().strftime("%H:%M:%S")
            writer.writerow([name, today, timestamp, "Present"])
        print(f"  [LOG]  Attendance marked: {name} at {timestamp}")
        return True  # newly logged
    return False  # already marked


# ─────────────────────────────────────────────
#  STEP 3 : Main recognition loop
# ─────────────────────────────────────────────
def run_attendance_system():
    known_encodings, known_names = load_known_faces()

    if not known_encodings:
        print("[ERROR] No known faces found. Add images to the 'known_faces' folder.")
        return

    # Open webcam (0 = default camera)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam. Check your camera connection.")
        return

    print("[INFO] Webcam started. Press 'Q' to quit.\n")

    # Track who was already marked this session for on-screen feedback
    marked_this_session = set()
    TOLERANCE = 0.50  # lower = stricter matching (0.4–0.6 is typical)
    SCALE = 0.25      # shrink frame for faster processing

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        # ── Process at reduced resolution for speed ──
        small_frame = cv2.resize(frame, (0, 0), fx=SCALE, fy=SCALE)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small)
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_idx = np.argmin(distances)
            best_distance = distances[best_idx]

            if best_distance < TOLERANCE:
                name = known_names[best_idx]
                confidence = round((1 - best_distance) * 100, 1)
                color = (0, 200, 0)  # green
                label = f"{name}  {confidence}%"

                # Log attendance
                if log_attendance(name):
                    marked_this_session.add(name)
            else:
                name = "Unknown"
                color = (0, 0, 220)  # red
                label = "Unknown"

            # ── Scale face box back to full resolution ──
            top, right, bottom, left = [int(v / SCALE) for v in face_location]

            # Draw bounding box
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Draw name label background
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, label, (left + 6, bottom - 8),
                        cv2.FONT_HERSHEY_DUPLEX, 0.65, (255, 255, 255), 1)

        # ── HUD overlay ──
        cv2.putText(frame, "Face Recognition Attendance System",
                    (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 220, 0), 2)
        cv2.putText(frame, f"Marked today: {len(marked_this_session)}",
                    (10, 58), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
        cv2.putText(frame, "Press Q to quit",
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)

        cv2.imshow("Face Recognition Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("\n[INFO] System stopped. Attendance logs saved in 'attendance_logs/' folder.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    run_attendance_system()
