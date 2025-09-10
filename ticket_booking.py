class MovieTicketBookingSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = []

    def display_available_seats(self):
        available_seats = [seat for seat in range(1, self.total_seats + 1) if seat not in self.booked_seats]
        print("Available seats:", available_seats)

    def book_seat(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            print("Invalid seat number. Please choose a seat between 1 and", self.total_seats)
        elif seat_number in self.booked_seats:
            print("Seat already booked. Please choose a different seat.")
        else:
            self.booked_seats.append(seat_number)
            print("Seat", seat_number, "booked successfully.")

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            print("Seat", seat_number, "cancellation successful.")
        else:
            print("Seat is not booked. Cannot cancel.")

# Example usage
total_seats = 10
booked_seats = [2, 5, 7]

booking_system = MovieTicketBookingSystem(total_seats)
booking_system.booked_seats = booked_seats

booking_system.book_seat(3)
booking_system.cancel_seat(5)

booking_system.display_available_seats()

