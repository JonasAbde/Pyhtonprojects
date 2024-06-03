class ListProcessingStateMachine:
    def __init__(self, items):
        self.items = items
        self.state = 'idle'
        self.index = 0

    def transition(self, event):
        if self.state == 'idle' and event == 'start':
            self.state = 'processing'
            print("Started processing list.")
        elif self.state == 'processing' and event == 'process_next':
            if self.index < len(self.items):
                print(f"Processing item: {self.items[self.index]}")
                self.index += 1
            else:
                self.state = 'done'
                print("Finished processing list.")
        elif self.state == 'done' and event == 'reset':
            self.state = 'idle'
            self.index = 0
            print("State machine reset to idle state.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
list_sm = ListProcessingStateMachine([1, 2, 3, 4, 5])
list_sm.transition('start')
list_sm.transition('process_next')
list_sm.transition('process_next')
list_sm.transition('reset')
