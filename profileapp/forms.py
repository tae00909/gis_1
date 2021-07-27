from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    # 메타 정보
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
