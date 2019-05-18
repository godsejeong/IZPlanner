import threading
import time

from flask import Flask
from flask_restful import Resource, Api
import PlanParser
import DetailsTimeParser

app = Flask(__name__)
api = Api(app)


class RegistUser(Resource):
    def post(self):
        return {'plan': plan}


class DetailPlan(Resource):
    def get(self, plan_name):
        print(plan_name)
        return {'detailPlan': detailJson[plan_name]}



api.add_resource(DetailPlan, '/allPlanList/<string:plan_name>')
api.add_resource(RegistUser, '/allPlanList')

def start_info():
    print("나오라")
    global plan
    global detailJson
    detailJson = PlanParser.detailPlan()
    plan = PlanParser.plan()
    threading.Timer(2.5, start_info()).start()

if __name__ == '__main__':
    start_info()
    app.run(host='0.0.0.0', port=3000, debug=True)

