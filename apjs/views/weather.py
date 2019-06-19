from django.http import HttpResponse,JsonResponse, FileResponse

from thirdparty import juhe

import json
def helloworld(request):
    print('request method  ', request.method)
    print('request meata  ', request.META)
    print('request cookies', request.COOKIES)
    # return HttpResponse(content="ok is git is working now ",status=200)
    m = {
        "message": "hello world is a django project"
    }
    return JsonResponse(data=m, safe=False, status=200)
    pass

def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data,status=200)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data =[]
        for city in cities:
            result = juhe.weather(city)
            result["city"]=city
            response_data.append(result)
        return JsonResponse(data=response_data,safe=False,status=200)
