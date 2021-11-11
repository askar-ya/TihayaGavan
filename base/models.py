from django.db import models


class Background(models.Model):
    """"Фон сайта"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')

    class Meta:
        db_table = 'Background'
        verbose_name = 'Задний фон'
        verbose_name_plural = 'Задний фон'


class Hot(models.Model):
    """"горячие блюда"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Hot'
        verbose_name = 'горячие блюда'
        verbose_name_plural = 'горячие блюда'


class Salad(models.Model):
    """"салаты"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Salad'
        verbose_name = 'салаты'
        verbose_name_plural = 'салаты'


class Snacks(models.Model):
    """"салаты"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'snacks'
        verbose_name = 'закуски'
        verbose_name_plural = 'закуски'


class Specially(models.Model):
    """"салаты"""
    image1 = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='картинка горизонтальная')

    image2 = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='картинка квадрат')

    image3 = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='картинка вертикальная')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Specially'
        verbose_name = 'Спец'
        verbose_name_plural = 'Спец'


class Bar(models.Model):
    """"салаты"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Bar'
        verbose_name = 'Бар'
        verbose_name_plural = 'Бар'


class Dessert(models.Model):
    """"салаты"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Dessert'
        verbose_name = 'десерт'
        verbose_name_plural = 'десерт'


class Phone(models.Model):
    """"телефон"""
    name = models.CharField('Название блюда', max_length=255)

    class Meta:
        db_table = 'Phone'
        verbose_name = 'телефон'
        verbose_name_plural = 'телефон'


class Interior(models.Model):
    """"интерьер"""
    text = models.TextField('текст')

    class Meta:
        db_table = 'Interior'
        verbose_name = 'интерьер'
        verbose_name_plural = 'интерьер'


class Place(models.Model):
    """"место"""
    text = models.TextField('текст')

    class Meta:
        db_table = 'Place'
        verbose_name = 'место'
        verbose_name_plural = 'место'


class Team(models.Model):
    """"команда"""
    text = models.TextField('текст')

    class Meta:
        db_table = 'Team'
        verbose_name = 'команда'
        verbose_name_plural = 'команда'


class Gallery(models.Model):
    """"салаты"""
    image = models.ImageField(blank=True, upload_to='images/',
                              verbose_name='ссылка картинки')
    text = models.TextField('текст')

    class Meta:
        db_table = 'Gallery'
        verbose_name = 'галерея'
        verbose_name_plural = 'галерея'
