from django import forms
from .models import Issue
from .models import Student, Book

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['book', 'student']


class ReturnForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Student")
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book")

    def __init__(self, *args, **kwargs):
        super(ReturnForm, self).__init__(*args, **kwargs)

        if 'student' in self.data:
            try:
                student_id = int(self.data.get('student'))
                self.fields['book'].queryset = Book.objects.filter(issue__student_id=student_id, issue__is_returned=False).distinct()
            except (ValueError, TypeError):
                pass  # invalid input — ignore and keep empty
