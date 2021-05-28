from rest_framework.permissions import BasePermission


class CustomerAccessPermission(BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):

        if view.action == 'update':
            return request.user.is_authenticated \
                   and request.user.has_perm('webapp.change_article')

        return True
