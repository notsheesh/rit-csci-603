from dataclasses import dataclass
import sys

DEBUG = False

@dataclass
class Passenger: 
    """
    A class representing a passenger and their details.

    Attributes:
    - name (str): The name of the passenger.
    - ticket_number (int): The ticket number of the passenger.
    - has_carry_on (bool): Whether the passenger has carry-on luggage.
    - zone (str): The assigned zone letter for the passenger based on their ticket number.

    Methods:
    - __init__(self, name: str, ticket_number: int, has_carry_on: bool): Initializes a passenger with the provided details.
    - get_name(self): Returns the name of the passenger.
    - get_ticket_number(self): Returns the ticket number of the passenger.
    - get_has_carry_on(self): Returns True if the passenger has carry-on luggage, False otherwise.
    - get_zone(self): Returns the assigned zone letter for the passenger.
    - __str__(self): Returns a string representation of the passenger's details.
    """
    __slots__ = "name", "ticket_number", "has_carry_on", "zone"

    name: str
    ticket_number: int
    has_carry_on: bool
    zone: str

    def __init__(self, name: str, ticket_number: int, has_carry_on: bool):
        """
        Initializes a passenger with the provided details.

        :param name: The name of the passenger.
        :param ticket_number: The ticket number of the passenger.
        :param has_carry_on: Whether the passenger has carry-on luggage.
        """
        self.name = name
        self.ticket_number = ticket_number
        self.zone = self._parse_ticket(ticket_number)
        self.has_carry_on = has_carry_on
    
    def get_name(self):
        """
        Returns the name of the passenger.
        """
        return self.name

    def _parse_ticket(self, ticket_number):
        """
        Parses the ticket number to determine the assigned zone letter for the passenger.

        :param ticket_number: The ticket number of the passenger.
        :return: The assigned zone letter.
        """
        first_digit = int(str(ticket_number)[0])
        zone_letter = chr(ord('A') + first_digit - 1)
        return zone_letter
    
    def get_ticket_number(self):
        """
        Returns the ticket number of the passenger.
        """
        return self.ticket_number

    def get_has_carry_on(self):
        """
        Returns True if the passenger has carry-on luggage, False otherwise.
        """
        return self.has_carry_on

    def get_zone(self):
        """
        Returns the assigned zone letter for the passenger.
        """
        return self.zone
    
    def __str__(self):
        """
        Returns a string representation of the passenger's details.

        For example: "Alex, ticket: 200009, carry_on: True"
        """
        long_str = "{}, ticket: {}, carry_on: {}".format(
            self.get_name(), 
            self.get_ticket_number(), 
            self.get_has_carry_on()
            )

        short_str = str(self.get_ticket_number()) + ": " + self.get_zone();
        return long_str

def test():
    print(Passenger("Alex", 200009, True))

def main():
    test()

if __name__ == '__main__':
    main()