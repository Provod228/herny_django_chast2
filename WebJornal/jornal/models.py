from django.db import models


class Subject(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Введите название предмет",
        verbose_name="Название предмет",
        unique=True,
        null=False,
    )

    def __str__(self):
        return self.title


class EducationalMaterial(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Введите название предмет",
        verbose_name="Название предмет",
        null=False,
    )
    summary = models.TextField(
        max_length=1000,
        help_text='Введите краткое описание учебного материала',
        verbose_name='Учебный материал',
        null=False,
    )
    material_file = models.FileField(
        help_text='Загрузите файл с учебным материалом',
        verbose_name='Файл с учебным материалом',
        null=False,
        upload_to='material_files'
    )
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE,
        help_text='Выберите учебны предмет',
        verbose_name='Учебны предмет', null=True,
    )

    def __str__(self):
        return self.title
