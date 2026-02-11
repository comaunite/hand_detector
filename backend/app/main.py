from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.services.hand_tracker import HandTracker
import cv2
import base64
import asyncio

# if __name__ == "__main__":
#    HandTracker().run()
app = FastAPI()

@app.websocket("/ws/video")
async def video_ws(ws: WebSocket):
    await ws.accept()
    tracker = HandTracker()

    try:
        while True:
            frame = tracker.read_frame()
            if frame is None:
                break

            _, buffer = cv2.imencode(".jpg", frame)
            jpg_as_text = base64.b64encode(buffer).decode("utf-8")

            await ws.send_json({
                "image": jpg_as_text
            })

            await asyncio.sleep(0.03)  # ~30 FPS

    except WebSocketDisconnect:
        pass
    finally:
        tracker.release()
