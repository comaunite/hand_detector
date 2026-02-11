# Hand Detector

A little Python project I used for learning real-time video feed processing and hand detection using computer vision and FastAPI.  
Includes a React frontend for visualization and interaction.

## Features

- Hand landmark detection in video frames
- FastAPI backend for processing and WebSocket streaming
- React frontend for live video and results display

## Tech Stack

- Python (OpenCV, MediaPipe, FastAPI)
- TypeScript (React + Vite)
- pip for Python dependencies
- npm for frontend dependencies

## Run backend (Windows PowerShell)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run frontend (Windows PowerShell)
```powershell
cd frontend/detector_ui
npm install
npm dev
```

## Usage

Dev URL: `http://localhost:5173/`