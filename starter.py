import lang

print("Lang Script Runner")
print(".lang ending will be added automatically.")
file = input("Filename: ")

if file == None or file.strip() == None or file.startswith(" ") or file == "":
	print("Invalid filename")
	quit()
else:
	#result, error = lang.run('<shell>', f'run("{file}")')
	result, error = lang.run('<shell>', f'run("{file}.lang")')

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

			