from rest_framework import serializers

from day03_lianxi.models import Emp


class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ('name','age','addr','salary')
        extra_kwargs = {
            "name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "员工名字必填的",
                    "min_length": "名字长度有问题"
                }
            },
            "age": {
                "write_only": True
            },
            "addr": {
                "write_only": True
            },
            "salary": {
                "write_only": True
            },
        }
        #局部钩子
        #


        def validate(self, attrs):
            name = attrs.get("name")
            addr = attrs.get("addr")
            emp_obj = Emp.objects.filter(name=name, addr=addr)
            if emp_obj:
                raise serializers.ValidationError("该员工已存在")
            return attrs