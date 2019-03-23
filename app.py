from flask import Flask
from flask_restful import Resource, Api
import PlanParser
import DetailsTimeParser
import threading
import json
app = Flask(__name__)
api = Api(app)



class RegistUser(Resource):
    def post(self):
        return {'plan': PlanParser.plan()}

class DetailPlan(Resource):
    def get(self, plan_name):
        print(plan_name)
        # DetailsTimeParser.TimeParser.set_info(plan_name)
        detailJson = PlanParser.detailPlan()
        planVaule = detailJson[plan_name]
        plan = DetailsTimeParser.TimeParser.parser(planVaule)
        return {'detailPlan': plan}


api.add_resource(DetailPlan, '/allPlanList/<string:plan_name>')
api.add_resource(RegistUser, '/allPlanList')

if __name__ == '__main__':
    app.run(debug=True)
