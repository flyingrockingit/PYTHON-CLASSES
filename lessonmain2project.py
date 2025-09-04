import random

class hotel_registration:
    def __init__(self, guest_names, room_type, booking_id=None):
        self.guest_names = list(guest_names)     
        self.room_type = room_type
        self.booking_id = booking_id if booking_id else str(random.randint(100000, 999999))

    def display(self):
        print(f"\nGuests: {self.guest_names}\nRoom Type: {self.room_type}\nBooking ID: {self.booking_id}")


guest1 = hotel_registration(("John Smith", "Emily Smith"), "Deluxe")
guest2 = hotel_registration(("Alice Brown",), "Suite")

guest1.display()
guest2.display()
