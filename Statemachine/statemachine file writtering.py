class FileWriteStateMachine:
    def __init__(self, filepath):
        self.filepath = filepath
        self.state = 'idle'
        self.file = None

    def transition(self, event, line=None):
        if self.state == 'idle' and event == 'start':
            self.file = open(self.filepath, 'w')
            self.state = 'writing'
            print("File opened for writing.")
        elif self.state == 'writing' and event == 'write_line':
            if line:
                self.file.write(line + '\n')
                print(f"Wrote line: {line}")
            else:
                print("No line provided to write.")
        elif self.state == 'writing' and event == 'close':
            self.file.close()
            self.state = 'done'
            print("File closed after writing.")
        elif self.state == 'done' and event == 'reset':
            self.state = 'idle'
            print("State machine reset to idle state.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
file_write_sm = FileWriteStateMachine('output.txt')
file_write_sm.transition('start')
file_write_sm.transition('write_line', 'Hello, World!')
file_write_sm.transition('close')
file_write_sm.transition('reset')
