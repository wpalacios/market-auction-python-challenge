import os
from flask import json


class MarketAuctionService():
    def get_all_data(self):
        filename = os.path.join('static', 'api-response.json')
        with open(filename) as response_data:
            data = json.load(response_data)
        return data
    
    def get_by_id_and_year(self, model_id, year):
        data = self.get_all_data()
        equipment = next((item for key, item in data.items() if key == model_id and item['schedule']['years'].get(year,None) is not None), None)

        if equipment is None:
            return None
        
        cost = equipment['saleDetails']['cost']
        year = equipment['schedule']['years'][year]
        market_ratio = year['marketRatio']
        auction_ratio = year['auctionRatio']
        
        return {
            'marketValue': cost * market_ratio,
            'auctionValue': cost * auction_ratio
        }
  