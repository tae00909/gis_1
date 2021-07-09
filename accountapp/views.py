from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
def hello_world(request):
    if request.method == "POST":
        # context = 딕셔너리, key 값이 템플릿에서 사용할 변수 이름, value 값이 파이썬 변수가 됨
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'POST METHOD!'})
    # Get 방식으로 올때도 정의를 해줘야 에러가 안뜸
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'GET METHOD!'})