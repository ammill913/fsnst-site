from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=200)
    head_name = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    LEVEL_CHOICES = [
        ("bachelor", "Бакалавр"),
        ("master", "Магістр"),
        ("phd", "PhD"),
    ]

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="bachelor")
    description = models.TextField()
    coordinator_name = models.CharField(max_length=150)
    coordinator_contact = models.CharField(max_length=150)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    disciplines = models.TextField()

    class Meta:
        ordering = ["level", "code"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.position})"


class HomeContent(models.Model):
    title = models.CharField(
        max_length=200, default="Факультет соціальних наук та соціальних технологій"
    )
    about_text = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title


class ExchangeProgram(models.Model):
    university = models.CharField("Університет", max_length=200)
    country = models.CharField("Країна", max_length=100, default="")
    languages = models.CharField("Мови навчання", max_length=150)
    places = models.PositiveSmallIntegerField("Місця")
    deadline = models.DateField("Дедлайн")
    description = models.TextField("Опис")

    def __str__(self):
        return self.university

    @property
    def is_active(self):
        return self.deadline >= timezone.now().date()
