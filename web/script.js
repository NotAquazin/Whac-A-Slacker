// Alarm audio setup
import AudioAPI from './AudioAPI.js';
print("Audio running")
const audio = new AudioAPI;
audio.setupAudio(document);

// Refresh focus status every second
async function refreshFocus() {
    const data = await window.pywebview.api.get_focus_status();

    document.getElementById("windowTitle").innerText =
        data.windowTitle || "—";

    document.getElementById("reason").innerText =
        data.reason;

    const statusEl = document.getElementById("status");

    if (data.isFocused) {
        statusEl.innerText = "Focused";
        document.body.className = "focused";
        audio.stopAudio();
    } else {
        statusEl.innerText = "Distracted";
        document.body.className = "distracted";
        audio.playAudio();
    }
}

setInterval(refreshFocus, 1000);
