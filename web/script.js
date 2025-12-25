// Alarm audio setup
import AudioAPI from './AudioAPI.js';
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

// Button to start/stop focus checking
let button = document.getElementById('checkerButton');
button.addEventListener('click', function() {
    if (button.innerText === 'Start') {
        window.pywebview.api.start_tracking();
        button.innerText = 'Stop';
        refreshFocus();
        window.focusInterval = setInterval(refreshFocus, 1000);
    }
    else {
        button.innerText = 'Start';
        window.pywebview.api.stop_tracking();
        clearInterval(window.focusInterval);
        document.getElementById("windowTitle").innerText = "—";
        document.getElementById("reason").innerText = "—";
        document.getElementById("status").innerText = "Whac-A-Slacker";
        document.body.className = "idle";
        audio.stopAudio();
    }

});

