# Example of unittest.mock

def test_Foo():
	bar = Mock()
	bar_func(bar)
	bar.assert_called_once()

def test_Foo2():
	# Specifies the interface that the Mock object is implementing. 
	bar = Mock(spec = spec_class)
	# Specifies a function that should be called when the Mock is called. 
	bar2 = Mock(side_effect = bar_func)
	# Specifies the value that should be returned when the Mock object is called. 
	bar3 = Mock(return_value = 1)

# MonkeyPatch Example
def call_it():
	print("Hello, world!")

def test_patch(monkeypatch):
	monkeypatch(call_it, Mock())
	call_it()
	call_it.assert_called_once()