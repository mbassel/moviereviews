from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        fieldnames = ['username', 'password1', 'password2']
        for fieldname in fieldnames:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )
