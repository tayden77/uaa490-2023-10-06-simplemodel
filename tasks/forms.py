from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # better practice: list fields explicitly rather than "__all__"
        fields = ['title', 'priority', 'description']
         
    def clean(self):
        super(TaskForm, self).clean()

        t = self.cleaned_data['title']
        p = self.cleaned_data['priority']

        if p >5 and len(t) < 10:
            self.errors['title'] = self.error_class([
                'Minimum 10 chars needed when priority > 5'
            ])
        return self.cleaned_data

class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']