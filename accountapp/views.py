from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request에 요청관련 메서드가 다 들어가 있다
def hello_world(request):
    if request.method == "POST":
        # context
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'POST METHOD!'})
    # Get 방식으로 올때도 정의를 해줘야 에러가 안뜸
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'GET METHOD!'})