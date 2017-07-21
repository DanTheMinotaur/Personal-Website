from django import forms


# Contact form for home page
class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=60)
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label="Message")
