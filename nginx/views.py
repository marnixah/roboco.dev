from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import path
from .models import permissions as nginx_permissions

services = [service for code, name, service in nginx_permissions]


def return_nginx_response(request, service):
    # If user is not logged in, return 401
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    index = services.index(service)
    permission = nginx_permissions[index][0]
    # Check if the user has the permission to access the service
    if request.user.has_perm(permission):
        return HttpResponse("OK", status=200)
    else:
        return HttpResponse("Forbidden", status=403)


@login_required
def nginx_redirect(request):
    # Get redirect out of GET parameters
    redirect_url = request.GET.get("redirect", "https://roboco.dev/")
    # Redirect to the redirect_url
    return HttpResponseRedirect(redirect_url)


# /nginx/[service]
urlpatterns = [
    path(
        r"^nginx/(?P<service>{})$".format("|".join(services)),
        return_nginx_response,
        name="nginx",
    ),
    path(
        "nginx/redirectback",
        nginx_redirect,
    ),
]