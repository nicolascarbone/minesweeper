"""minesweeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import TokenViewSet, UserViewSet
from grids.views import GridViewSet
from elements.views import ElementViewSet

router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'user', UserViewSet, base_name='user')

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('grids/', GridViewSet.as_view({
        'get': 'get_older_games',
        'post': 'create'
        })
    ),
    path('grids/<int:pk>', GridViewSet.as_view({
        'get': 'get',
        'delete': 'delete'
        })
    ),
    path(
        'grids/<int:grid>/squares/<int:row>/<int:cell>/explore',
        GridViewSet.as_view({'post': 'explore'})
    ),
    path('api/', include(router.urls)),
    path('api/token/', TokenViewSet.as_view()),
    path('api/user/', UserViewSet.as_view())
]
