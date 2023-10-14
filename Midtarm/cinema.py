class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.allocate_seats()
        self.entry_hall(self)

    def allocate_seats(self):
        for i in range(self.rows):
            for j in range(self.cols):
                seat_id = f"{i},{j}"
                self.seats[seat_id] = "0"

    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        self.show_list.append(movie)
        self.seats[id] = [["0" for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, seat_id, seats_book):
        if seat_id not in [show[0] for show in self.show_list]:
            raise ValueError("Please Provide a Valid ID")
        for seat in seats_book:
            row, col = seat
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                raise ValueError("Please Provide a Valid Seat")
            if self.seats[seat_id][row][col] == "1":
                raise ValueError("Already Booked")
            self.seats[seat_id][row][col] = "1"

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        # for show in self.show_list:
        #     if id not in show[0]:
        #         raise ValueError("Please Provide a Valid ID")
        # for row in self.seats[id]:
        #     for seat in row:
        #         print(seat)
        #      print()
        if id not in [show[0] for show in self.show_list]:
            raise ValueError("Please Provide a Valid Id")
        print([[seat for seat in row] for row in self.seats[id]])


hall1 = Hall(6, 6, 1)
hall1.entry_show("111", "Spider_man1", "9:30")
hall1.entry_show("112", "Spider_man2", "9:30")
hall1.entry_show("113", "Spider_man3", "9:30")
hall1.entry_show("114", "Spider_man4", "9:30")

while True:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book ticket")
    print("4. Exit")
    s = int(input("Enter Option: "))

    if s == 1:
        for show in hall1.show_list:
            print(show)
    elif s == 2:
        id = input("show id: ")
        hall1.view_available_seats(id)
    elif s == 3:
        id = input("Show ID: ")
        row = int(input("Enter seat row: "))
        col = int(input("Enter seat col: "))
        hall1.book_seats(id, [(row, col)])
        print(f"Seat ({row,col}) booked for show {id}")
    elif s == 4:
        break
