from django.db import models
from django.utils.text import slugify

class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("Слаг", max_length=220, unique=True, blank=True)
    short_description = models.TextField("Короткое описание", blank=True)
    long_description = models.TextField("Полное описание", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    is_published = models.BooleanField("Публиковать", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        return super().save(*args, **kwargs)

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='places')
    position = models.PositiveIntegerField("Позиция", default=0)

    class Meta:
        ordering = ['position', 'id']
        verbose_name = "Фото места"
        verbose_name_plural = "Фото мест"

    def __str__(self):
        return f"{self.position} — {self.place.title}"
