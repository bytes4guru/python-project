class PythonProjects():

    def __init__(self, message):
        self.message = message
        self.say_hello()

    def say_hello(self):
        print(self.message)


# Create an instance of the above class:
inst = PythonProjects("Hello, world!")

# Call the above method using the instance:
inst.say_hello()


# ==========
#
# If the module gets imported, everything that 
# follows if __name__ == "__main__": code will 
# not get executed. If it's run by itself, it 
# will run, and this is a great way to test, 
# or self-test each module.
#
#  ==========

if __name__ == "__main__":
    print("Hi!")