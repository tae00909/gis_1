from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel


def hello_world(request):
    # 요청 보낸 유저가 로그인되어있다면
    if request.user.is_authenticated:
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
    else:
        # 로그인 안되어있으니 로그인 페이지로 이동
        return HttpResponseRedirect(reverse('accountapp:login'))

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
#U
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') # url 성공시 어디로 이동
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        # 로그인이 되어있다면 get 함수를 사용 and get_object를 사용해 target_user를 가져올 수 있음
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            # HttpResponseForbidden -> 금지된 경로로 접근했다라는 경고가 뜸
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        # 로그인이 되어있다면 post 함수를 사용
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

#D
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        # 로그인이 되어있다면 get 함수를 사용 and get_object를 사용해 target_user를 가져올 수 있음
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            # HttpResponseForbidden -> 금지된 경로로 접근했다라는 경고가 뜸
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        # 로그인이 되어있다면 post 함수를 사용
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()