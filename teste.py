class Player:
    
    def _init_(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/ point de vie", health, "/ force d'attaque", attack)

    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
     return self.health
    
    def get_attack(self):
      return self.attack
    
    def damage(self, damege):
       self.health -= damege                                                                                                                
       
    def attack_player(self, target_player):
       target_player.damege()



Player1 = Player("sensey", 20, 30, 3)
Player2 = Player("Bob", 20, 25, 3)

Player1.attack_player(Player2)
print(Player1.get_pseudo(), "attaque", Player2.get_pseudo())
print("Bienvenue au joueur", Player1.get_pseudo, "/ point de vie", Player1.get_health, "/ force d'attaque", Player1.get_attack_value())  
class weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damege = damage


    def get_name(self):
        return self.name
    
    def get_damege_amount(self):
        return self.damege
knife = weapon("couteau", 3)