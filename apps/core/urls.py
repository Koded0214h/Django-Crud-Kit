from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('create_item/', views.create_item, name='create_item'),
    path('read_items/', views.read_items, name='read_items'),
    path('update_item/<int:id>/', views.update_item, name='update_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('create_category/', views.create_category, name='create_category'),
    path('item/<int:id>/', views.item, name='item')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)