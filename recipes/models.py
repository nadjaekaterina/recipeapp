from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 

#Category Dropdown
CATEGORY_CHOICES = (
    ('salads','SALADS'),
    ('soups', 'SOUPS'),
    ('dough','DOUGH'),
    ('pasta','PASTA'),
    ('rice','RICE'),
    ('meats','MEATS'),
    ('fish','FISH'),
    ('spreads','SPREADS'),
    ('sweets','SWEETS'),
)

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Add your category here')
    ingredients = RichTextField(default='Add your ingredients here')
    description = RichTextField(default='Add your description here')
    picture = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title