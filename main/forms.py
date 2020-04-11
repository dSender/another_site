from django import forms
from .models import CustomUser, Post


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        return self.cleaned_data


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'img')


class UserSettings(forms.ModelForm):
	class Meta:
		models = CustomUser
		fields = ('avatar', )


class AccountSettingsForm(forms.Form):
    avatar = forms.FileField(required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    old_password = forms.CharField(widget=forms.PasswordInput, required=True)
