#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/30
# @Filename       : image.py
# @Desc           :
import hashlib
import os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from django.views import View
from utils.response import ReturnCode, CommonResponseMixin

from backend_ch1_sec1 import settings
import utils.response


def image(request):
    # 判断请求的方法
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        # 在全局配置图片的路径 backend -settings
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        # 如果图片找到
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            return Http404()
    elif request.method == 'POST':
        pass

# section 3-5,3-6。 实现图片的查询，删除，和修改
class ImageView(View, CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        print(imgfile)
        if os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            # return HttpResponse(data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            response = self.wrap_json_response(code=ReturnCode.RESOURCE_NOT_FOUND)
            return JsonResponse(data=response, safe=False)

    def post(self, request):
        files = request.FILES
        response_data = []
        print(files['test'])
        for key, uploaded_file in files.items():
            print(key)
            print(uploaded_file)
            content = uploaded_file.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            print(md5)
            with open(path, 'wb+') as f:
                f.write(content)
            response_data.append({
                'name': key,
                'md5': md5
            })
        response = self.wrap_json_response(data=response_data, code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        #从url里面取出 md5
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, img_name)
        # 如果存在删除
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success.'
        # 告诉不存在
        else:
            message = 'file(%s) not found.' % img_name
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)

# section 3-4
# def image_text(request):
#     if request.method =='GET':
#         md5 = request.GET.get('md5')
#         imgfile = os.path.join(settings.IMAGES_DIR, md5+'.jpg')
#         if not os.path.exists(imgfile):
#             return utils.response.wrap_json_response(
#                 code =utils.response.ReturnCode.RESOURCES_NOT_EXISTS)
#         else:
#             response_data = {}
#             response_data['name']= md5 + '.jpg'
#             response_data['url'] = '/service/image?md5=%s'%(md5)
#             response = utils.response.wrap_json_response(data=response_data)
#             return JsonResponse(data=response, safe = False)
