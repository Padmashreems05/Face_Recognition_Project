"""
register_face.py
================
Captures your photo from the webcam and saves it to the known_faces/ folder.
Run this BEFORE the main system to add yourself or others.

Usage:
    python register_face.py
"""

import cv2
import os


def register_face():
    name = input("Enter the person's name (e.g., Rahul_Sharma): ").strip()
    if not name:
        print("[ERROR] Name cannot be empty.")
        return

    # Sanitize: replace spaces with underscores
    safe_name = name.replace(" ", "_")
    save_path = os.path.join("known_faces", f"{safe_name}.jpg")
    os.makedirs("known_faces", exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam.")
        return

    print("\n[INFO] Webcam ready.")
    print("  - Look directly at the camera.")
    print("  - Press SPACE to capture your photo.")
    print("  - Press Q to cancel.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Mirror effect for natural feeling
        frame = cv2.flip(frame, 1)

        cv2.putText(frame, f"Registering: {name}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, "Press SPACE to capture | Q to quit", (10, 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (200, 200, 200), 1)

        # Draw guide oval
        h, w = frame.shape[:2]
        cv2.ellipse(frame, (w // 2, h // 2), (120, 160), 0, 0, 360, (0, 220, 255), 2)

        cv2.imshow("Register Face", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):  # SPACE
            cv2.imwrite(save_path, frame)
            print(f"\n[SUCCESS] Face saved as: {save_path}")
            print(f"[INFO] You can now run: python face_recognition_attendance.py\n")
            break
        elif key == ord("q"):
            print("[INFO] Cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    register_face()
