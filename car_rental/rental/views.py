from django.shortcuts import render, redirect

from .forms import CarFilterForm
from .models import Car, Contact, Review

from .forms import ContactForm


def about(request):
    return render(request, 'rental/about.html')

def services(request):
    return render(request, 'rental/services.html')

def cars(request):
    cars = Car.objects.all()
    return render(request, 'rental/cars.html', {'cars': cars})

def client(request):
    return render(request, 'rental/clients.html')

def contact(request):
    success = False

    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone Number')
        message = request.POST.get('Message')

        # Сохранение данных в базу
        Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            message=message
        )

        # Установить флаг успеха и выполнить редирект
        return redirect('contact_sent')  # Замените 'index' на имя вашего URL для главной страницы
    return render(request, 'rental/contact.html', {'success': success})

def contact_sent(request):
    return render(request, 'rental/contact_sent.html')

def index(request):
    cars = Car.objects.all()
    success = False

    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone Number')
        message = request.POST.get('Message')

        # Сохранение данных в базу
        Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            message=message
        )

        # Установить флаг успеха и выполнить редирект
        return redirect('contact_sent')  # Замените 'index' на имя вашего URL для главной страницы

    return render(request, 'rental/index.html', {'cars': cars, 'success': success})


def car_list(request):
    # Сначала получаем все автомобили
    cars = Car.objects.all()

    # Создаем экземпляр формы с данными из GET-запроса
    form = CarFilterForm(request.GET)

    # Проверяем, если форма валидна, то фильтруем по выбранным параметрам
    if form.is_valid():
        brand = form.cleaned_data.get('brand')
        body_type = form.cleaned_data.get('body_type')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        # Фильтруем по бренду
        if brand:
            cars = cars.filter(brand=brand)

        # Фильтруем по типу кузова
        if body_type:
            cars = cars.filter(body_type=body_type)

        # Фильтруем по минимальной цене
        if price_min is not None:
            cars = cars.filter(price_per_day__gte=price_min)

        # Фильтруем по максимальной цене
        if price_max is not None:
            cars = cars.filter(price_per_day__lte=price_max)

    if request.is_ajax():
        return render(request, 'rental/partials/car_list.html', {'cars': cars})

    return render(request, 'rental/index.html', {'cars': cars, 'form': form})

def clients(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        message = request.POST.get('Message')

        # Сохраняем новый отзыв в базе данных
        Review.objects.create(name=name, message=message)

        # Перенаправляем на страницу с отзывами
        return redirect('clients')  # Замените на имя вашего URL для страницы отзывов

    reviews = Review.objects.all().order_by('-created_at')  # Получаем все отзывы, сортируя по дате
    return render(request, 'rental/clients.html', {'reviews': reviews})

