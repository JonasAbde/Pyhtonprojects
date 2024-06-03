class FileReadStateMachine:
    def __init__(self, filepath):
        self.filepath = filepath
        self.state = 'idle'
        self.file = None

    def transition(self, event):
        if self.state == 'idle' and event == 'start':
            self.file = open(self.filepath, 'r')
            self.state = 'reading'
            print("File opened for reading.")
        elif self.state == 'reading' and event == 'read_line':
            line = self.file.readline()
            if line:
                print(f"Read line: {line.strip()}")
            else:
                self.state = 'done'
                self.file.close()
                print("Finished reading file.")
        elif self.state == 'done' and event == 'reset':
            self.state = 'idle'
            print("State machine reset to idle state.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
file_sm = FileReadStateMachine('example.txt')
file_sm.transition('start')
file_sm.transition('read_line')
file_sm.transition('read_line')
file_sm.transition('reset')
