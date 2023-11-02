from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from . models import Post

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request,'sns/index.html')

# sns.html 페이지를 부르는 sns 함수
def sns(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # sns.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져온다
    return render(request, 'sns/sns.html', {'postlist':postlist})

# sns의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html ㅠㅔ이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'sns/posting.html', {'post':post})