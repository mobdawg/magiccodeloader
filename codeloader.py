# Author: Raymond Malicdem


def load_module_magic_import(name, package=None):
	try:
		fromlist = ([package,] if package is not None else [])
		module = __import__(name, fromlist=fromlist)
		return module
	except (ImportError, SyntaxError) as err:
		print(err)


def get_function(module, function_name):
	function = None
	try:
		function = getattr(module, function_name)
		if not hasattr(function, "__call__"):
			raise AttributeError()
	except AttributeError:
		function = None
	return function