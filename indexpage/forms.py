from django import forms
from .models import Division, Profession, Worker

class DivisionCreateForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']
        labels = {
            'name': ('Наименование'),
        }

class ProfessionCreateForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['name']
        labels = {
            'name': ('Наименование'),
        }

class WorkerCreateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['division', 'profession', 'firstname', 'secondname', 'salary']
        labels = {
            'firstname': ('Имя'),
            'secondname': ('Фамилия'),
            'division': ('Подразделение'),
            'profession': ('Профессия'),
            'salary': ('Оклад'),
        }

