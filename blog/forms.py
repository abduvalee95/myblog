from django import forms
from .models import Post

choices = [('Новости', 'Новости'),('Спорт', 'Спорт'),('Игровой новости', 'Игровой новости'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title','title_tag','author', 'categry', 'body', 'img')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'титл'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'название'}),
            'author' : forms.Select(attrs={'class' : 'form-control','placeholder' : 'автор'}),
            'categry' : forms.Select(choices=choices,attrs={'class' : 'form-control','placeholder' : 'категории'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'напишити ваш '}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title','title_tag','body')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'титл'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'название'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control','placeholder' : 'автор'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'напишити ваш '}),
            
        }