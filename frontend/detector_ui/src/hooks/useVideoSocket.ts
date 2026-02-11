import { useEffect, useState } from "react";

export function useVideoSocket() {
	const [image, setImage] = useState<string | null>(null);

	useEffect(() => {
		let ws: WebSocket;
		let alive = true;

		try {
			ws = new WebSocket("ws://localhost:8000/ws/video");

			ws.onmessage = (event) => {
				if (!alive) return;
				const data = JSON.parse(event.data);
				setImage(data.image);
			};

			ws.onerror = (err) => {
				console.error("WebSocket error", err);
			};

			ws.onclose = (ev) => {
				console.warn("WebSocket closed", ev);
			};
		} catch (e) {
			console.error("Failed to create WebSocket", e);
		}

		return () => {
			alive = false;
			ws?.close();
		};
	}, []);

	return image;
}
