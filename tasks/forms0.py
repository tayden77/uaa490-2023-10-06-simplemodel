from django import forms
from .models import Task

class TaskNameForm(forms.Form):
    task = forms.CharField(label="Task to delete")

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task", min_length=5)
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10, initial=5)

    def clean(self):
        #WRONG: super(NewTaskForm, self.clean())
        super(NewTaskForm, self).clean()

        t = self.cleaned_data['task']
        p = self.cleaned_data['priority']

        if p >5 and len(t) < 10:
            self.errors['task'] = self.error_class([
                'Minimum 10 chars needed when priorty > 5'
            ])
        return self.cleaned_data
