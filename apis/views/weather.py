import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from utils.response import CommonResponseMixin
from thirdparty import juhe

# 3-1 section
# def helloworld(request):
#     print('request method  ', request.method)
#     print('request meata  ', request.META)
#     print('request cookies', request.COOKIES)
#     # return HttpResponse(content="ok is git is working now ",status=200)
#     m = {
#         "message": "hello world is a django project"
#     }
#     return JsonResponse(data=m, safe=False, status=200)
#     pass

# 3-7 section 之前的
# def weather(request):
#     if request.method == 'GET':
#         city = request.GET.get('city')
#         data = juhe.weather(city)
#         return JsonResponse(data=data,status=200)
#     elif request.method == 'POST':
#         received_body = request.body
#         received_body = json.loads(received_body)
#         cities = received_body.get('cities')
#         response_data =[]
#         for city in cities:
#             result = juhe.weather(city)
#             result["city"]=city
#             response_data.append(result)
#         return JsonResponse(data=response_data,safe=False,status=200)

# 3-7 section
class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = juhe.weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = self.wrap_json_response(data)
        return JsonResponse(data=response_data, safe=False)