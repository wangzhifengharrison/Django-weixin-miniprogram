import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    # 完全是其他天气 api
    key = 'eeeddf1125c901054f066c5c58ecb484'
    api = 'https://api.openweathermap.org/data/2.5/weather'
    params = 'q=%s&appid=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)

    response = dict()
    response['temperature']=json_data.get('main').get('temp')
    response['wind_direction'] =json_data.get('wind').get('deg')
    response['wind_strength'] = json_data.get('wind').get('speed')
    response['humidity'] = json_data.get('main').get('humidity')
    response['time'] = json_data.get('dt')
    print(response)
    return response


if __name__ == '__main__':
    data = weather('Canberra,au')
