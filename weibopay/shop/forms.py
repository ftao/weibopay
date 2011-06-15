#coding=utf-8
from django import forms


class PostWeiboForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='消息')

