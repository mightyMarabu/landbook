from flask import Flask, render_template, Response


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bender/<id>")
def bender(id = id):
    return Response("{id: %s}" %id, mimetype = "application/json")


if __name__ == "__main__":
    app.run(debug = True)
