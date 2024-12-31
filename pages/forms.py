from django import forms
from .models import CommentAnonymous, CommentAuthenticated, Articles, Subjects, GalleryArticles




class CommentAnonymousForm(forms.Form):
    name = forms.CharField(label='Имя автора', widget=forms.TextInput(attrs={
        'class': 'form-control custom-form',
        'placeholder': 'Введите имя автора'
    }))
    content = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={
        'class': 'form-control custom-form',
        'placeholder': 'Введите комментарий',
        'rows': 4,
        'cols': 65
    }))

class CommentAuthenticatedForm(forms.ModelForm):
    class Meta:
        model = CommentAuthenticated
        fields = ['content']
        labels = {
            'content': 'Комментарий',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control custom-form',
                'placeholder': 'Введите комментарий',
                'rows': 4,
                'cols': 65
            }),
        }


class EditArticleForm(forms.ModelForm):
    subject_article = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Тематика статьи'
    )

    class Meta:
        model = Articles
        fields = [
            'title',
            'description',
            'card_description',
            'category',
            'timing_article',
            'subject_article'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'card_description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'timing_article': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'card_description': 'Короткое описание',
            'category': 'Категория',
            'timing_article': 'Хронометраж статьи'
        }


class CreateArticleForm(forms.ModelForm):
    image = forms.FileField(required=False, label='Изображения статьи')

    subject_article = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Тематика статьи'
    )

    class Meta:
        model = Articles
        fields = [
            'title',
            'description',
            'card_description',
            'category',
            'timing_article',
            'subject_article',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'card_description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'timing_article': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'card_description': 'Короткое описание',
            'category': 'Категория',
            'timing_article': 'Хронометраж статьи'
        }

