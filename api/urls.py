from django.conf.urls import url, include
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
#
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# Привязываем наше API используя автоматическую маршрутизацию.
# Также мы подключим возможность авторизоваться в браузерной версии API.

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]