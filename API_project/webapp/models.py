from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
status_choice = [('moderate', 'модерированная'), ('new', 'новая')]
# Create your models here.
class Article(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Цитата', validators=(MinLengthValidator(50),))
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name='почтовый адрес')
    rating = models.ManyToManyField('webapp.RateArticle', related_name='article_rate')
    status = models.CharField(max_length=50, null=False, choices=status_choice,  blank=False, default='новая')
    data = models.DateTimeField(auto_now_add=True, verbose_name='время добавления')


    class Meta:
        db_table = 'article'
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
class RateArticle(models.Model):
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='rate_article',
                                verbose_name='Статья', null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='user_rate_article')
    rate = models.IntegerField(blank=False, null=False, verbose_name='Рейтинг', validators=[MinValueValidator(-1), MaxValueValidator(1)])
    class Meta:
        db_table = 'rate_article'
        verbose_name = 'rate'
        verbose_name_plural = 'rates'

    def __str__(self):
        return f'{self.article}: {self.user}'


# class DeRateArticle(models.Model):
#     article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='like_article',
#                                 verbose_name='Статья', null=False, blank=False)
#     user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='user_rate_article')
#
#     class Meta:
#         db_table = 'rate_article'
#         verbose_name = 'rate'
#         verbose_name_plural = 'rates'
#
#     def __str__(self):
#         return f'{self.article}: {self.user}'
















