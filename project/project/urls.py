from django.contrib import admin
from django.urls import path,include;
from rest_framework_jwt.views import (obtain_jwt_token,
verify_jwt_token,refresh_jwt_token);
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/',include("task.urls")),
    path("apis/auth/",include('rest_framework.urls',namespace="resturls")),
    path('api-token-auth/', obtain_jwt_token,name="obtain"),
    path("api-token-refresh/'", refresh_jwt_token,name="refresh"),
    path("api-token-verify/", verify_jwt_token,name="verify")
]
