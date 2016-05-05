#!/usr/bin/python
import sys
from macros import macro_list

def macro_list_title():
	print "\n== MACROS ==\n"

def search_macro(search_text):
	macro_list_title()
	for macro in macro_list.keys():
		if search_text in macro:
			print macro
	
def lazy_macros():
	if len(sys.argv) == 1:
		macro_list_title()
		macro_names = macro_list.keys()
		macro_names.sort()

		for macro in macro_names:
			print macro
			
		print "\nYou also can use the \"search\" command if you don't remember well the name of the macro!"
	elif len(sys.argv) == 2:	
		print "\nPut a name to it!"
	else:
		macro_type = sys.argv[1]
		object_name = sys.argv[2]
		
		if macro_type == "search":
			search_macro(object_name)
		else:
			print macro_list[macro_type] % object_name
	
lazy_macros()	