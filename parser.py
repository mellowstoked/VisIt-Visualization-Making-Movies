movements = open('view_3D_atts.py', 'r+')
save_window_code = open('save_window.py', 'r')
save_windows = open('save_all_windows.py', 'w')

for line in movements:
	# Write string to save all windows
	save_windows.write(line)
	strings = line.split()

	if strings == []:
		continue
	elif strings[0] == '#' and strings[1] == 'End':
		# this is where we want to insert the save window code
		save_window_code.seek(0,0)
		for w in save_window_code:
			save_windows.writelines(w)

movements.close()
save_window_code.close()
save_windows.close()

