'''
This is a class for pets used in digital pet games. Users can create a pet
and perform functions such as feeding, playing, and sleepin.
'''


class pet:
    def __init__(self, name:str, species:str):
        self.name = name
        self.species = species.lower()
        self.energy = 20
        self.happiness = 50
        self.health = 100

    def pet_image(self):
        '''
        Show images of pets
        '''
        if self.species == 'cat':
            print(r'''
  /\_/\\  
 ( o.o ) 
  > ^ <
''')
        elif self.species == 'dog':
            print(r'''
  / \\__
 (    @\\___
 /         O
/   (_____/
/_____/   U
''')
    
    def feed_pet(self):
        '''
        Feeding function: Different foods have different effects
        '''
        food_type = input('Plase choose food type [chicken]|[snacks]|[fish]|[bone]:')
        # First, ask about the type of food to be fed. It must be healthy enough before feeding
        
        if self.health > 10:
            
            if food_type == "chicken":
                self.energy += 10
                self.health += 5
                self.happiness +=1
                print('🍗 😋 Delicious chicken!')
        
            elif food_type == "snacks":
                self.energy += 2
                self.health -= 5
                self.happiness += 5
                print('🍪🍪🍪')
                print (f"Your pet {self.name} is very happy!")
        
            elif food_type == "fish":
                if self.species == "cat":
                    self.energy += 10
                    self.health += 5
                    self.happiness += 10
                    print('🐱 ❤ ❤ ❤ 🐟')
                    print(f"This is {self.name}'s favorite food!!!")
                elif self.species == "dog":
                    self.happiness -= 10
                    print(f"🐶 {self.name} doesn't like this food (︶︹︺) ")
        

            elif food_type == "bone":
                if self.species == "dog":
                    self.energy += 10
                    self.health += 5
                    self.happiness += 10
                    print('🐶 ❤ ❤ ❤ 🦴')
                    print(f"This is {self.name}'s favorite food!!!")
                elif self.species == "cat":
                    self.happiness -= 10
                    print(f"🐱 {self.name} doesn't like this food (︶︹︺) ")
        
            else:
                print('Please choose the correct types of food')
                return False

            # Check health, hunger level and happiness value after feeding
            print('Eating is done.')

            if self.health <= 10:
                print(f"| Warning | Your pet {self.name}'s health level has dropped to 10 and it is in danger of losing its life!")
            if self.energy >100:
                print(f"| Warning | Your pet {self.name} eats too much! There is a risk of obesity. ")
            if self.happiness <= 0:
                self.happiness = 0
                print(f"| Warning | Your pet {self.name}'s happiness value is 0. Please note!")
            elif self.happiness > 100:
                self.happiness = 100
            return True
        
        # If not healthy enough, print the prompt message
        if self.health <=10:
            print(f"| Warning | Your pet {self.name} is not healthy enough! Unable to feed")
        
    
    def interaction_pet (self):
        '''
        Interactive functions: Different interactions have different effects
        '''
        interaction_type = input("Plase choose interaction type [walk]|[ball]|[bath]|[TV]:")
        #Ask about the type of interaction before the interaction. If the pet is not healthy or hungry, interaction cannot be carried out
        
        if self.energy > 0 and self.health > 10:

            if interaction_type == "walk":
                if self.energy < 15:
                    print(f"Sorry, your pet {self.name} energy level is not high enough to complete this activity")
                else:
                    self.happiness += 15
                    self.health += 5
                    self.energy -= 15
                    if self.species == 'cat':
                        print('🐱 walking...')
                    elif self.species == 'dog':
                        print('🐶 walking...')
            
            elif interaction_type == 'ball':
                if self.energy < 20:
                    print(f"Sorry, your pet {self.name} energy level is not high enough to complete this activity")
                else:
                    self.happiness += 20
                    self.health += 5
                    self.energy -= 20
                    if self.species == 'cat':
                        print('🐱 → ⚽ pounces on the ball!')
                    elif self.species == 'dog':
                        print('🐶 → ⚽ pounces on the ball!')
            
            elif interaction_type == 'bath':
                self.happiness += 5
                self.health += 10
                if self.species == 'cat':
                    print('🛀 🐱 💧')
                elif self.species == 'dog':
                    print('🛀 🐶 💧')
            
            elif interaction_type == 'TV':
                if self.energy < 5:
                    print(f"Sorry, your pet {self.name} energy level is not high enough to complete this activity")
                else:
                    self.happiness += 10
                    self.energy -= 5
                    if self.species == 'cat':
                        print('🐱...📺')
                    elif self.species == 'dog':
                        print('🐶...📺')
            else:
                print('Please enter the correct type of interaction!')
                return False
            
            # After the interaction is completed, check whether all indicators are normal
            print('The interaction is completed.')
            if self.health > 100:
                self.health= 100
            if self.happiness >100:
                self.happiness = 100
            if self.energy <= 0:
                self.energy = 0
                print(f"| Warning | Your pet {self.name} is too hungry!")
            return True

        # Give a prompt if interaction is not possible
        if self.energy == 0:
            print(f"| Warning | Your pet {self.name} is too hungry!")
        if self.health < 10:
            print(f"| Warning | Your pet {self.name} is not healthy enough! Unable to interact")

    def sleep(self):
        '''
        Sleep function, restore health, energy reduction
        '''
        self.health += 10
        self.energy -= 20
        if self.species == 'cat':
            print(' 🐱🌙 ....💤 ')
            print(' ............')
            print(' ......☀.....')
        
        elif self.species == 'dog':
            print(' 🐱🌙 ....💤 ')
            print(' ............')
            print(' ......☀.....')

        if self.health > 100:
            self.health = 100
        if self.energy < 0:
            self.energy = 0
            print(f"| Warning | Your pet {self.name} is too hungry!")
    
    def go_hospital(self):
        '''
        For the function of going to the hospital, the pet's health condition must 
        be below 10 to go to the hospital and restore its health
        '''
        if self.health > 10:
            print('Your pet is very healthy! There is no need to go to the hospital')
        else:
            self.health += 25
            if self.species =='cat':
                print('🐱 → 🏥 ')
                print('⛑ → 🐱 ❤ +++')
            elif self.species =='dog':
                print('🐶 → 🏥')
                print('⛑ → 🐶 ❤ +++')
            
            print('Your pet has successfully received treatment!')
    
    def __str__(self) -> str:
        '''Returns a status report summarising the pet's current state.'''
        return f'''Status Report - {self.name}
-------------------------
Type       : {self.species}
Energy     : {self.energy}
Health     : {self.health}
Happiness  : {self.happiness}
-------------------------'''
    

        
            

                    



