from django import forms
from .models import Feedback  # Import the new Feedback model

class FeedBackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'name', 'feedback']
        labels = {
            'email': 'Enter your Email',
            'name': 'Enter your Name',
            'feedback': 'Your Feedback'
        }
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super(FeedBackForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'