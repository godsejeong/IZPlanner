from flask import Flask
from flask_restful import Resource, Api
import PlanParser
import DetailsTimeParser

app = Flask(__name__)
api = Api(app)

class RegistUser(Resource):
    def post(self):
        return {'plan': PlanParser.plan()}

class DetailPlan(Resource):
    def get(self, plan_name):
        print(plan_name)
        detailJson = PlanParser.detailPlan()
        return {'detailPlan': detailJson}


api.add_resource(DetailPlan, '/allPlanList/<string:plan_name>')
api.add_resource(RegistUser, '/allPlanList')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
