from api_account.constant.Data import RoleData
from api_account.permisisons.MyBasePermission import MyBasePermission


class AdminPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN]


class UserPermission(MyBasePermission):
    match_any_roles = [RoleData.USER]


class UserOrAdminPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN, RoleData.USER]
