from django import forms
from .tasks import parse_article_task


class ArticleTask(forms.Form):
    email = forms.URLField(label="Url")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(ArticleTask, self).__init__(*args, **kwargs)

    def send_email(self):
        # try to trick spammers by checking whether the honeypot field is
        # filled in; not super complicated/effective but it works
        if self.cleaned_data['honeypot']:
            return False
        parse_article_task.delay(
            self.cleaned_data['email'], self.cleaned_data['message'])