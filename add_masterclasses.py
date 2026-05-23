import os
import django
from datetime import datetime
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.utils import timezone
from masterclasses.models import Category, MasterClass

def run():
    # --- Категории ---
    categories = [
        {'name': 'Живопись и графика', 'slug': 'zhivopis'},
        {'name': 'Лепка и керамика', 'slug': 'lepka'},
        {'name': 'Скрапбукинг', 'slug': 'skrapbuking'},
        {'name': 'Текстиль и шитьё', 'slug': 'tekstil'},
    ]
    for cat in categories:
        obj, created = Category.objects.get_or_create(slug=cat['slug'], defaults={'name': cat['name']})
        print(f'{"Создана" if created else "Уже есть"} категория: {obj.name}')

    # --- Мастер-классы 
    masterclasses = [
        {
            'title': 'Акварельные рассветы',
            'description': 'Изучение базовых акварельных техник: заливка, лессировка, градиент. Рисуем нежный рассвет над водой.',
            'category_slug': 'zhivopis',
            'difficulty': 'beginner',
            'duration': 120,
            'price': 1200,
            'max_seats': 8,
            'schedule': datetime(2026, 6, 15, 10, 0),
            'image': 'masterclasses/aqva.jpg',
        },
        {
            'title': 'Масляная фактура: импрессионизм',
            'description': 'Работа мастихином, создание объёмных мазков. Пишем копию картины Моне «Водяные лилии».',
            'category_slug': 'zhivopis',
            'difficulty': 'advanced',
            'duration': 180,
            'price': 2000,
            'max_seats': 6,
            'schedule': datetime(2026, 6, 20, 14, 0),
            'image': 'masterclasses/масло.jpg',
        },
        {
            'title': 'Гончарный круг: первая чашка',
            'description': 'Центрирование глины, формирование простой чаши, декорирование ангобами. Обжиг и глазурь входят в стоимость.',
            'category_slug': 'lepka',
            'difficulty': 'beginner',
            'duration': 150,
            'price': 1800,
            'max_seats': 4,
            'schedule': datetime(2026, 6, 18, 11, 0),
            'image': 'masterclasses/гончарка.jpg',
        },
        {
            'title': 'Полимерная глина: миниатюрные тортики',
            'description': 'Лепка реалистичных миниатюр десертов для кукол, брелоков или магнитов. Роспись акрилом.',
            'category_slug': 'lepka',
            'difficulty': 'beginner',
            'duration': 90,
            'price': 1000,
            'max_seats': 10,
            'schedule': datetime(2026, 6, 22, 16, 0),
            'image': 'masterclasses/Mushroom people figurine.jpg',
        },
        {
            'title': 'Альбом для путешествий',
            'description': 'Создание крафтового альбома в технике «тревел-бук» с кармашками, тегами и конвертами для билетов.',
            'category_slug': 'skrapbuking',
            'difficulty': 'medium',
            'duration': 180,
            'price': 1600,
            'max_seats': 6,
            'schedule': datetime(2026, 7, 1, 12, 0),
            'image': 'masterclasses/travel memories.jpg',
        },
        {
            'title': 'Тёплая игрушка: заяц тильда',
            'description': 'Шитьё интерьерной куклы по выкройке, набивка, ручная вышивка мордочки, подбор одежды.',
            'category_slug': 'tekstil',
            'difficulty': 'beginner',
            'duration': 120,
            'price': 1300,
            'max_seats': 8,
            'schedule': datetime(2026, 6, 25, 15, 0),
            'image': 'masterclasses/игрушка.jpg',
        },
        {
            'title': 'Эко-панно из сухоцветов',
            'description': 'Композиция из засушенных цветов, злаков и веток на деревянной основе под стекло.',
            'category_slug': 'tekstil',
            'difficulty': 'beginner',
            'duration': 90,
            'price': 1300,
            'max_seats': 8,
            'schedule': datetime(2026, 6, 28, 12, 0),
            'image': 'masterclasses/эко.jpg',
        },
    ]

    for mc in masterclasses:
        try:
            cat = Category.objects.get(slug=mc['category_slug'])
        except Category.DoesNotExist:
            print(f'⚠️ Категория {mc["category_slug"]} не найдена, пропускаем {mc["title"]}')
            continue

        schedule_aware = timezone.make_aware(mc['schedule'])

        defaults = {
            'description': mc['description'],
            'category': cat,
            'difficulty': mc['difficulty'],
            'duration': mc['duration'],
            'price': Decimal(str(mc['price'])),
            'max_seats': mc['max_seats'],
            'schedule': schedule_aware,
            'is_active': True,
        }
        if 'image' in mc:
            defaults['image'] = mc['image']

        obj, created = MasterClass.objects.update_or_create(
            title=mc['title'],
            defaults=defaults
        )
        print(f'{"Создан" if created else "Обновлён"} мастер-класс: {obj.title} (изображение: {obj.image})')

if __name__ == '__main__':
    run()