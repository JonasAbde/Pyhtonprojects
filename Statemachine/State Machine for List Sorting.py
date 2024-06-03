class ListSortingStateMachine:
    def __init__(self, items):
        self.items = items
        self.state = 'idle'

    def transition(self, event):
        if self.state == 'idle' and event == 'start':
            self.state = 'sorting'
            print("Started sorting list.")
        elif self.state == 'sorting' and event == 'sort':
            self.items.sort()
            self.state = 'done'
            print(f"Sorted list: {self.items}")
        elif self.state == 'done' and event == 'reset':
            self.state = 'idle'
            print("State machine reset to idle state.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
sort_sm = ListSortingStateMachine([3, 1, 4, 1, 5, 9])
sort_sm.transition('start')
sort_sm.transition('sort')
sort_sm.transition('reset')
