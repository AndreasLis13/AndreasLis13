# This program creates a Car object, a Truck object,
# and an SUV object.
from pyexpat import model
import vehicles

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():

    try:
        vehcile_file = input("Enter file containing vehicles: ")
        
        with open(vehcile_file, 'r') as file:
            
            file.read()
    
    except:
        print("No file found")
    
    vehicles_list = []
    
    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            new_car = vehicles.Car(model = input("Enter model: "),
            model_year = input("Enter model year: "),
            kilometer = input("Enter kilometers: "),
            pris = input("Enter price: "),
            doors = input("Enter doors: "))
            vehicles_list.append(new_car)

        elif choice == NEW_TRUCK_CHOICE:
            new_truck = vehicles.Truck(model = input("Enter model: "),
            model_year = input("Enter model year: "),
            kilometer = input("Enter kilometers: "),
            pris = input("Enter price: "),
            wheeldrive = input("Enter wheeldrive: "))
            vehicles_list.append(new_truck)

        elif choice == NEW_SUV_CHOICE:
            new_suv = vehicles.SUV(model = input("Enter model: "),
            model_year = input("Enter model year: "),
            kilometer = input("Enter kilometers: "),
            pris = input("Enter price: "),
            passangers = input("Enter passangers: "))
            vehicles_list.append(new_suv)
            
        elif choice == FIND_VEHICLE_CHOICE:
            search = input("What vechicle make are your searching for? ")

            for obj in vehicles_list:
                if search == vehicles.Car.get_model(obj):
                    print(obj)
                
                elif search == vehicles.Truck.get_model(obj):
                    print(obj)

                elif search == vehicles.SUV.get_model(obj):
                    print(obj)
                

        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)

        elif choice == QUIT_CHOICE:
            new_list = []

            for obj in vehicles_list:
                str_object = repr(obj)
                new_list.append(str_object)

            vehcile_file = input("Enter filename to save list of vehicles: ")

            with open(vehcile_file, 'w') as file:

                for elem in new_list:
                    file.write(elem)
                
                file.close()
                print('Saving to file and exiting the program...') 

        else:
            print('Error: invalid selection.')    

# The display_menu function displays a menu.5
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit and transfer to file')     

# Call the main function.
if __name__ == '__main__':
      main()