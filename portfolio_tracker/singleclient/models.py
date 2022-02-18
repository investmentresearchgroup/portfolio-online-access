from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
MAX_LENGTH = 50
MAX_DIGITS = 15
DECIMAL_PLACES = 5
ALPHANUMERIC = RegexValidator(r'^[0-9a-zA-Z]*$', "Only alphanumeric characters are allowed.")
ALPHABET = RegexValidator(r'[A-Za-z]*$',"Only alphabetic characters are allowed.")


class Client(models.Model):
    fpk = models.CharField(max_length=MAX_LENGTH)
    name = models.CharField(max_length=MAX_LENGTH)
    date_opened = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fpk} - {self.name}"
    class Meta:
        unique_together = ['fpk']

class AccountType(models.Model):
    account_type = models.CharField(max_length=50,validators=[ALPHABET])

    def __str__(self):
        return self.account_type
    class Meta:
        unique_together = ['account_type']


class Account(models.Model):
    fpk = models.CharField(max_length=MAX_LENGTH)
    clientid = models.ForeignKey(Client,on_delete=models.CASCADE)
    name = models.CharField(max_length=MAX_LENGTH)
    date_opened = models.DateField()
    account_type = models.ForeignKey(AccountType,on_delete=models.CASCADE)
    inception_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fpk} - {self.name}"

    class Meta:
        unique_together = ['fpk']


class SecurityAssetClass(models.Model):
    security_asset_class = models.CharField(max_length=50,validators=[ALPHABET])

    def __str__(self):
        return self.security_asset_class
    class Meta:
        unique_together = ['security_asset_class']
        verbose_name = 'Security Asset Class'
        verbose_name_plural = 'Security Asset Classes'


class Security(models.Model):
    fpk = models.CharField(max_length=MAX_LENGTH)
    name = models.CharField(max_length=MAX_LENGTH)
    asset_class = models.ForeignKey(SecurityAssetClass,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fpk} - {self.name}"
    class Meta:
        unique_together = ['fpk']
        verbose_name_plural = 'Securities'


class SecurityPrice(models.Model):
    securityid = models.ForeignKey(Security,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['securityid','date']


class Transaction(models.Model):
    accountid = models.ForeignKey(Account,on_delete=models.CASCADE)
    security = models.ForeignKey(Security,on_delete=models.CASCADE)
    trade_date = models.DateField()

    TRANSACTION_TYPE_CHOICES = [
        ("BUY","Buy"),
        ("SELL","Sell"),
        ("DIVIDEND","Dividend"),
        ("INTEREST","Interest"),
        ("DEPOSIT","Deposit"),
        ("WITHDRAWAL","Withdrawal"),
    ]
    trx_type = models.CharField(choices=TRANSACTION_TYPE_CHOICES,max_length=MAX_LENGTH)
    trx_qty =  models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    trx_amt = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    trxid = models.CharField(max_length=MAX_LENGTH,validators=[ALPHANUMERIC])
    comment = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        unique_together = ['trxid']
