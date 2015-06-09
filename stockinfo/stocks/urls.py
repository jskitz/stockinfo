from django.conf.urls import include, url

from rest_framework import routers

from stockinfo.stocks import views

router = routers.DefaultRouter()
router.register(r'stocks', views.StockViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
