import pytest
from services.market_auction import MarketAuctionService


class TestMarketAuctionService():

    def test_get_market_auction(self):
        assert MarketAuctionService().get_by_id_and_year('67352', '2007') is not None

    @pytest.mark.parametrize('id, year', [('67352', '2007'), ('87964', '2011')])
    def test_get_correct_market_and_auction_values(self, id, year):
        expected_result = {
            'marketValue': 216384.71025600002,
            'auctionValue': 126089.52642
        }
        result = MarketAuctionService().get_by_id_and_year(id, year)

        if result is None: 
            print("no information found for given id %s and year %s" % (id, year))
        else:
            assert result['auctionValue'] == expected_result['auctionValue']