from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label="Comment")

