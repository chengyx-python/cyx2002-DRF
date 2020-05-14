from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    # 异常
    error = "%s %s %s" % (context['view'], context['request'].method, exc)
    #返回值为空，自定义
    if response is None:
        return Response(
            {"error": "出错了！！！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=None)
    return response