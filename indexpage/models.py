from django.db import models

# подразделение
class Division(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

# профессия
class Profession(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


# работник
class Worker(models.Model):
    # имя
    firstname = models.CharField(max_length=50)
    # фамилия
    secondname = models.CharField(max_length=50)
    # подразделение
    division = models.ForeignKey(Division,
                              related_name='order_divisions',
                              on_delete=models.CASCADE)
    # профессия
    profession = models.ForeignKey(Profession,
                                related_name='order_professions',
                                on_delete=models.CASCADE)
    # оклад
    salary = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering = ('firstname', 'secondname',)

    def __str__(self):
        return f'Работник {self.firstname} {self.secondname}, {self.division}, {self.profession}, оклад = {self.salary}'




