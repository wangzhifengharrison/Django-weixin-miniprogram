
from django.urls import path

from apis.views import menu, weather, image

# from .views import weather
urlpatterns =[

    # path('',weather.helloworld)
    # path('',weather.weather)
    #path('weather',weather.weather),
    path('weather',weather.WeatherView.as_view()),
    path('menu', menu.get_menu),
    # path('image', image.image),
    # http://127.0.0.1:8000/api/v1.0/service/imagetext?md5=02bcecdf1bcbe1a2c446097ea657618c
    # path('imagetext', image.image_text)
    path('image', image.ImageView.as_view()),
    path('image/list', image.ImageListView.as_view())
]