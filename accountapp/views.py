from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')
        # 데이터베이스에 데이터를 저장해줘야하기 때문에 model에 데이터를 전송해주겟다.
        # NewModel 클래스르 받은 객체 -> model_instance
        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()



        # context = 딕셔너리, key 값이 템플릿에서 사용할 변수 이름, value 값이 파이썬 변수가 됨
        return render(request, 'accountapp/hello_world.html',
                      context={'model_instance':model_instance})
    # Get 방식으로 올때도 정의를 해줘야 에러가 안뜸
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'GET METHOD!'})