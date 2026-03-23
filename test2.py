class Player:
    
    def _init_(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
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
