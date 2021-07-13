from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
from django.urls import reverse

from accountapp.models import NewModel


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