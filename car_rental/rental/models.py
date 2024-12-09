from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    body_type = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return self.brand

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.car} by {self.customer_name}"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания

    def __str__(self):
        return f"Contact from {self.name}"

class Review(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.name}"