from django.db import models
from django.conf import settings


# Create your models here.

class Project(models.Model):
    object = models.CharField(verbose_name='Объект', max_length=200)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    date = models.CharField(verbose_name='Дата монтажа', max_length=200)
    task = models.CharField(verbose_name='Задача', max_length=200)
    jobs = models.CharField(verbose_name='Выполненые работы', max_length=200)
    price = models.CharField(verbose_name='Общая стоимость проекта', max_length=200)
    thumb1 = models.ImageField(verbose_name='Миниатюра 1 (334x500)', upload_to='static/img/project_img/')
    thumb2 = models.ImageField(verbose_name='Миниатюра 2 (334x500)', upload_to='static/img/project_img/')
    thumb3 = models.ImageField(verbose_name='Миниатюра 3 (334x500)', upload_to='static/img/project_img/')
    thumb4 = models.ImageField(verbose_name='Миниатюра 4 (1000x500)', upload_to='static/img/project_img/')
    thumb5 = models.ImageField(verbose_name='Миниатюра 5 (500x1000)', upload_to='static/img/project_img/')
    thumb6 = models.ImageField(verbose_name='Миниатюра 6 (500x1000)', upload_to='static/img/project_img/')
    img1 = models.ImageField(verbose_name='Изображение 1', upload_to='static/img/project_img')
    img2 = models.ImageField(verbose_name='Изображение 2', upload_to='static/img/project_img')
    img3 = models.ImageField(verbose_name='Изображение 3', upload_to='static/img/project_img')
    img4 = models.ImageField(verbose_name='Изображение 4', upload_to='static/img/project_img')
    img5 = models.ImageField(verbose_name='Изображение 5', upload_to='static/img/project_img')
    img6 = models.ImageField(verbose_name='Изображение 6', upload_to='static/img/project_img')

    def __str__(self):
        return self.object

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Partner(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    img = models.ImageField(verbose_name='Изображение', upload_to='static/img/partner_img/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    city = models.CharField(verbose_name='Город', max_length=200)
    img = models.ImageField(verbose_name='Фотография', upload_to='static/img/review_img/')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Recall(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=10)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'


class SendCatalog(models.Model):
    mail = models.CharField(verbose_name='Почта', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Заявка на каталог'
        verbose_name_plural = 'Заявки на каталог'


class SendCatandprice(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=200)
    mail = models.CharField(verbose_name='Почта', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на котолог и прайс'
        verbose_name_plural = 'Заявки на каталог и прайс'


class Quiz(models.Model):
    door_type = models.CharField(verbose_name='Тип двери', max_length=200)
    price_type = models.CharField(verbose_name='Ценовой сегмент', max_length=200)
    style_type = models.CharField(verbose_name='Стиль', max_length=200)
    size_type = models.CharField(verbose_name='Размер', max_length=200)
    material_type = models.CharField(verbose_name='Материал', max_length=200)
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=200)
    mail = models.CharField(verbose_name='Почта', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка с квиза'
        verbose_name_plural = 'Заявки с квиза'


class Subscribe(models.Model):
    mail = models.CharField(verbose_name='Почта', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Заявка на подписку'
        verbose_name_plural = 'Заявки на подписку'


