import json

# Room details
rooms = {
    101: {"type": "Single", "rate": 2000},
    102: {"type": "Double", "rate": 3500},
    201: {"type": "Suite", "rate": 6000}
}

# Load previous bookings from file
def load_bookings():
    try:
        with open("bookings.txt", "r") as file:
            data = json.load(file)
            return {int(room): details for room, details in data.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


bookings = load_bookings()

# Save bookings in file
def save_bookings():
    with open("bookings.txt", "w") as file:
        json.dump(bookings, file, indent=4)


# Display available rooms
def view_rooms():
    print("\n----- ROOM DETAILS -----")

    for room_no, details in rooms.items():
        status = "Booked" if room_no in bookings else "Available"

        print("Room:", room_no)
        print("Type:", details["type"])
        print("Price per night: Rs.", details["rate"])
        print("Status:", status)
        print("------------------------")


# Generate bill
def generate_bill(room_no):
    if room_no not in bookings:
        print("This room is not booked.")
        return

    guest = bookings[room_no]["guest"]
    nights = bookings[room_no]["nights"]
    rate = rooms[room_no]["rate"]

    amount = rate * nights
    gst = amount * 12 / 100
    total = amount + gst

    print("\n------- HOTEL BILL -------")
    print("Guest Name:", guest)
    print("Room Number:", room_no)
    print("Number of Nights:", nights)
    print("Room Charge:", amount)
    print("GST (12%):", int(gst))
    print("Total Bill: Rs.", int(total))
    print("--------------------------")


# Book a room
def book_room():
    try:
        guest = input("Enter guest name: ")
        room_no = int(input("Enter room number: "))
        nights = int(input("Enter number of nights: "))

        if room_no not in rooms:
            print("Invalid room number.")
            return

        if room_no in bookings:
            print("Room", room_no, "is already booked. Please choose another room.")
            return

        if nights < 1 or nights > 30:
            print("Please enter nights between 1 and 30.")
            return

        bookings[room_no] = {
            "guest": guest,
            "nights": nights
        }

        save_bookings()

        print("\nRoom", room_no, "booked for", guest, "|", nights, "night(s)")
        generate_bill(room_no)

    except ValueError:
        print("Please enter valid numeric values.")


# Cancel a booking
def cancel_booking():
    try:
        room_no = int(input("Enter room number to cancel: "))

        if room_no in bookings:
            guest = bookings[room_no]["guest"]
            del bookings[room_no]

            save_bookings()

            print("Booking for", guest, "in room", room_no, "cancelled.")
        else:
            print("This room is not currently booked.")

    except ValueError:
        print("Please enter a valid room number.")


# Main menu
def main():
    while True:
        print("\n===== HOTEL ROOM BOOKING SYSTEM =====")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Generate Bill")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            try:
                room_no = int(input("Enter room number: "))
                generate_bill(room_no)
            except ValueError:
                print("Please enter a valid room number.")

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            print("Thank you for using our Hotel Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
