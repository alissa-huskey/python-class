from collections import namedtuple

from blessed.terminal import Terminal

class UserError(BaseException):
    def __init__(self, *args):
        if args:
            self.message = args[0]

MENU = (
    ("Cheeseburger", 12.59),
    ("Mac & Cheese", 14.29),
    ("Burrito", 9.59),
    ("Club Sandwich", 13.29),
    ("Cobb Salad", 8.99),
    ("Nachos", 9.99),
    ("Milk Shake", 7.99),
    ("Soft Drink", 2.99),
    ("Coffee", 2.79),
)

Order = namedtuple("Order", ("item_no", "qty", "sign"), defaults=(None,))

def menu():
    """Print the menu"""
    print("\nMenu:\n")
    for i, (name, price) in enumerate(MENU, 1):
        print(f"{i:>3}.  {name:<20}  ${price:=7.2f}  ")

def bill(items):
    """Print the bill"""

    if not items:
        return

    print("\nYour order:\n")

    subtotal = 0

    for item_no, quantity in items.items():
        name, price = MENU[int(item_no)-1]
        cost = price * quantity
        subtotal += cost
        print(f"    {name:<20} ${price:=7.2f}  (x{quantity:>3})  => ${cost:=7.2f}")

    tax = subtotal * .08
    total = subtotal + tax

    print("\n", "Subtotal".ljust(24), f"${subtotal:=7.2f}".rjust(28), sep="")
    print("Tax".ljust(24), f"${tax:=7.2f}".rjust(28), sep="")
    print("Total".ljust(24), f"${total:=7.2f}".rjust(28), sep="")

def quantity_valid(amount):
    if amount in ("q", "quit"):
        exit()

    return amount and amount.isnumeric() and int(amount) > 0

def take_item(item_no=None, error=None):
    """Ask the user what item they want to order, validate and return the item number."""
    while True:

        sign = None

        if error:
            print(f"Error: {error.message}")

        if not item_no:
            item_no = input(f"{'Item number':>12} : ").strip()

        # to quit
        if item_no in ("quit", "q"):
            exit()

        # invalid response
        elif not item_no.isnumeric() or int(item_no)-1 <0 or int(item_no)-1 >= len(MENU):
            raise UserError("Please enter an item number or enter twice when done.")

        # return the item number
        else:
            qty = ""
            while True:
                qty = input(f"{'How many':>12} : ").strip()

                if qty.startswith("+") or qty.startswith("-"):
                    sign = qty[0]
                    qty = qty[1:]

                # quit
                if qty in ("q", "quit"):
                    exit()

                # invalid
                elif not quantity_valid(qty):
                    raise UserError("Enter a valid quantity.", item_no=item_no)

                # success
                else:
                    break

            return Order(item_no, int(qty), sign)

def add_item(items, line):
    """Add, remove or adjust an item in items dictionary."""

    # initialize the quantity
    qty = line.qty

    # if a sign was passed, adjust based on the existing quantity
    if line.sign in ("+", "-") and line.item_no in items:

        # make qty negative to subtract
        if line.sign == "-":
            qty = -qty

        qty = items[line.item_no] + qty

    # remove from items if there are none
    if qty <= 0:
        del items[line.item_no]

    # set the calculated quantity
    else:
        items[line.item_no] = qty


def order():
    """Ask the user what they want to order and return dict of {item_no: qty}"""



def main():
    items = {}
    term = Terminal()

    while True:
        print(term.clear())

        #  with term.location(0, term.height - (len(MENU) + 3)):
        with term.location(0, 5):
            menu()

            #  with term.location(0, 5):
        with term.location(0, term.height - (len(items) + 6)):
            if items:
                bill(items)

        try:
            line = take_item()
        except UserError as e:
            line = take_item(e.item_no, e)

        add_item(items, line)


main()
