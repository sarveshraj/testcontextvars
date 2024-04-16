from contextvars import ContextVar, copy_context
from uuid import uuid4

requestIdCtxVar: ContextVar[str] = ContextVar("requestId", default="defaultRequestId")


def wrapper(view):
    def f(request, *args, **kwargs):
        # using request.META as request.headers does not support assignment
        requestId = request.META.get("HTTP_X_REQUEST_ID")
        if not requestId:
            requestId = uuid4().hex
            request.META["HTTP_X_REQUEST_ID"] = requestId

        requestIdCtxVar.set(requestId)

        ctx = copy_context()
        return ctx.run(lambda: view(request, *args, **kwargs))

    return f
