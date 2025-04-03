from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات")
    completion_date = models.DateField(verbose_name="تاریخ تکمیل")
    client = models.CharField(max_length=200, verbose_name="نام کارفرما")
    location = models.CharField(max_length=200, verbose_name="محل پروژه")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-completion_date']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="پروژه")
    image = models.ImageField(upload_to='projects/', verbose_name="تصویر")
    is_main = models.BooleanField(default=False, verbose_name="تصویر اصلی")

    class Meta:
        verbose_name = "تصویر پروژه"
        verbose_name_plural = "تصاویر پروژه"

    def __str__(self):
        return f"تصویر {self.id} از {self.project.title}"