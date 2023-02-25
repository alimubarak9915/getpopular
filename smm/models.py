import uuid

from django.conf import settings
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.category_name)


class SmmServices(models.Model):
    choices = (
        ('Premium', 'premium'),
        ('Normal', 'normal'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    service_name = models.CharField(max_length=100, null=True, blank=True)
    service_price = models.IntegerField(null=True, blank=True)
    minimum_quantity = models.IntegerField(null=True, blank=True)
    service_description = models.TextField(blank=True, null=True)
    service_tag = models.CharField(max_length=100, null=True, blank=True, choices=choices)

    class Meta:
        verbose_name_plural = 'Smm Services'

    def __str__(self):
        return str(self.service_name)


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    wallet_balance = models.IntegerField(null=True, blank=True)
    transactions_proof_img = models.ImageField(upload_to='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Wallet'

    def __str__(self):
        return str(f"{self.user}-{self.wallet_balance}")


class Orders(models.Model):
    order_status = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    order_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    smm_service = models.ForeignKey(SmmServices, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    order_date_and_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True, blank=True, choices=order_status)

    class Meta:
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = uuid.uuid4().hex[:5].upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(f'{self.smm_service.service_name}-{self.is_paid}')
