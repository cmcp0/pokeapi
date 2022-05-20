from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 50)
    height = models.DecimalField(decimal_places=1, max_digits= 6)
    weight = models.DecimalField(decimal_places=1, max_digits= 6)

    def __str__(self) -> str:
        return self.name

class EvolutionType(models.Model):
    key = models.ForeignKey(Pokemon, on_delete= models.CASCADE)
    id_pokemon = models.IntegerField()
    name_pokemon = models.CharField(max_length= 50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.key.name    

class Evolution(EvolutionType):
    pass

class PreEvolution(EvolutionType):
    pass

class BaseStat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
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