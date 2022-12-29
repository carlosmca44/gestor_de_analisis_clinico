from django import forms
from .models import User, Pacient, AnalysisRequest, Results
from django.contrib.auth.forms import UserCreationForm


class userCreationForm(UserCreationForm):

    CATEGORIES = [('1', 'Doctor'), ('2', 'Laboratoristas'),
                  ('3', 'Bioquimico')]

    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        label='Rol', widget=forms.Select(attrs={'class': 'form-select'}), choices=CATEGORIES)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2', 'category']
        help_texts = {k: '' for k in fields}
        labels = {'first_name': 'Nombre/s',
                  'last_name': 'Apellido/s', 'username': 'Nombre de usuario'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class newPacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['name', 'last_name', 'ci',
                  'age', 'sex', 'sicks', 'diagnosis']


class newClinicalAnalysisForm(forms.ModelForm):

    CATEGORIES = [('Sangre', 'Sangre'), ('Orina', 'Orina'),
                  ('ADN', 'ADN')]

    kind = forms.ChoiceField(
        label='Tipo', widget=forms.Select(attrs={'class': 'form-select'}), choices=CATEGORIES)

    class Meta:
        model = AnalysisRequest
        fields = ['pacient', 'kind']


class ResultsForm(forms.ModelForm):

    class Meta:
        model = Results
        fields = ['idanalysis', 'info']
