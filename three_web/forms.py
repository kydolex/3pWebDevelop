from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())


class Infomation_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())


class Sample_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)