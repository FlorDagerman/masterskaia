import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Product

products = [
    # ========== КИСТИ ==========
    {
        'name': 'Кисть синтетика №0, круглая',
        'sku': 'BR-000',
        'description': 'Тонкая кисть для деталей и миниатюры. Упругий ворс, хороший набор краски.',
        'price': 90,
        'stock': 25,
        'is_available': True,
        'image': 'products/кисть1.jpg',
    },
    {
        'name': 'Кисть синтетика №6, круглая',
        'sku': 'BR-006',
        'description': 'Универсальная кисть для акрила, акварели, гуаши. Держит форму, не линяет.',
        'price': 150,
        'stock': 30,
        'is_available': True,
        'image': 'products/кисть2.jpg',
    },
    {
        'name': 'Кисть щетина плоская №12',
        'sku': 'BR-012',
        'description': 'Для масляной живописи и акрила. Жёсткая щетина, создаёт фактурные мазки.',
        'price': 210,
        'stock': 20,
        'is_available': True,
        'image': 'products/кисть3.jpg',
    },
    {
        'name': 'Набор кистей (6 шт.)',
        'sku': 'SET-BR6',
        'description': 'Синтетические кисти разных форм: круглая, плоская, веерная, скошенная.',
        'price': 590,
        'stock': 12,
        'is_available': True,
        'image': 'products/кисти.jpg',
    },

    # ========== КРАСКИ ==========
    {
        'name': 'Акварель “Невская палитра” 24 цвета',
        'sku': 'AQU-24',
        'description': 'Профессиональная акварель, высокая светостойкость, кюветы 2,5 мл.',
        'price': 1200,
        'stock': 10,
        'is_available': True,
        'image': 'products/Краски.jpg',
    },
    {
        'name': 'Акрил “Ладога” 12 цветов по 20 мл',
        'sku': 'ACR-12',
        'description': 'Плотная укрывистая краска для холста, дерева, керамики. Можно смешивать.',
        'price': 850,
        'stock': 15,
        'is_available': True,
        'image': 'products/акрил.jpg',
    },
    {
        'name': 'Гуашь “Гамма” 16 цветов',
        'sku': 'GUA-16',
        'description': 'Яркая, укрывистая, хорошо ложится на бумагу и картон. Подходит для детей.',
        'price': 420,
        'stock': 20,
        'is_available': True,
        'image': 'products/гуашь.jpg',
    },
    {
        'name': 'Масло “Мастер-класс” набор 8 цветов x 46 мл',
        'sku': 'OIL-8',
        'description': 'Художественное масло на льняном масле, насыщенные пигменты.',
        'price': 2200,
        'stock': 8,
        'is_available': True,
        'image': 'products/масло.jpg',
    },

    # ========== ГЛИНА И ПЛАСТИКА ==========
    {
        'name': 'Глина самоотвердевающая белая, 1 кг',
        'sku': 'CLAY-W1',
        'description': 'Лёгкая, не требует обжига, застывает за 24 часа.',
        'price': 400,
        'stock': 20,
        'is_available': True,
        'image': 'products/белый.jpg',
    },
    {
        'name': 'Глина самоотвердевающая терракотовая, 1 кг',
        'sku': 'CLAY-T1',
        'description': 'Терракотовый цвет, приятная текстура.',
        'price': 420,
        'stock': 15,
        'is_available': True,
        'image': 'products/глина.jpg',
    },
    {
        'name': 'Полимерная глина Sculpey Original, белая, 340 г',
        'sku': 'POL-SC1',
        'description': 'Американская полимерная глина, запекаемая. После запекания становится прочной.',
        'price': 1250,
        'stock': 10,
        'is_available': True,
        'image': 'products/полимер.jpg',
    },
    {
        'name': 'Полимерная глина FIMO Soft, набор 6 цветов',
        'sku': 'POL-F6',
        'description': 'Мягкая, легко смешивается, не крошится. Набор базовых цветов.',
        'price': 1800,
        'stock': 8,
        'is_available': True,
        'image': 'products/полимер2.jpg',
    },

    # ========== ХОЛСТЫ И ОСНОВЫ ==========
    {
        'name': 'Холст на подрамнике 30×40 см, хлопок',
        'sku': 'CAN-3040',
        'description': 'Грунтованный хлопковый холст, средняя зернистость.',
        'price': 350,
        'stock': 12,
        'is_available': True,
        'image': 'products/холст1.jpg',
    },
    {
        'name': 'Холст на подрамнике 40×50 см, лён',
        'sku': 'CAN-4050',
        'description': 'Льняной холст, мелкое зерно, двойной грунт.',
        'price': 680,
        'stock': 8,
        'is_available': True,
        'image': 'products/холст2.jpg',
    },
    {
        'name': 'Холст на картоне 20×30 см, 3 шт.',
        'sku': 'CAN-2030',
        'description': 'Эскизный вариант. Удобно для этюдов.',
        'price': 190,
        'stock': 25,
        'is_available': True,
        'image': 'products/холст3.jpg',
    },

    # ========== ДЕКОР / ИНСТРУМЕНТЫ ==========
    {
        'name': 'Палитра пластиковая овальная (10 ячеек)',
        'sku': 'PAL-OV',
        'description': 'Лёгкая, легко моется. Есть центральное углубление для смешивания.',
        'price': 90,
        'stock': 30,
        'is_available': True,
        'image': 'products/что-то.jpg',
    },
    {
        'name': 'Клей “Момент Кристалл” 30 мл',
        'sku': 'GLUE-30',
        'description': 'Прозрачный, эластичный, склеивает стекло, керамику, пластик, дерево.',
        'price': 120,
        'stock': 50,
        'is_available': True,
        'image': 'products/клей.jpg',
    },
    {
        'name': 'Мастихин для масла (стальной)',
        'sku': 'MST-01',
        'description': 'Изогнутый стальной мастихин для смешивания красок и создания фактуры.',
        'price': 250,
        'stock': 10,
        'is_available': True,
        'image': 'products/мастихин.jpg',
    },
    {
        'name': 'Набор стеков для лепки (6 шт.)',
        'sku': 'STK-6',
        'description': 'Деревянные и пластиковые стеки для работы с глиной и пластикой.',
        'price': 160,
        'stock': 20,
        'is_available': True,
        'image': 'products/набор1.jpg',
    },
    {
        'name': 'Лак для акрила глянцевый, 100 мл',
        'sku': 'LAC-100',
        'description': 'Защищает поверхность, придаёт глянец. Не желтеет.',
        'price': 180,
        'stock': 15,
        'is_available': True,
        'image': 'products/лак.jpg',
    },
]

def run():
    count_new = 0
    count_update = 0
    for data in products:
        defaults = {
            'name': data['name'],
            'description': data['description'],
            'price': Decimal(str(data['price'])),
            'stock': data['stock'],
            'is_available': data['is_available'],
        }
        if 'image' in data and data['image']:
            defaults['image'] = data['image']
        
        obj, created = Product.objects.update_or_create(
            sku=data['sku'],
            defaults=defaults
        )
        if created:
            print(f"✅ Добавлен товар: {obj.name} (арт. {obj.sku})")
            count_new += 1
        else:
            print(f"🔄 Обновлён товар: {obj.name}")
            count_update += 1
    print(f"\n🎉 Результат: добавлено {count_new}, обновлено {count_update} товаров.")
    print(f"📦 Всего товаров в базе: {Product.objects.count()}")

if __name__ == '__main__':
    run()