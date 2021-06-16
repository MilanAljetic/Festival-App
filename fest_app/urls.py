from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import FestivalDelete, FestivalUpdate, ManagerLogin, user_list

app_name = 'fest_app'

urlpatterns = [
    path('', views.index, name='base'),
    path('manager_login/', ManagerLogin.as_view(), name='manager_login'),
    path('logout/', views.manager_logout, name='logout'),
    path('<slug:slug>/', views.festival_detail, name='festival_detail'),
    path('add_festival', views.festival_create, name='add_festival'),
    path('festival/<slug:slug>/update/',FestivalUpdate.as_view(), name='festival_update'),
    path('festival/<slug:slug>/delete/',FestivalDelete.as_view(), name='festival_delete'),
    path('festival/<slug:slug>/user_list/', views.user_list, name='user_list'),
    path('festival/<slug:slug>/apply/', views.user_apply, name='user_apply')
    #path('add_festival', PersonCreateView.as_view(), name='add_festival')
    #path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)