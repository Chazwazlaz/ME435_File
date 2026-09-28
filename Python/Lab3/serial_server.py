import flask
import plateloader
import threading

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
loader = plateloader.PlateLoader()


@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")

@app.get("/api/<command>")
def handle_plateloader_commands(command):
    with serial_lock:
        responce = loader.send_command(command)
    #todo: run the command
    return "Success!"



if __name__ == "__main__":
    print("Running Flask")
    app.run(host="0.0.0.0", port=8080, debug=True) # use_reloader=False