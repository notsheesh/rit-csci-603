from dataclasses import dataclass
import sys

DEBUG = False

@dataclass
class Passenger: 
    __slots__ = "name", "ticket_number", "has_carry_on", "zone"

    name: str
    ticket_number: int
    has_carry_on: bool
    zone: str

    def __init__(self, name: str, ticket_number: int, has_carry_on: bool):
        self.name = name
        self.ticket_number = ticket_number
        self.zone = self._parse_ticket(ticket_number)
        self.has_carry_on = has_carry_on
    
    def get_name(self):
        return self.name

    def _parse_ticket(self, ticket_number):
        first_digit = int(str(ticket_number)[0])
        zone_letter = chr(ord('A') + first_digit - 1)
        return zone_letter
    
    def get_ticket_number(self):
        return self.ticket_number

    def get_has_carry_on(self):
        return self.has_carry_on

    def get_zone(self):
        return self.zone
    
    def __str__(self):
        long_str = "{}, ticket: {}, carry_on: {}".format(
            self.get_name(), 
            self.get_ticket_number(), 
            self.get_has_carry_on()
            )

        short_str = str(self.get_ticket_number()) + ": " + self.get_zone();
        # return short_str # For dev env
        return long_str

def test():
    print(Passenger("Alex", 200009, True))

def main():
    test()

if __name__ == '__main__':
    main()