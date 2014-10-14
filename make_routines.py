idnum = 0
first_time_through = True
colors = ["#000000", "#6f7072", "#f27f20"]
coloriterator = 0
color = colors[coloriterator]
routines = open('routines.txt', 'r')
current_file = None

for line in routines:
        if line == "===\n":
		if not first_time_through:
			current_file.write("</form>\n")
			current_file.write("</html>\n")
                new_file_name = routines.next().rstrip('\n')
                current_file = open(new_file_name, 'w')
		current_file.write("<html>\n")
		current_file.write("<form>\n")
		first_time_through = False
                continue
	idnum += 1
	current_file.write("<input type=\"checkbox\" id=%d>" % idnum)
	current_file.write("<label style=\"color:%s;\" for=%d>" % (colors[coloriterator], idnum))
        current_file.write(line)
	current_file.write("<br><br>\n")

current_file.write("</form>")
current_file.write("</html>")

