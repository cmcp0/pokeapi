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
    type = models.CharField(max_length= 50,)
    id_pokemon = models.IntegerField()
    name_pokemon = models.CharField(max_length= 50)

    def __str__(self):
        return f'{self.type} {self.name_pokemon}'   

class BaseStat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
    stat = models.IntegerField()
    effort = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.stat}' 
