import os
from flask import json


class MarketAuctionService():
    def get_all_data(self):
        filename = os.path.join('static', 'api-response.json')
        with open(filename) as response_data:
            data = json.load(response_data)
        return data
    
    def get_values_for_year(self, year, equipment_data):
        floor_year = min(equipment_data['schedule']['years'])
        ceiling_year = max(equipment_data['schedule']['years'])

        if year < floor_year:
            start_year = floor_year
            def_market_ratio = 1 - equipment_data['schedule']['defaultMarketRatio']
            def_auction_ratio = 1 - equipment_data['schedule']['defaultAuctionRatio']
        else:
            start_year =  ceiling_year
            def_market_ratio = 1 + equipment_data['schedule']['defaultMarketRatio']
            def_auction_ratio = 1 + equipment_data['schedule']['defaultAuctionRatio']
         
        # if year is less than min year from all data then decrease amount of years and default market ratio
        # if year is greater than max year from all data then increase amount of years and default market ratio
        difference = abs(int(start_year) - int(year))
        values = equipment_data['schedule']['years'][start_year]
        for i in range(difference):
            values['marketRatio'] = values['marketRatio'] * def_market_ratio
            values['auctionRatio'] = values['auctionRatio'] * def_auction_ratio

        return values

    def get_by_id_and_year(self, model_id, year):
        data = self.get_all_data()
        equipment = next((item for key, item in data.items() if key == model_id), None)

        if equipment is None:
            return None
        
        requested_year = next((item for item in equipment['schedule']['years'] if equipment['schedule']['years'].get(year, None) is not None), None)

        if requested_year is None:
            computed_year_values = self.get_values_for_year(year, equipment)
        
        cost = equipment['saleDetails']['cost']
        year = computed_year_values if requested_year is None else equipment['schedule']['years'][year]
        market_ratio = year['marketRatio']
        auction_ratio = year['auctionRatio']
        
        return {
            'marketValue': cost * market_ratio,
            'auctionValue': cost * auction_ratio
        }
'''
"2006": { "marketRatio": 0.311276, "auctionRatio": 0.181383 },

0.311276 
0.30505048 (n-0.02)
0.2989494704 (n-0.02)'''