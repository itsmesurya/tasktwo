from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    fields = ("username", "password")
    model = get_user_model()

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["username"].label = "Display name"
