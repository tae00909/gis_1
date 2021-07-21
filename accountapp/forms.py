# 상속받아 커스텀마이징을 해주겟따
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 그대로 받아온다.

        self.fields['username'].disabled = True

