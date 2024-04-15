from contextvars import copy_context
from django.http import HttpResponse
from .functions import a, delay
from .context import requestIdCtxVar
from uuid import uuid4


def test(request):
    requestId = uuid4().hex

    requestIdCtxVar.set(requestId)

    delay()

    ctx = copy_context()
    ctx.run(lambda: a(requestId))

    return HttpResponse()


def ping(request):
    return HttpResponse("pong")
