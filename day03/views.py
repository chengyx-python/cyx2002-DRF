from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from day03 import serializers
from day03.models import Book,Press,Author,AuthorDetail


class BookAPIVIew(APIView):

    def get(self, request, *args, **kwargs):
        #获取前端id
        book_id = kwargs.get("id")
        if book_id:
            try:
                book_obj = Book.objects.get(pk=book_id)
                book_ser = serializers.BookModelSerializer(book_obj).data
                return Response({
                    "status": 200,
                    "message": "查询图书成功",
                    "results": book_ser
                })
            except:
                return Response({
                    "status": 200,
                    "message": "查询图书不存在",
                })
        else:
            book_list = Book.objects.all()
            book_data = serializers.BookModelSerializer(book_list, many=True).data

            return Response({
                "status": 200,
                "message": "查询图书列表成功",
                "results": book_data
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        # 反序列化要给data赋值
        book_ser = serializers.BookModelDeSerializer(data=request_data)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()

        return Response({
            "status": 200,
            "message": "保存成功",
            "results": serializers.BookModelSerializer(book_obj).data
        })

class BookAPIVIewV2(APIView):
    #获取单个 多个
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        if book_id:
            try:
                book_obj = Book.objects.get(pk=book_id, is_delete=False)
                book_ser = serializers.BookModelSerializerV2(book_obj).data
                return Response({
                    "status": 200,
                    "message": "查询图书成功",
                    "results": book_ser
                })
            except:
                return Response({
                    "status": 200,
                    "message": "查询图书不存在",
                })
        else:
            book_list = Book.objects.filter(is_delete=False)
            book_data = serializers.BookModelSerializerV2(book_list, many=True).data

            return Response({
                "status": 200,
                "message": "查询图书列表成功",
                "results": book_data
            })
    #添加单个 多个
    def post(self, request, *args, **kwargs):
        """
        单增：传的数据是与model类对应的一个字典
        群增：[ {} {} {} ]  群增的时候可以传递列表里面嵌套与model类对应的多个字典来完成群增
        """
        request_data = request.data
        #判断增加一个还是多个  {}or[]
        if isinstance(request_data, dict):
            many = False
        elif isinstance(request_data, list):
            many = True
        else:
            return Response({
                "status": 200,
                "message": "数据格式有误",
            })

        book_ser = serializers.BookModelSerializerV2(data=request_data, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()

        return Response({
            "status": 200,
            "message": "添加成功",
            "results": serializers.BookModelSerializerV2(book_obj, many=many).data
        })
    #删除单个 多个
    def delete(self, request, *args, **kwargs):
        """
        删除单个以及删除多个
        :param request: 请求的DRF对象
        # 单个删除：  有id  且是通过路径传参  v2/books/1/
        # 多个删除： 有多个id json传参 {"ids": [1,2,3]}
        """
        book_id = kwargs.get("id")
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get("ids")

        # 判断id是否图书存在 且未删除
        res = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if res:
            return Response({
                "status": 200,
                "message": "删除成功",
            })

        return Response({
            "status": 500,
            "message": "删除失败或者已删除",
        })
    #单个整体修改
    def put(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get("id")
        try:
            book_obj = Book.objects.get(pk=book_id, is_delete=False)
        except:
            return Response({
                "status": 500,
                "message": "图书不存在",
            })

        book_ser = serializers.BookModelSerializerV2(data=request_data, instance=book_obj, partial=False)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()

        return Response({
            "status": 200,
            "message": "更新成功",
            "results": serializers.BookModelSerializerV2(book_obj).data
        })
    #单个局部修改
    def patch(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get("id")
        try:
            book_obj = Book.objects.get(pk=book_id, is_delete=False)
        except:
            return Response({
                "status": 500,
                "message": "图书不存在",
            })
        book_ser = serializers.BookModelSerializerV2(data=request_data, instance=book_obj, partial=True)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()

        return Response({
            "status": 200,
            "message": "更新成功",
            "results": serializers.BookModelSerializerV2(book_obj).data
        })