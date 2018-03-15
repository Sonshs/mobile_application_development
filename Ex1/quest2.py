import math
from flask import request
from flask.views import MethodView
from flask import jsonify
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():                                             # define homepage
    return "Welcome to the Sonshs's page."


@app.route('/distance', methods=['GET', 'POST'])        # define web tinh khoang cach
def distance():
    latlng1 = request.args.get('latlng1', type=str)
    latlng2 = request.args.get('latlng2', type=str)
    cor1 = latlng1.split(",")
    cor2 = latlng2.split(",")
    lat1 = float(cor1[0])
    lng1 = float(cor1[1])
    lat2 = float(cor2[0])
    lng2 = float(cor2[1])

    lat = (lat2 - lat1) * (math.pi / 180)
    lng = (lng2 - lng1) * (math.pi / 180)
    lat1_2rad = lat1 * (math.pi / 180)
    lat2_2rad = lat2 * (math.pi / 180)
    a = math.sin(lat / 2) * math.sin(lat / 2) + math.cos(lat1_2rad) * math.cos(lat2_2rad) * math.sin(
        lng / 2) * math.sin(lng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt((1 - a)))
    d = 6371000 * c
# create data return
    data = {}
    data['coordinates'] = {}
    data['coordinates']['lat1'] = lat1
    data['coordinates']['long1'] = lng1
    data['coordinates']['lat2'] = lat2
    data['coordinates']['long2'] = lng2
    data['result'] = {}
    data['result']['distance'] = d

    return jsonify(data)                # tra ve duoi dang json


class View(MethodView):

    def get(self):
        return

    def post(self):
        return


app_view = View.as_view('app_view')

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/distance?latlng1=21.0031177,105.8201408&latlng2=10.746903,106.676292