from django.urls import include, path
from rest_framework import routers
from crm.views.user import UserViewSet, GroupViewSet
from django.http import HttpResponse

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from crm.tasks import add
def hello_world(request):
    add.delay(1, 2)
    return HttpResponse("Hello World!")

urlpatterns = [
    path('', include(router.urls)),
    path('hello_world/', hello_world),
]