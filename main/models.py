from django.db import models

# Create your models here.





class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    cost = models.FloatField(verbose_name="Цена")
    available_ammount = models.IntegerField(verbose_name="Есть в наличии")
    volume_type = models.ForeignKey("VolumeType", on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to="products", null=True)


    def __str__(self):
        return f"{self.name} - {self.description}"


class VolumeType(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип объема")

    def __str__(self):
        return f"{self.name}"



class Comment(models.Model):
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Коммент")
    img = models.ImageField(verbose_name="Картинка", null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}: {self.text}"


class user_view(models.Model):
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    password = models.CharField(max_length=150, verbose_name="Пароль")
    email = models.CharField(max_length=150, verbose_name="Почта")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name= models.CharField(max_length=150, verbose_name="Фамилия")


