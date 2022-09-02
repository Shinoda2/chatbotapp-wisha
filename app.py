from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", methods=["POST"])

def response():
    query = dict(request.form)['query']
    if 'medico' in query or 'Medico' in query or 'Médico' in query or 'médico' in query:
        result = "La lista de médicos es: medico 1, medico 2, medico 3, etc..."
    else:
        result = query + " " + time.ctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)