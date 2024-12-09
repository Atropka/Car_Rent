from django import forms
from .models import Car
from .models import Contact

class CarFilterForm(forms.Form):
    # Получаем уникальные значения для фильтрации
    brand_choices = [(car['brand'], car['brand']) for car in Car.objects.all().values('brand').distinct()]
    body_type_choices = [(car['body_type'], car['body_type']) for car in Car.objects.all().values('body_type').distinct()]

    # Поля фильтрации
    brand = forms.ChoiceField(choices=[('', 'Все бренды')] + brand_choices, required=False)
    body_type = forms.ChoiceField(choices=[('', 'Все типы')] + body_type_choices, required=False)
    price_min = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Минимальная цена")
    price_max = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Максимальная цена")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']