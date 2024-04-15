from contextvars import ContextVar

requestIdCtxVar: ContextVar[str] = ContextVar("roleId", default="defaultRoleId")
