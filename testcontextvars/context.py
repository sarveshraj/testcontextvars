from contextvars import ContextVar

roleIdCtxVar: ContextVar[str] = ContextVar('roleId', default='defaultRoleId')