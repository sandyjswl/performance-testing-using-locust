import flask
from flask import Response, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = {
    "name": "sandeep",
    "city": "siliguri"
}

success_response = 1


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        global success_response
        success_response += 1

        if success_response % 5 == 0:
            return Response("Error", status=500)
        return jsonify(data)
    if request.method == 'POST':
        return Response("User Added Successfully", status=200)


@app.route('/version', methods=['GET'])
def version():
    response = {"version": 1.0}
    return jsonify(response)


app.run()
