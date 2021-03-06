# Generated by Django 3.2.3 on 2021-05-28 06:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, validators=[django.core.validators.MinLengthValidator(50)], verbose_name='Цитата')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, verbose_name='почтовый адрес')),
                ('status', models.CharField(choices=[('moderate', 'модерированная'), ('new', 'новая')], default='новая', max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='RateArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)], verbose_name='Рейтинг')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_article', to='webapp.article', verbose_name='Статья')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_rate_article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'rate',
                'verbose_name_plural': 'rates',
                'db_table': 'rate_article',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.ManyToManyField(related_name='article_rate', to='webapp.RateArticle'),
        ),
    ]
