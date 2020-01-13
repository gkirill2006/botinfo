# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Draw(models.Model):
    block_number = models.IntegerField(blank=True, null=True)
    hash = models.TextField(blank=True, null=True)
    winner_number = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    members_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'draw'


class DrawBets(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    btc_address = models.TextField(blank=True, null=True)
    pay = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'draw_bets'


class Lang(models.Model):
    ru = models.TextField(blank=True, null=True)
    en = models.TextField(blank=True, null=True)
    es = models.TextField(blank=True, null=True)
    cn = models.TextField(blank=True, null=True)
    de = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang'


class Numbers(models.Model):
    block_number = models.IntegerField(blank=True, null=True)
    hash = models.TextField(blank=True, null=True)
    numbers_block = models.TextField(blank=True, null=True)
    last_number = models.IntegerField(blank=True, null=True)
    five_of_thirty_six = models.IntegerField(blank=True, null=True)
    six_of_forty_five = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


    def __str__(self):
        return self.hash


class Users(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    language_bot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    count_visits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
