from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationsForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    models = Comment
    form_class = CommentCreationsForm
    template_name = 'commentapp/create.html'

    # 만들고 나서 해당 게시글로 돌아가야되기 때문(동적 -> get_success_url)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})