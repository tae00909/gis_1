from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel

# 장고에서 제공해주는 데코레이터
# login_url -> 로그인 위치의 경로 ('account/login 이면 설정안해줘도 된다)
@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')
        # 데이터베이스에 데이터를 저장해줘야하기 때문에 model에 데이터를 전송해주겟다.
        # NewModel 클래스르 받은 객체 -> model_instance
        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        # newmodel 데이터 베이스의 오브젝트의 모든 데이터를 가져오겠다는 뜻
        data_list = NewModel.objects.all()

        # Redirect(재연결) -> 어디로 제연결?? ->
        # 주소가 길어질때
        # app_name = 'accountapp'을 설정한 적 있다.
        # 그리고 name='hello_world' 네이밍 해준적 있다.
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

#C
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm # 장고에서 제공해주는 회원가입 폼
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

#R?
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # 해당 객체에 어떻게 접근할 것인지
    template_name = 'accountapp/detail.html'


has_ownership = [login_required, account_ownership_required]


#U
# 장고에서 제공해주는 데코레이터 -> 메서드를 변환해준다.
# login_required는 함수를 위한 것인데 메서드를 위한것으로 변환
@method_decorator(has_ownership, 'get') # get 방식
@method_decorator(has_ownership, 'post') # post 방식
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') # url 성공시 어디로 이동
    template_name = 'accountapp/update.html'


#D
@method_decorator(has_ownership, 'get') # get 방식
@method_decorator(has_ownership, 'post') # post 방식
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
