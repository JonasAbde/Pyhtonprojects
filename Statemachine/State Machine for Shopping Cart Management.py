class ShoppingCartStateMachine:
    def __init__(self):
        self.state = 'empty'
        self.items = []

    def transition(self, event, item=None):
        if self.state == 'empty' and event == 'add_item':
            self.items.append(item)
            self.state = 'active'
            print(f"Added item: {item}. Cart is now active.")
        elif self.state == 'active' and event == 'add_item':
            self.items.append(item)
            print(f"Added item: {item}.")
        elif self.state == 'active' and event == 'remove_item':
            if item in self.items:
                self.items.remove(item)
                print(f"Removed item: {item}.")
                if not self.items:
                    self.state = 'empty'
                    print("Cart is now empty.")
            else:
                print(f"Item {item} not in cart.")
        elif self.state == 'active' and event == 'checkout':
            self.state = 'checked_out'
            print(f"Checked out with items: {self.items}")
        elif self.state == 'checked_out' and event == 'reset':
            self.state = 'empty'
            self.items = []
            print("Cart reset to empty state.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
cart_sm = ShoppingCartStateMachine()
cart_sm.transition('add_item', item='Apple')
cart_sm.transition('add_item', item='Banana')
cart_sm.transition('remove_item', item='Apple')
cart_sm.transition('checkout')
cart_sm.transition('reset')
