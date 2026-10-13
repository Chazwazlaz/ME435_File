import flask
import arduino
import threading

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
LEDFlasher = arduino.arduino("COM4")


@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")


@app.get("/api/led/<state>")
def handle_led(state):
    with serial_lock:
        response = LEDFlasher.send_command(f"LED {state.upper()}")
    return response


@app.get("/api/flash/<int:num_flashes>/<int:period_ms>")
def handle_flash(num_flashes, period_ms):
    with serial_lock:
        response = LEDFlasher.send_command(f"FLASH {num_flashes} {period_ms}")
    return response


if __name__ == "__main__":
    print("Running Flask")
    LEDFlasher.connect()
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)