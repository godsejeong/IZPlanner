from flask import Flask
from flask_restful import Resource, Api
import PlanParser
app = Flask(__name__)
api = Api(app)

class RegistUser(Resource):
    def post(self):
        return {'plan':PlanParser.PlanningJson}


api.add_resource(RegistUser,'/allPlanList')


if __name__ == '__main__':
    app.run(debug=True)
