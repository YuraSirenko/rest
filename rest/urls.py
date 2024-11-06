from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_app_2/', include('rest_app_2.urls', namespace='rest_app_2')),
    path('rest_app_3_template/', include('rest_app_3_template.urls', namespace='rest_app_3_template')),

]