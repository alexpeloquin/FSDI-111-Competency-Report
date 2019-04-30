from menu import menu
from video import Video
from functions import create_new,print_list,save_inventory,rent_video,movie_list,return_video,load_inventory

#Load inventory from DB
load_inventory()
# Start the system
selection= ""
while selection != "x":
    selection = menu()
    if(selection == "1"):
        create_new()
    elif(selection == "2"):
        print_list()
    elif(selection == "3"):
        rent_video()
    elif(selection == "4"):
        return_video()
