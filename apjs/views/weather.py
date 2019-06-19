from django.http import HttpResponse


def helloworld(request):
    print('request method  ', request.method)
    print('request meata  ', request.META)
    print('request cookies', request.COOKIES)
    return HttpResponse("ok is git is working now ")
    pass