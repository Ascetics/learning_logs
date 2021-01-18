from django import forms
from learning_logs.models import Topic, Entry


class TopicForm(forms.ModelForm):
    """主题表单"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """条目表单"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
