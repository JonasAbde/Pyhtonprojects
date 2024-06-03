class UserAuthStateMachine:
    def __init__(self):
        self.state = 'logged_out'
        self.attempts = 0

    def transition(self, event, success=False):
        if self.state == 'logged_out' and event == 'login_attempt':
            if success:
                self.state = 'logged_in'
                self.attempts = 0
                print("User logged in.")
            else:
                self.attempts += 1
                print(f"Login failed. Attempt {self.attempts}.")
                if self.attempts >= 3:
                    self.state = 'locked'
                    print("Account locked due to too many failed attempts.")
        elif self.state == 'logged_in' and event == 'logout':
            self.state = 'logged_out'
            print("User logged out.")
        elif self.state == 'locked' and event == 'reset':
            self.state = 'logged_out'
            self.attempts = 0
            print("Account reset. User can try logging in again.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
auth_sm = UserAuthStateMachine()
auth_sm.transition('login_attempt', success=False)
auth_sm.transition('login_attempt', success=False)
auth_sm.transition('login_attempt', success=False)
auth_sm.transition('reset')
auth_sm.transition('login_attempt', success=True)
auth_sm.transition('logout')
