import test as test
from flask import Flask, json, request
app = Flask(__name__)

@app.route('/json', methods=['GET'])
def get_json():
	if request.method == 'GET':
		with open("Random (Responses)", "r") as file:
			file_data = file.read()
		jsON = test.clean_up(file_data)
		return jsON
	else:
		return "INVALID"

if __name__ == '__main__':
	app.run()
