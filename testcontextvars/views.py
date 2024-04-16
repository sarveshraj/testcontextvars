from django.http import HttpResponse
from .functions import delay, a


def test(request):
    delay()
    a(request.META.get("HTTP_X_REQUEST_ID"))
    return HttpResponse("Test complete")


def ping(request):
    return HttpResponse("pong")
