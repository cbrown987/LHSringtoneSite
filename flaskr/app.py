from flask import Flask, Response, render_template_string, render_template, request, send_file, send_from_directory

app = Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def home():
    return render_template("main.html")
@app.route("/downlad1")
def streamwav():
    audioFile = "UPLOAD_FOLDER/K Harris Ringtone.mp3"
    def generate():
        with open(audioFile, "rb") as mp3:
            data = mp3.read(1024)
            while data:
                yield data
                data = mp3.read(1024)
    return Response(generate(), mimetype="audio/x-wav") , render_template("download.html")
@app.route("/listen")
def listen():
    audioFile = "UPLOAD_FOLDER/K Harris Ringtone.mp3"
    def generate():
        with open(audioFile, "rb") as mp3:
            data = mp3.read(1024)
            while data:
                yield data
                data = mp3.read(1024)
    return Response(generate(), mimetype="audio/mpeg")





if __name__ == "__main__":
    app.run(debug=True)