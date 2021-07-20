from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 장고에서 제공해주는 LoginView
    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    # 로그아웃
    path('logout/',LogoutView.as_view(), name='logout'),

    # AccountCreateView는 클래스이기 때문에 as_view를 추가
    path('create/', AccountCreateView.as_view(), name='create'),
    # <int:pk> pk라는 이름의 숫자를 받는다. -> primary key 약자 이 고유값을 통해서 어떤 account를 받아올지
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]