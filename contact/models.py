from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"