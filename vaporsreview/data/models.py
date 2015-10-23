from django.db import models

RATING_CHOICES = zip(range(1, 6), range(1, 6))
CURRENCY = [
    'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
    'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD',
    'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP',
    'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP',
    'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR',
    'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW',
    'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA',
    'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD',
    'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
    'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL',
    'SOS', 'SRD', 'SSP', 'STD', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD',
    'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'USS', 'UYI', 'UYU', 'UZS', 'VEF', 'VND', 'VUV',
    'WST', 'XAF', 'XAG', 'XAU', 'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XFU', 'XOF', 'XPD',
    'XPF', 'XPT', 'XSU', 'XTS', 'XUA', 'XXX', 'YER', 'ZAR', 'ZMW'
]
CURRENCY_CHOICES = [(el, el) for el in CURRENCY]


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('parrent', 'name')

    parrent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):

    class Meta:
        unique_together = (('name', 'address'), ('latitude', 'longitude'))

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    logo = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return self.name


class Item(models.Model):

    source_url = models.URLField()
    category = models.ForeignKey('Category')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField()
    video = models.URLField(null=True, blank=True)
    summary = models.TextField()
    features = models.TextField(help_text='Add name | value pairs seperated by new line')
    pros = models.TextField(help_text='Add values seperated by new line')
    cons = models.TextField(help_text='Add values seperated by new line')
    conclusion = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    price = models.FloatField()
    discounted_price = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    discount_code = models.CharField(max_length=10, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
