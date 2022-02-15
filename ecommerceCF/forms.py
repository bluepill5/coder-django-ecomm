import email
from django import forms

# from django.contrib.auth.models import User
from users.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, 
                               min_length=4, 
                               max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'placeholder': 'Username'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                     'class': 'form-control',
                                     'id': 'email',
                                     'placeholder': 'example@gmail.com '
                                     }
                             ))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': '*********'
                               }))
    password2 = forms.CharField(required=True,
                               label='Confirmar password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': '*********'
                               }))

    def clean_username(self):
        ''' Para implmentar una validación en el username '''
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya existe')
        
        return username

    def clean_email(self):
        ''' Para implmentar una validación en el email '''
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya existe')
        
        return email

    # Utilizamos el método clean si queremos validar campos 
    # que dependen entre si
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')
    
    def save(self):
        ''' Para delegar el guardar los usuarios al formulario '''
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
