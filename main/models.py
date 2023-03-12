from django.db import models

class Articles(models.Model):
    brand = models.CharField('Марка', max_length=50)
    mode = models.CharField('Марка', max_length=50)
    year = models.IntegerField()
    dvig = models.CharField('Марка', max_length=50)
    mileage = models.IntegerField()
    rule = models.CharField('Марка', max_length=50)
    full_text = models.TextField('Инфо')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self().title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'







