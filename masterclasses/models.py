from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class MasterClass(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Новичок'),
        ('medium', 'Средний'),
        ('advanced', 'Продвинутый'),
    ]
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, verbose_name='Сложность')
    duration = models.IntegerField(help_text='минуты', verbose_name='Длительность')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    max_seats = models.PositiveIntegerField(verbose_name='Максимум мест')
    image = models.ImageField(upload_to='masterclasses/', verbose_name='Изображение')
    schedule = models.DateTimeField(verbose_name='Дата и время')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    @property
    def available_seats(self):
        booked = self.booking_set.filter(status='paid').count()
        return self.max_seats - booked

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер-класс'
        verbose_name_plural = 'Мастер-классы'

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает оплаты'),
        ('paid', 'Оплачено'),
        ('cancelled', 'Отменено'),
        ('completed', 'Проведено'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    masterclass = models.ForeignKey(MasterClass, on_delete=models.CASCADE, verbose_name='Мастер-класс')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата бронирования')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.user.username} - {self.masterclass.title}'