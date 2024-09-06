# Generated by Django 5.0.7 on 2024-08-07 12:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_category_img_alter_category_is_available_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '1. Категория', 'verbose_name_plural': '1. Категории'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': '3. Событие', 'verbose_name_plural': '3. События'},
        ),
        migrations.AlterModelOptions(
            name='mappoint',
            options={'verbose_name': '5. Точка на карте', 'verbose_name_plural': '5. Точки на карте'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '2. Товар в меню', 'verbose_name_plural': '2. Товары в меню'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': '8. Уведомление', 'verbose_name_plural': '8. Уведомления'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': '4. Партнер', 'verbose_name_plural': '4. Партнеры'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '10. Профиль', 'verbose_name_plural': '10. Профили'},
        ),
        migrations.AlterModelOptions(
            name='refundrequest',
            options={'verbose_name': '7. Запрос на возврат', 'verbose_name_plural': '7.  Запросы на возврат'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': ' Отзыв', 'verbose_name_plural': ' Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': '9. Акция', 'verbose_name_plural': '9. Акции'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': '6. Транзакция', 'verbose_name_plural': '6. Транзакции'},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='system',
        ),
        migrations.RemoveField(
            model_name='refundrequest',
            name='status',
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(help_text='рекомендованное разрешение: 800x600', upload_to='cat_imgs/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='events',
            name='img',
            field=models.ImageField(help_text='Рекомендованное разрешение: 800x533', upload_to='events_imgs/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='events',
            name='tag',
            field=models.CharField(max_length=225, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='mappoint',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(help_text='Рекомендованное разрешение: 800x600', upload_to='product_imgs/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Доступно'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=225, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='img',
            field=models.ImageField(help_text='Рекомендованное разрешение: 100x100', upload_to='partner_imgs/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, default=1, upload_to='logos/', verbose_name='Логотип'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='refundrequest',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата запроса'),
        ),
        migrations.AlterField(
            model_name='refundrequest',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transaction', verbose_name='Транзакция'),
        ),
        migrations.AlterField(
            model_name='refundrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='review',
            name='subject',
            field=models.CharField(max_length=225, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='minimum_purchase_quantity',
            field=models.PositiveIntegerField(verbose_name='Минимальное количество для покупки'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена за единицу'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='remaining_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Оставшееся количество'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='total_quantity',
            field=models.PositiveIntegerField(verbose_name='Общее количество'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stock', verbose_name='Акция'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
