from flask import Flask, render_template, Response, jsonify
from db_conn import insert_into_db, resetMap, getDatafromDB
import json

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/save/")
def submit():
#    sub = {"id":"2"}
#    sub = ["What am", "I doing?"]
    sub = insert_into_db()
    return Response(json.dumps(sub), mimetype = "application/json")

@app.route("/save/<lat>/<lng>/<radius>/<lastname>/<more>/<use>")
def savePoint(lat, lng, radius, lastname, more, use):
    poi = insert_into_db("landbook.insert_data", (lat,lng,radius,lastname,more,use))
    return jsonify("data submitted!")

@app.route("/getData/")
def getTableData():
    dat = getDatafromDB()
    return Response(json.dumps(dat), mimetype = "application/json")
    print("dat")

@app.route("/reset/")
def reset():
#    res = {"id":"3"}
    res = resetMap()
    return jsonify("map reseted!")
#    return Response(json.dumps(res), mimetype = "application/json")

if __name__ == "__main__":
    app.run(debug = True)
    app.run(host='0.0.0.0', port=80)
