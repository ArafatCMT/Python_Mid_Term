class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        
    def entry_show(self, movie_name, id,time):
        tuple = (movie_name, id, time)
        self.__show_list.append(tuple)
        _2Dlst = [[int(0) for i in range(self._cols)] for j in range(self._rows)]
        self._seats["id"] = _2Dlst

    def book_seats(self,id):
        flag = False
        for tuple in self.__show_list:
            # check valid id
            if id == tuple[1]:
                flag = True
                ticket = int(input("Number of ticket?: "))
                cnt = 0
                while cnt != ticket:
                    row = int(input("Enter set row: "))
                    col = int(input("Enter set col: "))
                    seat_list = self._seats["id"]
                    # check valid seat 
                    if (row >= 0 and row < self._rows) and (col >= 0 and col < self._cols):
                        if seat_list[row][col] == 0:
                            seat_list[row][col] = 1
                            print()
                            print(f"Seat {(row,col)} booked for \"{tuple[0]}\" movie" )
                            print()
                            cnt += 1
                        else:
                            print()
                            print("Already booked !")
                            print()
                    else:
                        print()
                        print("Invalid seat !")
                        print()
        if flag is False:
            print()
            print("Incorrect show id !")
            print()
            # recursion 
            id = input("Please, Enter corret show Id: ")
            self.book_seats(id)

    def view_show_list(self):
        print("---------------")
        for tuple in self.__show_list:
            print(f"MOVIE NAME : {tuple[0]}({tuple[1]})  SHOW ID : {tuple[1]}  TIME : {tuple[2]}")
        print("---------------")

    def view_available_seats(self, id):
        match = False
        for tuple in self.__show_list:
            if id == tuple[1]:
                print("True for available seat otherwise seat is booked already.")
                print()
                print()
                match = True
                _2dList = self._seats["id"]
                print(f"Available Seat for \"{tuple[0]}\" Movie:")
                for i in range(0,self._rows):
                    for j in range(0,self._cols):
                        if _2dList[i][j] == 0:
                            print(f"Seat {i,j}")
                print(f"Updated Seat Matrix for Hall {self._hall_no}:")
                print()
                print()
                lst = []
                for i in range(0,self._rows):
                    for j in range(0,self._cols):
                        lst.append(_2dList[i][j])
                    print(lst)
                    lst = []
                print()
                print()
        if match is False:
            print()
            print("Incorrect show id !")
            print()
            # recursion 
            id = input("Please, Enter corret show Id: ")
            self.view_available_seats(id)
            

class Star_Cinema:
    hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)
        

Cine_Complex = Star_Cinema()
Cine_Complex.entry_hall(6, 7, 1)

Bioscope = Hall(6,7,1)
Bioscope.entry_show("Rajkumar", "549", "10/04/2024  11:00 AM")
Bioscope.entry_show("PriyoToma", "333", "10/04/2024  2:00 PM")
Bioscope.entry_show("Kill Him", "696", "10/04/2024  6:00 PM")

while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    print()

    option = int(input("Enter Option: "))

    if option == 1:
        Bioscope.view_show_list()

    elif option == 2:
        id = input("Enter Show Id: ")
        Bioscope.view_available_seats(id)

    elif option == 3:
        id = input("Show Id: ")
        Bioscope.book_seats(id)

    elif option == 4:
        break
    else:
        print()
        print("Please, Select correct option!")
        print()