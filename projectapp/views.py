from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    #MultipleObjectMixin를 적으면 paginate_by 사용가능
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # 구독이 됐는지 안됐는지
        user = self.request.user
        project = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)
        else:
            subscription = None

        # Article 모델에서 만든 project가 현재 오브젝트(target_project)와 같은 것만 필터
        article_list = Article.objects.filter(project=self.object)
        # object_list에 위에서 뽑은 article_list 할당
        return super().get_context_data(object_list = article_list,
                                        subscription=subscription,
                                        **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20