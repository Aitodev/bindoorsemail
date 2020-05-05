from django import forms
from .models import Recall, SendCatalog, SendCatandprice, Quiz, Subscribe


class RecallForm(forms.ModelForm):
    class Meta:
        model = Recall
        fields = ['name', 'phone']


class SendCatalogForm(forms.ModelForm):
    class Meta:
        model = SendCatalog
        fields = ['mail', ]


class SendCatandpriceForm(forms.ModelForm):
    class Meta:
        model = SendCatandprice
        fields = ['name', 'phone', 'mail']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['door_type', 'price_type', 'style_type', 'size_type', 'material_type', 'name', 'phone', 'mail']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['mail', ]
