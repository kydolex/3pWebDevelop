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


class List_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)

class request_text_Form(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)


class UserForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)



class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)