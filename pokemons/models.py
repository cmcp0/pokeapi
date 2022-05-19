from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    height = models.DecimalField(decimal_places=1)
    weight = models.DecimalField(decimal_places=1)

class EvolutionType(models.Model):
    pokemon = models.ForeignKey(Pokemon)

    class Meta:
        abstract = True

class Evolution(EvolutionType):
    pass

class PreEvolution(EvolutionType):
    pass

class BaseStat(models.Model):
    pokemon = models.ForeignKey(Pokemon)
    name = models.CharField()
    stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        abstract = True

class Hp(BaseStat):
    pass

class Attack(BaseStat):
    pass

class Defense(BaseStat):
    pass
class SpecialAttack(BaseStat):
    pass

class SpecialDefense(BaseStat):
    pass

class Speed(BaseStat):
    pass