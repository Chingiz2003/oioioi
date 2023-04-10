from django.db import models


class Mark(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Марки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class MarkModel(models.Model):
    mark = models.ForeignKey(Mark, verbose_name="Марка", on_delete=models.CASCADE)

    name = models.CharField("Модель", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Engine(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип двигателя')

    class Meta:
        verbose_name = ("Двигатель")
        verbose_name_plural = ("Двигатели")

    def __str__(self):
        return self.title

class Rudder(models.Model):
    title = models.CharField(max_length=50, verbose_name='Расположение руля')

    class Meta:
        verbose_name = ("Руль")
        verbose_name_plural = ("Рули")

    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Наименование категории')

    
    def __str__(self):
        return self.title
  
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ads(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')
    marks = models.ForeignKey(Mark, on_delete=models.PROTECT, null=True, verbose_name='Марки')
    # mode = models.CharField('Модель', max_length=50)
    mark_model = models.ForeignKey(MarkModel, on_delete=models.CASCADE,  null=True, verbose_name='Модели')
    year = models.IntegerField(verbose_name='Год')
    #dvig = models.CharField('Тип двигателя', max_length=50)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, null=True, verbose_name='Двигатели')
    mileage = models.IntegerField(verbose_name='Пробег')
    # rule = models.CharField('Расположение руля', max_length=50)
    rudder = models.ForeignKey(Rudder, on_delete=models.CASCADE, null=True, verbose_name='Рули')
    full_text = models.TextField('Инфо')
    created_ad = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_ad = models.DateTimeField('Дата обвновления', auto_now=True )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    price = models.IntegerField(verbose_name='Цена', null=True)
    


    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'









