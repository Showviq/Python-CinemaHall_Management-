class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._init_seats()
        super().entry_hall(self)

    def _init_seats(self):
        for row in range(1, self._rows + 1):
            self._seats[row] = [0] * self._cols

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        show_found = False
        for show in self._show_list:
            if show[0] == show_id:
                show_found = True
                break

        if not show_found:
            print("Show ID is invalid.\nPlease enter a valid show ID.\nChoose option 1 to view all shows and their details.")
            return -1

        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print("Invalid seat No. Rows and Column should be between 1 to 8")
                return 0
            if self._seats[show_id][row - 1][col - 1] == 1:
                print(f"Seat ({row},{col}) is already booked for show {show_id}.")
                return 0
            self._seats[show_id][row - 1][col - 1] = 1
            print(f"Your seat ({row},{col}) booked for show {show_id} successfully.")
        return 1

    def view_show_list(self):
        for show_id, movie_name, time in self._show_list:
            print(f"MOVIE NAME:{movie_name} SHOW ID:{show_id} TIME:{time}")

    def view_available_seats(self, show_id):
        show_found = False
        for show in self._show_list:
            if show[0] == show_id:
                show_found = True
                break

        if not show_found:
            print("Show ID is invalid.\nPlease enter a valid show ID.\nChoose option 1 to view all shows and their details.")
            return

        print(f"Available seats for show {show_id}:")
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                if self._seats[show_id][row - 1][col - 1] == 0:
                    print(f"({row},{col})", end=' ')
            print()

def main():
    cinema_hall = Hall(rows=8, cols=8, hall_no=1)

    cinema_hall.entry_show(100, "PRIYOTOMA", "07/10/2023 11:00 AM")
    cinema_hall.entry_show(101, "SURONGO",  "07/10/2023 03:00 PM")
    cinema_hall.entry_show(110, "PROHELIKA", "07/10/2023 09:00 AM")
    cinema_hall.entry_show(111, "KILL HIM", "07/10/2023 06:00 PM")

    while True:
        print("Welcome to Star Cinema!\nHow can we help you?")
        print("1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. EXIT")
        option = input("ENTER OPTION: ")

        if option == "1":
            cinema_hall.view_show_list()
        elif option == "2":
            hall_id = int(input("ENTER SHOW ID: "))
            cinema_hall.view_available_seats(hall_id)
        elif option == "3":
            hall_id = int(input("ENTER SHOW ID: "))
            show_found = False
            for show in cinema_hall._show_list:
                if show[0] == hall_id:
                    show_found = True
                    break
            if not show_found:
                print("Show ID is invalid.\nPlease enter a valid show ID.\nChoose option 1 to view all shows and their details.")
                continue

            num_tickets = int(input("NUMBER OF TICKETS?: "))
            i = 0
            while i < num_tickets:
                seat_list = []
                row = int(input("ENTER SEAT ROW (1-8): "))
                col = int(input("ENTER SEAT COL (1-8): "))
                seat_list.append((row, col))
                verdict = cinema_hall.book_seats(hall_id, seat_list)
                if verdict == 0:
                    continue
                i += 1
        elif option == "4":
            print("Thank you for choosing stay with us.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()