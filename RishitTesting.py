import requests


class RishitTesting:
    def returnSomething(self):
        response = requests.get(
            'http://api.positionstack.com/v1/forward?access_key=98a9d61a363c46bbd1f387f0b9f334ad&query=1600%20Pennsylvania%20Ave%20NW,%20Washington%20DC')
        key = '98a9d61a363c46bbd1f387f0b9f334ad'
        data = response.json()
        return data['data'][0]['latitude']
