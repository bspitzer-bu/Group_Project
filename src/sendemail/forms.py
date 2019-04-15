from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(required = True)
    subject = forms.CharField(required = True)
    message = forms.CharField(required = True, widget = forms.Textarea)

    sender.widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
    subject.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
    message.widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})
