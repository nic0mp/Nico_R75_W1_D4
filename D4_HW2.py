class nicoPrint_string():
    
    def __init__(self):
        self.firstStr = ""
        
    def get_String(self):
        self.firstStr = input()
        
    def print_String(self):
        print(self.firstStr.upper())

firstStr = nicoPrint_string()
firstStr.get_String()
firstStr.print_String()
        
        