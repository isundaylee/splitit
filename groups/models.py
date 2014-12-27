from django.db import models

# Create your models here.

class Group(models.Model):

  class Meta:
    verbose_name = "Group"
    verbose_name_plural = "Groups"

  def __str__(self):
    pass

  name = models.TextField()

class Person(models.Model):

  class Meta:
    verbose_name = "Person"
    verbose_name_plural = "Persons"

  def __str__(self):
    return self.name

  def balance(self):
    amounts = list(map(lambda t: t.amount, self.transaction_set.all()))
    return sum(amounts)

  name = models.TextField()
  group = models.ForeignKey(Group, related_name='member_set')