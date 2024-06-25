# Author: Raymond Malicdem


from codeloader import load_module_magic_import, get_function
import argparse 


def main():
	args_parser = argparse.ArgumentParser()			
	args_parser.add_argument("valueone", type=str, help="comma separated value of items")
	args_parser.add_argument("valuetwo", type=int, help="single integer digit")
	args = args_parser.parse_args()

	mod1 = load_module_magic_import("loadables.loadable", "loadables")
	mod2 = load_module_magic_import("loadable",)
	mods = [mod1, mod2]
	func_names = ["most_number_element", "triangle"]
	for m in mods:
		for f in func_names:
			loaded_func = get_function(m, f)
			if loaded_func is not None:
				res = None
				if f == func_names[0]:
					res = loaded_func(args.valueone.split(","))
					print("item with the most number of occurrence:", res)
				elif f == func_names[1]:
					res = loaded_func(args.valuetwo)
					print(f"triangle shaped asterisk based on arg {args.valuetwo}:")
					for ast in res:
						print(ast)
				break


if __name__ == "__main__":
	main()

