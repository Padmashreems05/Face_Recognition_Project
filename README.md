🎓Face Recognition Attendance System
A real-time Face Recognition Attendance System built using Python, OpenCV, dlib, and face_recognition.This project detects and recognizes registered faces through webcam input and automatically marks attendance with date and time.

📸Demo
Webcam opens → Face detected → Name recognized → Attendance marked automatically in CSV ✅

✨Features
🎥 Real-time face detection using webcam
🧠 Face recognition using pre-registered images
📋 Automatic attendance marking with date & time
📁 Stores attendance records in CSV file
🚫 Duplicate entry prevention
🐣 Simple and beginner-friendly project

🛠️ Tech                                
Technology Purpose                     Stack 
Python 3.10                            Core programming language
OpenCV                                 Webcam access & image processing
dlib                                   Face detection backbone
face_recognition                       Face encoding & matching
NumPy                                  Numerical operations
CSV                                    Attendance data storage

📁 Project Structure
Face_Recognition_Project/
│
├── known_faces/                  # Store registered face images here
│
├── attendance_logs/
│   └── attendance.csv            # Auto-generated attendance records
│
├── register_face.py              # Script to register a new face
├── face_recognition_attendance.py # Main attendance system
└── view_attendance.py            # View attendance records

⚙️ Installation
1. Clone the repository:
bashgit clone https://github.com/your-username/Face_Recognition_Project.git
cd Face_Recognition_Project
2. Install required libraries:
bashpip install face_recognition opencv-python numpy dlib

⚠️ Note: dlib may require CMake on Windows. On Linux/Mac it usually installs directly.


🚀 How to Run
▶️ Step 1 — Register a Face
python register_face.py
What happens:

Enter the person's name when prompted (e.g., Padmashree)
Webcam opens with a guide oval — align your face inside it
Press SPACE to capture and save the photo
Press Q to cancel
Face is saved as known_faces/Padmashree.jpg

Enter the person's name (e.g., Rahul_Sharma): Padmashree
[INFO] Webcam ready.
  - Look directly at the camera.
  - Press SPACE to capture your photo.
  - Press Q to cancel.

[SUCCESS] Face saved as: known_faces/Padmashree.jpg
[INFO] You can now run: python face_recognition_attendance.py

▶️ Step 2 — Start the Attendance System
python face_recognition_attendance.py
What happens:

All faces from known_faces/ are loaded automatically
Webcam opens and starts recognizing faces in real time
Recognized faces shown with green box + name + confidence %
Unknown faces shown with a red box
Attendance is logged instantly to today's CSV file
Press Q to quit

[INFO] Loading known faces...
  [OK]   Loaded: Padmashree
[INFO] 1 face(s) loaded.

[INFO] Webcam started. Press 'Q' to quit.

  [LOG]  Attendance marked: Padmashree at 07:30:21

▶️Step 3 — View Attendance Report
python view_attendance.py

Output:

==================================================
  ATTENDANCE REPORT — 2026-05-13
==================================================
#    Name                      Time         Status
--------------------------------------------------
1    Padmashree                07:30:21     Present
==================================================

Or open the CSV directly:
attendance_logs/attendance_2026-05-13.csv

📊 Example CSV Record
Name,Date,Time,Status
Padmashree,2026-05-13,07:30:21,Present
