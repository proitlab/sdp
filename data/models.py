from django.db import models


KONDISI = [
    ('STANDBY', 'Standby'),
    ('RUSAK', 'Rusak'),
    ('AKTIF', 'Aktif'),
    ('TRIAL', 'Trial'),
    ('BACKUP', 'Backup'),
]

class Vendor(models.Model):
    class Meta:
        db_table = 'vendor'
        verbose_name_plural = 'Vendor'

    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.name    

    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Vendor, self).save(*args, **kwargs)


class ItemDetail(models.Model):
    class Meta:
        db_table = 'item_detail'
        verbose_name_plural = 'Item Detail'

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.name    

    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ItemDetail, self).save(*args, **kwargs)


class Location(models.Model):
    class Meta:
        db_table = 'location'
        verbose_name_plural = 'Location'


    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    area = models.CharField(max_length=50, blank=True)
    coordinate = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.name    

    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Location, self).save(*args, **kwargs)


class Technical(models.Model):
    class Meta:
        db_table = 'technical'
        verbose_name_plural = 'Technical Detail'

    ipaddr = models.GenericIPAddressField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.ipaddr

class Condition(models.Model):
    class Meta:
        db_table = 'condition'
        verbose_name_plural = 'Condition'

    condition = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.condition

    def clean(self):
        self.condition = self.condition.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Condition, self).save(*args, **kwargs)

class Status(models.Model):
    class Meta:
        db_table = 'Status'
        verbose_name_plural = 'Status'

    status = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.status

    def clean(self):
        self.status = self.status.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Status, self).save(*args, **kwargs)


class Items(models.Model):
    class Meta:
        db_table = 'items'
        verbose_name_plural = 'Items'

    item_name = models.ForeignKey(ItemDetail, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    technical = models.ForeignKey(Technical, on_delete=models.PROTECT)
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    serialnumber = models.CharField(max_length=50, unique=True)
    date_accept = models.DateField()
    reason_accept = models.CharField(max_length=100, blank=True)
    date_out = models.DateField(null=True, blank=True)
    reason_out = models.CharField(max_length=100, blank=True)
    date_in = models.DateField(null=True, blank=True)
    reason_in = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s" % self.serialnumber

    def clean(self):
        self.serialnumber = self.serialnumber.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Items, self).save(*args, **kwargs)
