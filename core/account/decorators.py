from django.core.exceptions import PermissionDenied
from account.models.user import User

def is_company(function):
    def wrap(request, *args, **kwargs):
        users = User.objects.get(email=request.user.email)
        if users.company == True:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
            
    return wrap