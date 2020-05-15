from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from day03_lianxi import serializers
from day03_lianxi.models import Emp


class EmpAPIView(APIView):
    #获取单个多个
    def get(self,request,*args,**kwargs):
        emp_id = kwargs.get('id')
        if emp_id:
            try:
                emp_obj = Emp.objects.get(pk=emp_id, is_alive=False)
                emp_ser = serializers.EmpModelSerializer(emp_obj).data
                return Response({
                    "status": 200,
                    "message": "查询成功",
                    "results": emp_ser
                })
            except:
                return Response({
                    "status": 200,
                    "message": "查询失败",
                })
        else:
            emp_list = Emp.objects.filter(is_alive=False)
            emp_data = serializers.EmpModelSerializer(emp_list, many=True).data

            return Response({
                "status": 200,
                "message": "查询所有员工成功",
                "results": emp_data
            })

    #添加单个多个
    def post(self, request, *args, **kwargs):
        request_data = request.data
        if isinstance(request_data, dict):
            many = False
        elif isinstance(request_data, list):
            many = True
        else:
            return Response({
                "status": 200,
                "message": "格式错误",
            })

        emp_ser = serializers.EmpModelSerializer(data=request_data, many=many)
        emp_ser.is_valid(raise_exception=True)
        emp_obj = emp_ser.save()

        return Response({
            "status": 200,
            "message": "添加成功",
            "results": serializers.EmpModelSerializer(emp_obj, many=many).data
        })

     #删除单个多个
    def delete(self, request, *args, **kwargs):
        print('1')
        emp_id = kwargs.get("id")
        if emp_id:
            ids = [emp_id]
        else:
            ids = request.data.get("ids")
        res = Emp.objects.filter(pk__in=ids, is_alive=False).update(is_alive=True)
        if res:
            return Response({
                "status": 200,
                "message": "删除成功",
            })

        return Response({
            "status": 500,
            "message": "删除失败",
        })

    #单体 整个修改
    def put(self, request, *args, **kwargs):
        request_data = request.data
        emp_id = kwargs.get("id")
        try:
            emp_obj = Emp.objects.get(pk=emp_id, is_alive=False)
        except:
            return Response({
                "status": 500,
                "message": "员工不存在",
            })
        emp_ser = serializers.EmpModelSerializer(data=request_data, instance=emp_obj, partial=False)
        emp_ser.is_valid(raise_exception=True)
        emp_ser.save()
        return Response({
            "status": 200,
            "message": "整体更新成功",
            "results": serializers.EmpModelSerializer(emp_obj).data
        })

        # 单个局部修改

    #单体 局部修改
    def patch(self, request, *args, **kwargs):
        request_data = request.data
        emp_id = kwargs.get("id")
        try:
            emp_obj = Emp.objects.get(pk=emp_id, is_alive=False)
        except:
            return Response({
                "status": 500,
                "message": "员工不存在",
            })
        emp_ser = serializers.EmpModelSerializer(data=request_data, instance=emp_obj, partial=True)
        emp_ser.is_valid(raise_exception=True)
        emp_ser.save()
        return Response({
            "status": 200,
            "message": "局部更新成功",
            "results": serializers.EmpModelSerializer(emp_obj).data
        })
