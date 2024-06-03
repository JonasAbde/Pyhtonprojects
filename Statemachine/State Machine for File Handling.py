class FileHandlerStateMachine:
    def __init__(self, filepath):
        self.filepath = filepath
        self.state = 'closed'
        self.file = None

    def transition(self, event, mode=None, data=None):
        if self.state == 'closed' and event == 'open':
            self.file = open(self.filepath, mode)
            self.state = 'opened'
            print(f"File opened in {mode} mode.")
        elif self.state == 'opened' and event == 'read':
            content = self.file.read()
            print(f"Read content: {content}")
        elif self.state == 'opened' and event == 'write':
            self.file.write(data)
            print(f"Wrote data: {data}")
        elif self.state == 'opened' and event == 'close':
            self.file.close()
            self.state = 'closed'
            print("File closed.")
        else:
            print(f"Invalid transition from {self.state} on {event} event.")

# Example usage
file_handler_sm = FileHandlerStateMachine('testfile.txt')
file_handler_sm.transition('open', mode='w')
file_handler_sm.transition('write', data='Hello, World!')
file_handler_sm.transition('close')
file_handler_sm.transition('open', mode='r')
file_handler_sm.transition('read')
file_handler_sm.transition('close')
