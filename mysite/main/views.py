from django.shortcuts import render
from articles.models import Question
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj} # {'question_list': <QuerySet [<Question: 장고 모델 질문입니다.>, <Question: pybo가 무엇인가요?>]>}
    return render(request, 'index.html', context)

