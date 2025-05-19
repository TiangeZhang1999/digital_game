
from digital_pet import pet

def main():
    print('| Welcome to the Digital Pet game! |')
    print()

    # The initial pet is empty and needs to be created by the user
    all_pet=[]
    now_pet= None
    
    while True:
        user_action = input("What would you like to do? [add]|[select]|[use]|[list]|[exit]: ").lower()
        print()
        
        if user_action == 'add':
            user_choose_species = input('Please select the specie of pet [cat]|[dog]: ').lower()
            
            while user_choose_species != 'cat' and user_choose_species != 'dog':
                print('Please choose the correct specie of pet!')
                user_choose_species=input('Please select the specie of pet [cat]|[dog]: ')


            print(f"You have chosen the specie of pet: {user_choose_species}")
            print()
            pet_name= input('Please give your pet a name: ')
            new_pet = pet(f'{pet_name}',f'{user_choose_species}')
            all_pet.append(new_pet)
            # Generate a new pet class here and add it to the list

            print("| The pet has been successfully created! |")
            new_pet.pet_image()
            print(new_pet)
            print()
        
        elif user_action == 'select':
            # Select the pet to be operated on
            if all_pet == []:
                print('No pets yet.')
            else:
                chosed_name = input("Enter the name of the pet to select: ")
                found = False
                for p in all_pet:
                    if p.name == chosed_name:
                        now_pet = p
                        print(f"You are now interacting with {p.name}!")
                        found = True
                        break
                if found == False:
                    print("No pet with that name.")
            print()

        elif user_action == 'list':
            # Display all the pets of the user
            if all_pet == []:
                print('No pets yet.')
            else:
                for p in all_pet:
                    print(f'| Name:{p.name} | Specie:{p.species} |')
            print()
        
        elif user_action == 'use':
            # Operate on the selected pet
            if now_pet == None:
                print('No pet selected. Use [select] to choose one.')
            else:
                user_command= input("Please enter a command: [images]|[feed]|[interaction]|[treatment]|[sleep]|[status]|[exit]: ").lower()

                if user_command == 'images':
                    now_pet.pet_image()

                elif user_command == 'feed':
                    now_pet.feed_pet()
        
                elif user_command == 'interaction':
                    now_pet.interaction_pet()
        
                elif user_command =='treatment':
                    now_pet.go_hospital()
        
                elif user_command == 'sleep':
                    now_pet.sleep()
        
                elif user_command == 'status':
                    print(now_pet)
        
                else:
                    print('Please enter the correct instructions!')

            print()
        
        elif user_action == 'exit':
            print('| Game over |')
            break 
        
        else:
            print('Please enter the correct instructions!')

    


        


    




if __name__ == '__main__':
    main()

    


