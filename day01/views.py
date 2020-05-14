
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser,JSONParser
from rest_framework.renderers import BrowsableAPIRenderer,TemplateHTMLRenderer,JSONOpenAPIRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from day01.models import UserInfo


# def user(request):
#     print("请求到达")
#     if request.method == "GET":
#         print("GET")
#     elif request.method == "POST":
#         print("post")
#     return HttpResponse("post SUCCESS")

# @method_decorator(csrf_exempt)
# class UserView(View):
#     """单个"""
#     def get(self,request,*args,**kwargs):
#         user_id = kwargs.get("pk")
#         if user_id:
#             user_val = UserInfo.objects.filter(pk=user_id).values().first()
#             if user_val:
#                 return JsonResponse({
#                     "status":200,
#                     "message":"获取用户成功",
#                     "results":user_val
#                 })
#         #多个
#         else:
#             user_list = UserInfo.objects.all().values()
#             if user_list:
#                 return JsonResponse({
#                     "status": 200,
#                     "message": "获取用户成功",
#                     "results": list(user_list)
#                 })
#         return JsonResponse({
#             "status": 400,
#             "message": "获取用户不存在",
#         })
#     def post(self,request,*args,**kwargs):
#         try:
#             user_obj = UserInfo.objects.create(**request.POST.dict())
#             if user_obj:
#                 return JsonResponse({
#                     "status": 200,
#                     "message": "添加用户成功",
#                     "results": {"username":user_obj.username,"password":user_obj.password}
#                     })
#             else:
#                 return JsonResponse({
#                     "status": 500,
#                     "message": "添加用户失败",
#                 })
#         except:
#             return JsonResponse({
#                 "status": 501,
#                 "message": "参数有误！",
#             })
#
#
#         return HttpResponse("post SUCCESS")

class StudentView(APIView):
    #单独配置渲染器
    # renderer_classes = [BrowsableAPIRenderer]
    # parser_classes = [MultiPartParser]
    def get(self,request,*args,**kwargs):
        print(request._request.GET)
        print(request.GET)
        print(request.query_params)
        return Response('GET')

    def post(self,request,*args,**kwargs):
        print(request._request.POST)
        print(request.data)
        print(request.POST)
        return Response('POST')

class StudentView2(APIView):
    # renderer_classes = [BrowsableAPIRenderer]
    # parser_classes = [JSONParser]
    def get(self,request,*args,**kwargs):
        stu_id = kwargs.get("id")
        if stu_id:
           stu_obj = UserInfo.objects.filter(id=stu_id).values().first()
           if stu_obj:
               return Response({
                   "status":200,
                   "message":"获取成功",
                   "results":stu_obj,
               })
           else:
               return Response({
                   "status": 500,
                   "message": "获取失败",
               })
        else:
            stus = UserInfo.objects.all().values()
            return Response({
                "status": 200,
                "message": "获取所有用户成功",
                "results":list(stus)
            })
        return Response("GET")

    def post(self,request,*args,**kwargs):
        # print(request.POST)
        # data = request.data
        try:
            stu_obj = UserInfo.objects.create(**request.POST.dict())
            # stu_obj = UserInfo.objects.create(**data)
            if stu_obj:
                return Response({
                    "status":200,
                    "message":"创建成功",
                    "results":{
                        "username": stu_obj.username,
                        "password": stu_obj.password
                    }
                })
            else:
                return Response({
                    "status": 500,
                    "message": "创建失败",
                })
        except:
            return Response({
                "status": 500,
                "message": "参数有误",
            })
        return Response("post")