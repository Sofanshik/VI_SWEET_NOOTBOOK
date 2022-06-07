from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


status_choices = (
    ("InPROGRESS", 'In Progress'),
    ("DONE", 'Done'),
    ("DECLINED", 'Declined')
)

def validation_min_length(value):
    if len(value) < 5:
        raise ValidationError(
            _('%(value)s is so small'),
            params={'value': value},
        )


class Cake(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, unique=True, validators=[validation_min_length])  # , validators=validation_min_length(6)
    description = models.CharField(max_length=250, null=True, blank=True)
    cake_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Confectioner(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    surname = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=18)
    e_mail = models.EmailField(max_length=35)

    def __str__(self):
        return self.surname


class OrderC(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confectioner_id = models.ForeignKey(Confectioner, on_delete=models.CASCADE)
    time_date_order = models.DateTimeField()
    prise_sum = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=11, choices=status_choices, default="InPROGRESS")
    # ссылка на торт

    def __str__(self):
        return self.id


# class ShoppingCart(models.Model):
#     cake_id = models.ForeignKey(Cake, on_delete=models.CASCADE, primary_key=True)
#     orderc_id = models.ForeignKey(OrderC, on_delete=models.CASCADE, primary_key=True, null=True, blank=True)
#     count = models.IntegerField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.cake_id


class Blog(models.Model):
    confectioner_id = models.ForeignKey(Confectioner, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mark = models.IntegerField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.mark
