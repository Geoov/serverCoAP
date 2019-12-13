import requests

headers = {
    'apikey': '94d5ca20-1d17-11ea-81f0-41774e6d57ad',
}

class requestConnection:
    def __init__(self):
            pass

    def getWinningBets(self):
        params = (
        	('sport', 'soccer'),
        	('country', 'germany'),
        	('league', 'soccer-germany-bundesliga')
        )

        response = requests.get('https://app.oddsapi.io/api/v1/odds', headers=headers, params=params)

        print(response.json())
