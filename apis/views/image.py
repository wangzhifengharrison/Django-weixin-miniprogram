#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/30
# @Filename       : image.py
# @Desc           :


import os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from backend_ch1_sec1 import settings
import utils.response

def image(request):
    #判断请求的方法
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        # 在全局配置图片的路径 backend -settings
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        #如果图片找到
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            #return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            return Http404()
    elif request.method == 'POST':
        pass

def image_text(request):
    if request.method =='GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5+'.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(
                code =utils.response.ReturnCode.RESOURCES_NOT_EXISTS)
        else:
            response_data = {}
            response_data['name']= md5 + '.jpg'
            response_data['url'] = '/service/image?md5=%s'%(md5)
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe = False)