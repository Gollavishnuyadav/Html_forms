
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('Topic_insert/',Topic_insert,name="Topic_insert"),
    path('Webpage_retrieve/',Webpage_retrieve,name="Webpage_retrieve"),
    path('webpage_insert/',webpage_insert,name="webpage_insert"),
    path('Access_insert/',Access_insert,name="Access_insert"),
    path('checkbox/',checkbox,name='checkbox'),
    path('Radio/',Radio,name="Radio"),
    # path('update/',update,name="update"),
    # path('update_Topic/',update_Topic,name="update_Topic"),
    path('access_display/',access_display,name="access_display"),
]
