from django.contrib import admin
from django.urls import path
#index는 대문, blog는 게시판
from sns.views import index, sns, posting

app_name='sns'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL 이름은 index이다
    path('', index, name='index'),
    # URL:80/sns에 접속하면 sns 페이지 + URL 이름은 sns이다
    path('sns/', sns, name='sns'),
    # URL:80/SNS/숫자로 접속하면 게시들-세부페이지(posting)
    path('sns/<int:pk>/', posting, name="posting"),
]