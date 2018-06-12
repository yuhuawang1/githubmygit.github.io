__author__ = 'tianyyan'
from django.db import models


class StsMaintNERev1(models.Model):
    ne_name = models.CharField(max_length=45)
    ne_type = models.CharField(max_length=45)
    ne_alias = models.CharField(max_length=45)  # added NE's alias
    ip = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    method = models.CharField(max_length=10)
    is_routine_check = models.BooleanField(default=True)
    check_items = models.CharField(max_length=1000)

    class Meta:
        db_table = 'stsmaintnerev1'

    def __str__(self):
        return self.ne_name


class NESPC(models.Model):
    ip = models.ForeignKey(StsMaintNERev1)
    spc = models.CharField(max_length=20, blank=True)


class StsMaintCheckItemRev1(models.Model):
    ne_type = models.CharField(max_length=45)
    item = models.CharField(max_length=45)
    description = models.CharField(max_length=1000)
    is_compared = models.BooleanField(default=False)
    missing_check = models.BooleanField(default=False)

    class Meta:
        db_table = 'stsmaintcheckitemrev1'

    def __str__(self):
        return self.item


class StsMaintPermission(models.Model):
    PERMISSION = (
        ('Email', 'Email'),
        ('Analysis Data', 'Analysis Data'),
        ('Original Report', 'Original Report'),
        ('Alarm Log', 'Alarm Log'),
        ('All', 'All'),
    )
    email = models.EmailField()
    permission = models.CharField(max_length=20, choices=PERMISSION)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'stsmaintpermission'


class StsMaintCheckDataRev1(models.Model):
    ne_name = models.CharField(max_length=45)
    ne_type = models.CharField(max_length=45)
    item = models.CharField(max_length=45)
    sub_item = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField()
    value = models.CharField(max_length=1000)
    is_alarm = models.BooleanField()
    tag = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'stsmaintcheckdatarev1'

    def __str__(self):
        return self.ne_name


class StsMaintReport(models.Model):
    url = models.CharField(max_length=200)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'stsmaintreport'


class StsMaintCheckItemPerNERev1(models.Model):
    ip = models.CharField(max_length=45)
    item = models.CharField(max_length=45)
    ne_type = models.CharField(max_length=45)

    class Meta:
        db_table = 'stsmaintcheckitempernerev1'

    def __str__(self):
        return self.ip


class StsMaintSchedule(models.Model):
    min = models.CharField(max_length=10)
    hour = models.CharField(max_length=10)
    dayofmonth = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    dayofweek = models.CharField(max_length=10)

    def __str__(self):
        return self.hour

    class Meta:
        db_table = 'stsmaintschedule'
