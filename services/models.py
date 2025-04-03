from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان خدمت")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='services/', verbose_name="تصویر")
    icon = models.CharField(max_length=50, verbose_name="آیکون", help_text="نام کلاس FontAwesome", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"
        ordering = ['order']

    def __str__(self):
        return self.title