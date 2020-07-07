# run: pytest -v -s


# Class Example #

# Note: The setup class and teardown class methods
# have the @classmethod decorator applied, as they
# are passed in the uninstantiated class object
# rather than a unique instance of the class.

class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True


# Module Example #

def setup_module(module):
    print("Setup Module!")
    return module

def teardown_module(module):
    print("Teardown Module!")
    return module

def setup_function(function):
    if function == test1:
        print("\nSetting up test1!")
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1!")
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True
