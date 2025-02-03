from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EducationalMaterial


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EducationalMaterialForm(forms.ModelForm):
    class Meta:
        model = EducationalMaterial
        fields = ('title', 'summary', 'material_file', 'subject')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.material_file:
            instance.material_file.name = f"material_{instance.title}_{instance.material_file.name}"
        if commit:
            instance.save()
        return instance
