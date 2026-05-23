from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

class Idea(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    cover_image = models.ImageField(upload_to='ideas/', blank=True, verbose_name='Обложка')
    tags = TaggableManager(verbose_name='Теги')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
        ordering = ['-created_at']

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, verbose_name='Идея')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        