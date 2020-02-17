# 本身存在异常处理的函数
from rest_framework.views import exception_handler
# 数据库错误
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status  # 返回http的状态码信息

import logging  # 引入日志器

logger = logging.getLogger('django')  # 日志记录对象


# 申明自定义的异常处理函数   异常对象，异常信息的上下文
def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法
    response = exception_handler(exc, context)
    # 最后报错返回response.没报错返回None,None有可能成功，有可能代表数据库错误
    if response is None:
        view = context['view']  # 异常发生时的上下文信息，报错的视图，是一个字典
        if isinstance(exc, DatabaseError):  # 判断是否是数据库错误
            logger.error('[%s] %s' % (view, exc))  # 数据库异常
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
