# Video Class for System
class Video:
    id = 0
    title = ""
    year = 0
    price = 0.0
    stock = 0

    # Constructor - the intialization of class attributes
    def __init__(self,id,title,year,price,stock):
        self.id = id
        self.title = title
        self.year = year
        self.price = price
        self.stock = stock
    
    # Method - to have object print all attirbutes
    def print_info(self):
        print("IDd: ")
        print("Title: ")
        print("Year: ")
        print("Price: ")
        print("Stock ")

