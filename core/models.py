from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, verbose_name="نام سایت")
    logo = models.ImageField(upload_to='logo/', verbose_name="لوگو")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    email = models.EmailField(verbose_name="ایمیل")
    address = models.TextField(verbose_name="آدرس")
    about_text = models.TextField(verbose_name="درباره ما")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.site_name