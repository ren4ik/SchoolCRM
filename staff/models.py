from django.db import models


class Employee(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50)
    date_birth = models.DateField("Дата рождения", editable=True)
    img = models.ImageField("Фото", upload_to="media/employee/", default="")

    def admin_image(self):

        if self.img:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.img.url}" target="_blank"><img src="{self.img.url}" width="80" /></a>'
            )
        else:
            return 'Фото нет'

    admin_image.short_description = 'Фото'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.last_name} {self.first_name.upper()[:1]}. {self.father_name.upper()[:1]}'


# class TimeTracking(models.Model):
#     pass
#
#
# class TimeGrid(models.Model):
#     pass


