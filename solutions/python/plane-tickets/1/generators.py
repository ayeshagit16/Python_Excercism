"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    alpha = ("A", "B", "C", "D")
    for seq in range(number):
        yield alpha[seq % len(alpha)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seat_letters = generate_seat_letters(number)
    count = 1
    for seq in range(number):
        letter = next(seat_letters)
        yield str(count) + letter
        
        if (seq + 1)%4 == 0:
            count += 1
        if count == 13:
            count += 1

        
        


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_number = generate_seats(len(passengers))
    passenger_list = {}
    for name in passengers:
        passenger_list[name] = next(seat_number)
    return passenger_list


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket_id = seat + flight_id
        count_zero = 12 - len(ticket_id)
        yield ticket_id + "0"*count_zero
        
