from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from day02.models import Employee
from day02.serializers import EmployeeModelSerializer, EmployeeDeserializer


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        emp_id = kwargs.get("id")
        if emp_id:
            try:
                emp_obj = Employee.objects.get(pk=emp_id)
                # 序列化
                emp_ser = EmployeeModelSerializer(emp_obj).data
                return Response({
                    "status": 200,
                    "message": "查询成功",
                    "results": emp_ser,
                })
            except:
                return Response({
                    "status": 500,
                    "message": "用户不存在"
                })
        else:
            emp_list = Employee.objects.all()
            #加many
            emp_ser = EmployeeModelSerializer(emp_list, many=True).data
            # print(emp_ser)
            return Response({
                "status": 200,
                "message": "查询所有成功",
                "results": emp_ser,
            })


    def post(self, request, *args, **kwargs):
        # 接受参数
        request_data = request.data

        # 验证数据合法
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                "status": 500,
                "message": "数据有误"
            })

        # 指定关键字参数 data
        deserializer = EmployeeDeserializer(data=request_data)
        # print(deserializer)

        # 使用is_valid()数据校验
        if deserializer.is_valid():
            emp_obj = deserializer.save()
            print(emp_obj)
            return Response({
                "status": 200,
                "message": "用户创建成功",
                "results": EmployeeModelSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 500,
                "message": "用户创建失败",
                "results": deserializer.errors
            })