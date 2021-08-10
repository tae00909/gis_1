from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.forms import CommentCreationsForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    models = Comment
    form_class = CommentCreationsForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        # form.instance.article = Article.objects.get(pk=self.request.POST.get('article_pk'))
        # 굳이 db에 접근 안하고 id값으로 바로 할당할 수 있다.
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    # 만들고 나서 해당 게시글로 돌아가야되기 때문(동적 -> get_success_url)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})