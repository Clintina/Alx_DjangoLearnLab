from django import forms
from .models import Book
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'Enter year'}),
        }

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and year < 0:
            raise forms.ValidationError("Year must be a positive number.")
        return year
