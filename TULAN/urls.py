from django.contrib import admin
from django.urls import path
from App.views import index, gallery, trade_hubs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('gallery/', gallery, name='gallery'),
    path('trade_hubs/', trade_hubs_view, name='trade_hubs'),
]