from django.shortcuts import render

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request,'sns/index.html')

# sns.html 페이지를 부르는 blog 함수
def sns(request):
    return render(request, 'sns/sns.html')