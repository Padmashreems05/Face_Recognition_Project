# 🎓 Face Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A real-time Face Recognition Attendance System built using Python, OpenCV, dlib, and face_recognition.  
Detects and recognizes registered faces through a webcam and automatically marks attendance with date and time in a CSV file.

---

## ✨ Features

- 🎥 Real-time face detection using webcam
- 🧠 Face recognition with confidence score display
- 📋 Automatic attendance logging (CSV) with date & time
- 🚫 Duplicate entry prevention per session
- 📁 Daily attendance files (`attendance_YYYY-MM-DD.csv`)
- 🖥️ Live HUD overlay showing marked count
- 🐣 Simple and beginner-friendly codebase

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10 | Core language |
| OpenCV | Webcam access & video rendering |
| dlib | Face detection backbone |
| face_recognition | Face encoding & matching |
| NumPy | Distance calculations |
| CSV | Attendance data storage |

---

## 📁 Project Structure

```
Face_Recognition_Project/
│
├── known_faces/                        # Store registered face images here
│
├── attendance_logs/
│   └── attendance_YYYY-MM-DD.csv       # Auto-generated daily attendance logs
│
├── register_face.py                    # Step 1 — Register a new face via webcam
├── face_recognition_attendance.py      # Step 2 — Run the live attendance system
├── view_attendance.py                  # Step 3 — View today's attendance report
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/Face_Recognition_Project.git
cd Face_Recognition_Project
```

**2. Install required libraries:**
```bash
pip install face_recognition opencv-python numpy dlib
```

> ⚠️ **Note:** `dlib` may require CMake on Windows. On Linux/Mac it usually installs directly.

---

## 🚀 How to Run

### ▶️ Step 1 — Register a Face

```bash
python register_face.py
```

What happens:
- Enter the person's name when prompted (e.g., `Padmashree`)
- Webcam opens with a guide oval — align your face inside it
- Press **SPACE** to capture and save the photo
- Press **Q** to cancel
- Face is saved as `known_faces/Padmashree.jpg`

```
Enter the person's name (e.g., Rahul_Sharma): Padmashree
[INFO] Webcam ready.
  - Look directly at the camera.
  - Press SPACE to capture your photo.
  - Press Q to cancel.

[SUCCESS] Face saved as: known_faces/Padmashree.jpg
[INFO] You can now run: python face_recognition_attendance.py
```

---

### ▶️ Step 2 — Start the Attendance System

```bash
python face_recognition_attendance.py
```

What happens:
- All faces from `known_faces/` are loaded automatically
- Webcam opens and starts recognizing faces in real time
- Recognized faces shown with **green box + name + confidence %**
- Unknown faces shown with a **red box**
- Attendance is logged instantly to today's CSV file
- Press **Q** to quit

```
[INFO] Loading known faces...
  [OK]   Loaded: Padmashree
[INFO] 1 face(s) loaded.

[INFO] Webcam started. Press 'Q' to quit.

  [LOG]  Attendance marked: Padmashree at 07:30:21
```

---

### ▶️ Step 3 — View Attendance Report

```bash
python view_attendance.py
```

Output:
```
==================================================
  ATTENDANCE REPORT — 2026-05-13
==================================================
#    Name                      Time         Status
--------------------------------------------------
1    Padmashree                07:30:21     Present
==================================================
```

Or open the CSV directly:
```
attendance_logs/attendance_2026-05-13.csv
```

---

## 📊 Example CSV Record

```csv
Name,Date,Time,Status
Padmashree,2026-05-13,07:30:21,Present
```

---

## ⚙️ Configuration (Inside `face_recognition_attendance.py`)

| Variable | Default | Description |
|---|---|---|
| `TOLERANCE` | `0.50` | Match strictness — lower = stricter (range: 0.4–0.6) |
| `SCALE` | `0.25` | Frame resize factor for faster processing |
| `known_faces_dir` | `"known_faces"` | Folder with registered face images |
| `log_dir` | `"attendance_logs"` | Folder where CSV files are saved |

---

## 💡 How It Works

1. Load phase — Every `.jpg`/`.png` in `known_faces/` is read and encoded into a 128-point face vector
2. Detection — Each webcam frame is resized (25%) and scanned for face locations
3. Matching — Euclidean distance between live face encoding and all known encodings is computed
4. Decision — If best distance < `TOLERANCE` (0.50), the face is identified; otherwise marked Unknown
5. Logging — Name, date, time, and status are written to a daily CSV (duplicates are skipped)

---

## 🔮 Future Improvements

- Liveness detection (anti-spoofing)
- Flask web dashboard for attendance view
- SQLite database instead of CSV
- Multi-face simultaneous recognition display
- Cloud-based attendance storage
- Email/SMS alert on attendance marked

---