from django.contrib.auth.forms import UserCreationForm, UserChangeForm, forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'autofocus': True,'placeholder':('First Name'),'class':('f-c')})
        self.fields['last_name'].widget.attrs.update({'placeholder':('Last Name'),'class':('f-c')})
        self.fields['email'].widget.attrs.update({'placeholder':('Email'),'class':('f-c')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password'),'class':('f-c')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password'),'class':('f-c')})

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
