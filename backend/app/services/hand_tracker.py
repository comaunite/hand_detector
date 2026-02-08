import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandTracker:
    def __init__(self):
        base_options = python.BaseOptions(
            model_asset_path="app/models/hand_landmarker.task"
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=2,
            min_hand_detection_confidence=0.7,
            min_hand_presence_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.detector = vision.HandLandmarker.create_from_options(options)

    def run(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            success, frame = cap.read()

            if not success:
                print("Feed not found.")
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            result = self.detector.detect(mp_image)

            if result.hand_landmarks:
                for hand_landmarks in result.hand_landmarks:
                    for lm in hand_landmarks:
                        h, w, _ = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(frame, (cx, cy), 3, (0, 255, 0), -1)

            cv2.imshow("Hands", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()