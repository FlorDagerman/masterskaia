from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    sku = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(default=0, verbose_name='Остаток')
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Изображение')
    is_available = models.BooleanField(default=True, verbose_name='Доступен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Итого')
    delivery_address = models.TextField(verbose_name='Адрес доставки')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    status = models.CharField(max_length=20, default='new', choices=[
        ('new', 'Новый'),
        ('paid', 'Оплачен'),
        ('shipped', 'Отправлен'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    ], verbose_name='Статус')

    def __str__(self):
        return f'Заказ №{self.id} от {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена на момент покупки')

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'