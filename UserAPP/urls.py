from django.urls import path
from UserAPP import views

urlpatterns = [
    #url(r'^user$', views.userApi),
    #url(r'^user/([0-9]+)$', views.userApi)
    path('user', views.userApi, name='user_list'),
    path('user/<int:id>', views.userApi, name='user_process')
]