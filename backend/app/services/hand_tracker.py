import cv2
from app.services.vision_processor import VisionProcessor

class HandTracker:
    def __init__(self):
        self.vision = VisionProcessor()
        self.cap = cv2.VideoCapture(0)

    def run_local(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()

            if not success:
                print("Feed not found.")
                break

            frame = self.vision.detect_and_draw_hands(frame)

            cv2.imshow("Hands", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.release()
        cv2.destroyAllWindows()

    def read_frame(self):
        success, frame = self.cap.read()

        if not success:
            return None

        frame = self.vision.detect_and_draw_hands(frame)

        return frame

    def release(self):
        self.vision.release()
        self.cap.release()