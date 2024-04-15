from contextvars import ContextVar

requestIdCtxVar: ContextVar[str] = ContextVar("requestId", default="defaultRequestId")
