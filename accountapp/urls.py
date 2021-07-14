from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 장고에서 제공해주는 LoginView
    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    # 로그아웃
    path('logout/',LogoutView.as_view(), name='logout'),

    # AccountCreateView는 클래스이기 때문에 as_view를 추가
    path('create/', AccountCreateView.as_view(), name='create')
]