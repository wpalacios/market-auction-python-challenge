# Market Auction Python Challenge
This is a small implementation for the challenge described in `Exercise.txt`, it was written in Python using Flask.
## Setup 
- Install correct Python version 3.9.2 (usage of pyenv and virtual env is preferred)
- Install dependencies from `requirements.txt`
- You can use Visual Studio Code editor built-in feature to run and debug the project or run it from a terminal by executing `python app.py` command


## Project structure
- endpoints 
  - market_auction: Contains a class Resource, representing an abstract RESTful resource. It will get the market and auction value for a given model id and year or return a 404 status code with a friendly message if no information found with the provided parameters. URL: /model/<int:model_id>/year/<int:year_id>
- services/market_auction: Implements some methods to get all the information contained in `static/api-response.json` and filter values by id and year and return and object containing computed values (as specified in `Exercise.txt`) for market and auction.
- tests: Contains all unit tests for `MarketAuctionService`
- static: folder to store mock data (`api-response.json`) for the exercise
