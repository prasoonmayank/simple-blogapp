from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255)
    subtitle = forms.CharField(max_length=255)
    description = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField()
