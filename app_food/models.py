from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Categories'  # Modelning ko'plikdagi ko'rinishi
        db_table = 'category'  # Yaratilgan jadvalning nomi


class Food(models.Model):
    food_name = models.CharField(max_length=100, verbose_name='Taom nomi', null=False, blank=False)
    food_recipe = models.TextField(verbose_name='Taomning retsepti', null=True, blank=True)
    food_preparation = models.TextField(verbose_name='Taomning tayyorlanishi', null=True, blank=True)
    food_image = models.ImageField(upload_to='media/foods_image/')
    food_price = models.FloatField(verbose_name='Narxi', null=False, blank=False)
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Taom turi", null=True)

    def __str__(self):
        return f"{self.pk} | {self.food_name}"

    class Meta:
        verbose_name_plural = 'Foods'  # Modelning ko'plikdagi ko'rinishi
        db_table = 'food'  # Yaratilgan jadvalning nomi
