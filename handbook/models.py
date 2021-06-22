from django.db import models
from pytils.translit import slugify
from django.urls import reverse


class Direction(models.Model):
    """направления/отделы"""
    title = models.CharField("Наименование", max_length=50, default="school")
    is_multidirectional = models.BooleanField("Несколько направлений", default=False)
    is_active = models.BooleanField("Да/Нет", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('direction-detail', kwargs={'slug': slugify(self.title)})


class Branch(models.Model):
    """Филиалы"""
    name = models.CharField(verbose_name="имя филиала", max_length=100, unique=True)
    short_name = models.CharField(verbose_name="короткое название", max_length=20, default="Rx")
    slug = models.SlugField(verbose_name="url", max_length=100, blank=True, unique=True)
    photo = models.ImageField(verbose_name="фото", upload_to="branch/", default="", blank=True)
    is_active = models.BooleanField(verbose_name="открыт", default=False)
    multidirectional = models.ForeignKey(Direction, verbose_name="Направление", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = slugify(name)
        super(Branch, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('branch-detail', kwargs={'slug': self.slug})


class GroupNumAlpha(models.Model):
    name = models.CharField("Наименование группы", max_length=20, unique=True)
    num = models.PositiveSmallIntegerField("Номер группы")
    alpha = models.CharField("Литера группы", max_length=3)

    def save(self, *args, **kwargs):
        self.name = f'{self.num}{self.alpha}'
        super(GroupNumAlpha, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group-info-detail', kwargs={'slug': self.name})


class Group(models.Model):
    group = models.ForeignKey(GroupNumAlpha, verbose_name="Наименование группы", on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, verbose_name="Филиал", on_delete=models.PROTECT)
    group_code = models.CharField("Код группы", max_length=10)
    is_active = models.BooleanField("Да/Нет", default=False)

    def save(self, *args, **kwargs):
        self.group_code = f'{self.branch}{self.group}'
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.group_code

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'slug': self.group_code})


class CategoryPosition(models.Model):
    title = models.CharField("Категория должности", max_length=100)
    is_active = models.BooleanField("Да/Нет", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-position-detail', kwargs={'slug': slugify(self.title)})


class Position(models.Model):
    category = models.ForeignKey(CategoryPosition, verbose_name="Категория", on_delete=models.PROTECT)
    title = models.CharField("Должность", max_length=50)
    is_active = models.BooleanField("Да/Нет", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('position-detail', kwargs={'slug': slugify(self.title)})


class Day(models.Model):
    """список дней недели"""
    pass


class Schedule(models.Model):
    """связь времени и номера урока"""
    pass


class Subject(models.Model):
    """список предметов"""
    pass




