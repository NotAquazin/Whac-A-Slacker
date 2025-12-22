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
    } else {
        statusEl.innerText = "Distracted";
        document.body.className = "distracted";
    }
}

setInterval(refreshFocus, 1000);