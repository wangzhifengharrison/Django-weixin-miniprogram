import json
import requests
import time

from utils import proxy


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
    response['temperature'] = json_data.get('main').get('temp')
    response['wind_direction'] = json_data.get('wind').get('deg')
    response['wind_strength'] = json_data.get('wind').get('speed')
    response['humidity'] = json_data.get('main').get('humidity')
    response['time'] = json_data.get('dt')
    print(response)
    return response


# third party information
def constellation(cons_name):
    '''
    :param cons_name: 星座名字
    :return: json 今天运势
    '''
    key = '638590d043a54639f3560b5381f5c4f0'
    api = 'http://web.juhe.cn:8080/constellation/getAll'
    types = ('today', 'tomorrow', 'week', 'month', 'year')
    params = 'consName=%s&type=%s&key=%s' % (cons_name, types[0], key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    return {
        'name': cons_name,
        'text': data['summary']
    }


# third party information
def stock(market, code):
    '''
    沪深股票
    :param market: 上交所 = sh, 深交所 = sz
    :param code: 股票编号
    :return:
    '''
    key = 'f887b09847c9bcde9801ca7aaa86513e'
    api = 'http://web.juhe.cn:8080/finance/stock/hs'
    params = 'gid=%s&key=%s' % (market + code, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    data = data.get('result')[0].get('data')
    response = {
        'name': data.get('name'),
        'now_price': data.get('nowPri'),
        'today_min': data.get('todayMin'),
        'today_max': data.get('todayMax'),
        'start_price': data.get('todayStartPri'),
        'date': data.get('date'),
        'time': data.get('time')
    }
    response['is_rising'] = data.get('nowPri') > data.get('todayStartPri')
    sub = abs(float(data.get('nowPri')) - float(data.get('todayStartPri')))  # 差值
    response['sub'] = float('%.3f' % sub)
    return response


# third party information
def history_today():
    key = '6c6b318d983b6b4ac8cc5cda0da92155'
    api = 'http://api.juheapi.com/japi/toh'
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    params = 'v=1.0&month=%d&day=%d&key=%s' % (month, day, key)
    url = api + '?' + params
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    result_list = data.get('result')
    result = []
    for item in result_list:
        result.append({
            'title': item.get('title'),
            'content': item.get('des')
        })
    return result


if __name__ == '__main__':
    data = weather('Canberra,au')
