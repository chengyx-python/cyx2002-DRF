from rest_framework import serializers, exceptions

from day02.models import Employee
from DRF import settings


class EmployeeModelSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()

    # SerializerMethodField 自定义一个序列化字段
    aaa = serializers.SerializerMethodField()
    # 自定义字段
    def get_aaa(self, obj):
        return "example"

    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        print(obj.gender, type(obj))
        #获取choic类型的值
        return obj.get_gender_display()  #male/female/other

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


class EmployeeDeserializer(serializers.Serializer):
    # 添加反序列化校验规则 错误信息
    username = serializers.CharField(
        max_length=10,
        min_length=5,
        error_messages={
            "max_length": "长度太长",
            "min_length": "长度太短"
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField(required=False)

    # 重复密码
    re_pwd = serializers.CharField()

    # 局部校验钩子 对反序列化器中的某个字段进行校验
    def validate_username(self, value):
        if "1" in value:
            raise exceptions.ValidationError("用户名异常")
        return value

    # 全局的校验钩子，会对反序列化器中所有校验规则进行验证
    def validate(self, attrs):
        print(attrs, "attr")
        password = attrs.get("password")
        re_pwd = attrs.pop("re_pwd")
        if password != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")
        return attrs


    # 在create方法完成保存之前  会先调用局部钩子
    def create(self, validated_data):
        print(validated_data)
        return Employee.objects.create(**validated_data)