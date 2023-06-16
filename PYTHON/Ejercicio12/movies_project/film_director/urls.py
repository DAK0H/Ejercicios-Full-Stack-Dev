from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='directors_list'),
    path('<letter>', views.index, name='directors_list'),
    path('director_detail/<int:id>/', views.director_detail, name='director_detail'),
    path('film_detail/<int:id>/', views.film_detail, name='film_detail'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)