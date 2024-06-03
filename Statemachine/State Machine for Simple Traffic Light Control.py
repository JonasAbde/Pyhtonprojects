class TrafficLightStateMachine:
    def __init__(self):
        self.state = 'red'

    def transition(self, event):
        if self.state == 'red' and event == 'timer_expired':
            self.state = 'green'
            print("Light changed to green.")
        elif self.state == 'green' and event == 'timer_expired':
            self.state = 'yellow'
            print("Light changed to yellow.")
        elif self.state == 'yellow' and event == 'timer_expired':
            self.state = 'red'
            print("Light changed to red.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
traffic_sm = TrafficLightStateMachine()
traffic_sm.transition('timer_expired')
traffic_sm.transition('timer_expired')
traffic_sm.transition('timer_expired')
