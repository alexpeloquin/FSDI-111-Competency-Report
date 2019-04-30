import pickle
from video import Video

inventory = []
inventory_file = "inventory.dat"

counter = 1

def create_new():
    global counter
    print("-"*24)
    print("Alright, lets add a new video to our inventory")
    print("-"*24)
    try:
        title = input("What is the title? ")
        year = int(input("What year was this made? "))
        price = float(input("How much do you want to charge to rent? "))
        stock = int(input("How many copies do you have for stock? "))
        v = Video(counter,title,year,price,stock)
        counter+=1
        inventory.append(v)
        save_inventory()
        input("Video created. Press Enter to continue")
    except:
        #to show if there is an error
        print("*** You entered data incorrectly, please revise ***")

def print_list():
    global Video
    print("\n")
    print("-"*24)
    print("Inventory by title(id) and stock on hand")
    print("-"*24)
    count = 1
    for v in inventory:
        print(str(count) + ". " + str(v.title) + " (" + str(v.id) + ") " + "- " + str(v.stock))
        count+=1
    print("-"*24)
    print("\n")

def rent_video():
    movie_list()
    global Video
    try:
        selection = input("What movie would you like to rent? ")
        selection = int(selection) - 1
        if selection >= 0:
            v = inventory[selection]
            v.stock -=1
            save_inventory()
            print("There is " + str(v.stock) + " remaining" )
    except:
        print("*** Your data is not valid ****")

def return_video():
    movie_list()
    global Video
    try:
        selection = input("What movie are you here to return? ")
        selection = int(selection) -1
        if selection >= 0:
            v = inventory[selection]
            v.stock +=1
            save_inventory()
            print("There is " + str(v.stock) + " remaining" )
    except:
        print("*** Your data is not valid ****")

        
def movie_list():
    global Video
    print("-"*24)
    print("These are the movies available for rent")
    print("Title  (Price)  Stock")
    print("-"*24)
    count = 1
    for v in inventory:
        print(str(count) + "." + str(v.title) + " (" + str(v.price) + ") " + "   " + str(v.stock))
        count +=1
    print("-"*24)

def save_inventory():
    writter = open(inventory_file,"wb")
    pickle.dump(inventory,writter)
    writter.close()
    print("Update Saved!!")

def load_inventory():
    try:
        reader = open(inventory_file,"rb")
        temp = pickle.load(reader)
        for v in temp:
            inventory.append(v) # put the car in array
        print("Loaded from DB: " + str(len(inventory)))
    except:
        print("***No data to read or corrupted***")