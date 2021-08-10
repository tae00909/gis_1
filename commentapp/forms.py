from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationsForm(ModelForm):
    class Meta
        models = Comment
        fields = ['content']
