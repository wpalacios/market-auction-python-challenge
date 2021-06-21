from flask import Flask
from flask_restful import Api
from endpoints.market_auction import MarketAuction

app = Flask(__name__)
api = Api(app)

api.add_resource(MarketAuction, '/model/<string:model_id>/year/<string:year>')

if __name__ == '__main__':
    app.run(debug=True)
