from flask import Flask, request
from markupsafe import escape
from routes.flow.post import flowPost
from routes.flow.get import flowGet
#----------------------------------
app = Flask(__name__)

@app.route("/flow", methods=["POST"])
def createFragment():
	if request.method == "POST":
		request_json = request.get_json()
		return flowPost(request_json)
	else:
		return "No existo"

@app.route("/flow/<hash>", methods=["GET"])
def consultFragment(hash):
	if request.method == "GET":
		hash = escape(hash)
		return flowGet(hash)
	else:
		return "No existo"

"""
#For documentation propouse
@app.route("/flow/entries")
def entries():
	return "Aquí están las entradas"
"""


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=4040)