import { useVideoSocket } from "./hooks/useVideoSocket";
import "./App.css";

function App() {
    const image = useVideoSocket();

    return (
        <div className="app-shell">
            {image ? (
                <img
                    src={`data:image/jpeg;base64,${image}`}
                    alt="Video stream"
                    className="video-stream"
                />
            ) : (
                <p className="app-status">Connecting to camera…</p>
            )}
        </div>
    );
}

export default App;
