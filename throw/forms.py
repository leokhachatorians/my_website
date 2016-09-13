from django import forms

class TweetForm(forms.Form):
    screen_name = forms.CharField(
            required=True,
            widget = forms.HiddenInput(attrs=
                {'id': 'modal-screen-name-value'}))

    tweet_reply_text = forms.CharField(
            label='Reply', max_length=138,
            widget=forms.Textarea(attrs=
                {'id': 'modal-reply-text',
                 'rows': 4,
                 'cols': 55,
                }))
