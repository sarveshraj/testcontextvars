from contextvars import copy_context
from django.http import HttpResponse
from .functions import a, delay
from .context import roleIdCtxVar
from uuid import uuid4


def test(request):
    roleId = uuid4().hex

    roleIdCtxVar.set(roleId)

    delay()

    ctx = copy_context()
    ctx.run(lambda: a(roleId))

    return HttpResponse()


def ping(request):
    return HttpResponse("pong")
