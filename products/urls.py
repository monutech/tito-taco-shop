from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('<int:product_id>/images/<str:filename>', views.get_image, name='product-img'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)