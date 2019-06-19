import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = 'eeeddf1125c901054f066c5c58ecb484'
    api = 'https://api.openweathermap.org/data/2.5/weather'
    params = 'q=%s&appid=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)
    weather = json_data.get('weather')
    weather_main = weather[0].get('main')
    print(weather_main)

    response = dict()
    response['weather_main'] = weather[0].get('main')
    response['temp'] = json_data.get('main').get('temp')
    print(response)
    return response


if __name__ == '__main__':
    data = weather('Canberra,au')
