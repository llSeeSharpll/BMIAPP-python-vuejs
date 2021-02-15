from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS
from entities.Bmiclass import Bmi


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/bmi', methods=['POST'])
def bmi():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        hieght1 = post_data.get('hieght')
        wieght2 = post_data.get('wieght')
        name = post_data.get('name')
        hieght=float(hieght1)
        wieght=int(wieght2)
        U1 = Bmi(name, wieght, hieght)
        result = U1.calculate_bmi()
        response_object['bmi'] = result
        return jsonify(response_object)
    else:
        return jsonify("error")


if __name__ == '__main__':
    app.run()
