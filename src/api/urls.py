from django.conf.urls import url, include
from rest_framework import routers
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^prices/(?P<mid>[0-9]+)/$', views.PriceList.as_view()),
    url(r'^', include(router.urls)),
]


