from flask_restful import Resource, abort
from services.market_auction import MarketAuctionService


class MarketAuction(Resource): 
    def get(self, model_id, year):
        market_auction =  MarketAuctionService().get_by_id_and_year(model_id, year)

        if market_auction is None:
            return abort(404, message='No information found for the given ID and/or year')

        return market_auction
