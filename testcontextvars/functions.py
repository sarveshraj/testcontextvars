from time import sleep
from random import random
from .context import requestIdCtxVar


def a(requestId: str):
    print(f"[{requestId}] Ctx var inside a(): {requestIdCtxVar.get()}")
    delay()
    b(requestId)
    return


def b(requestId: str):
    print(f"[{requestId}] Ctx var inside b(): {requestIdCtxVar.get()}\n")
    delay()
    return


def delay():
    sleep(random() * 2)
