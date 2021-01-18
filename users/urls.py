from django.urls import path, include

from users import views

app_name = 'users'

urlpatterns = [
    # django提供 'users/login/' 'users/logout/' 需要自己提供模板
    path('', include('django.contrib.auth.urls')),
    # 'users/register/'注册页面
    path('register/', views.register, name='register'),
]
