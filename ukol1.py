from dataclasses import dataclass
import math

@dataclass
class Locality:        #lokalita, kde se nemovitost nachazi
  name: str            #nazev katastru/obce
  koefficient: float   #koeficient, ktery se pouziva pri vypoctu dane

@dataclass   
class Property:       #nemovitost
  locality: Locality

@dataclass
class Estate(Property):
  estate_type: str    #typ pozemku
  area: float         #plocha pozemku v m2

  def calculate_tax(self):        #spocita vysi dane pro pozemek
    estate_types_coef = {         #koeficient
      "land" : 0.85,       
      "building_site" : 9,
      "forrest" : 0.35}
    return math.ceil(self.area * estate_types_coef[self.estate_type] * self.locality.koefficient)

  def __str__(self):
    estate_types = {
       "land" : "zemědělský pozemek",
       "building_site" : "stavební pozemek",
       "forrest" : "les"}
    return f"{estate_types[self.estate_type]}, lokalita {self.locality.name} (koeficient {self.locality.koefficient}), {self.area} metrů čtverečních, daň je {self.calculate_tax()}"
  
@dataclass
class Residence(Property):
  area: float
  commercial: bool

  def calculate_tax(self):              #vyse dane pro byt
     return math.ceil(self.area * self.locality.koefficient * 15 * (self.commercial + 1))
  
  def __str__(self):
    com = {
      True : "urcena",
      False : "neni urcena"}
    return f"lokalita {self.locality.name} (koeficient {self.locality.koefficient}), {self.area } metrů čtverečních, nemovitost {com[self.commercial]} k podnikani, daň je {self.calculate_tax()}"
  
  # Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8
pozemek = Locality('Manětín', 0.8)
pozemek1 = Estate(pozemek, 'land', 900)
print(pozemek1.calculate_tax())
print(str(pozemek1))

# Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8
dum = Residence(pozemek, 120, 0)
print(dum.calculate_tax())
print(str(dum))

# Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3
kancelar = Locality('Brno', 3)
kancelar1 = Residence(kancelar, 90, 1)
print(kancelar1.calculate_tax())
print(str(kancelar1))
