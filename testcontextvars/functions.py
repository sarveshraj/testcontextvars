from time import sleep
from random import random
from .context import roleIdCtxVar


def a(roleId: str):
    print(f"[{roleId}] Ctx var inside a(): {roleIdCtxVar.get()}")
    delay()
    b(roleId)
    return


def b(roleId: str):
    print(f"[{roleId}] Ctx var inside b(): {roleIdCtxVar.get()}\n")
    delay()
    return


def delay():
    sleep(random() * 2)
