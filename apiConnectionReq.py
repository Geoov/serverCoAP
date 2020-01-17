import requests



class apiConnectionReq():
    def __init__(self):
        pass

    def getAvioanie(self):

        # url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
        #
        # payload = "inboundDate=2019-09-10&cabinClass=business&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2019-09-01&adults=1"
        # headers = {
        #     'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        #     'x-rapidapi-key': "1ea5073e92msh39ba2d78b013112p103844jsnd22447afdf9c",
        #     'content-type': "application/x-www-form-urlencoded"
        #     }
        #
        # response = requests.request("POST", url, data=payload, headers=headers)

        url = "https://api.nasa.gov/planetary/apod?api_key=CJdQV1LWyWDGQRFPcZ9KCWitdgmGpxlOAOLHCj5A"
        r = requests.get(url)

        print(r.text)
