idnum = 0
first_time_through = True
colors = [
	"#cf6bec", "#6f7072", "#f27f20",
	"#00a2ff", "#cf25c8", "#07eaf2",
	"#2877dc", "#2ae6b7", "#2aafe6"]
coloriterator = 0
#color = colors[coloriterator]

# here's where we get the plaintext listing of all the routines for the week:
routines = open('routines.txt', 'r')
current_file = None

for line in routines:
        if line == "===\n":  # delineates different days in the plaintext file
		if not first_time_through:
			current_file.write("</form>\n")
			current_file.write("</html>\n")
                new_file_name = routines.next().rstrip('\n')
                current_file = open(new_file_name, 'w')
		current_file.write("<html>\n")
		current_file.write("<form>\n")
		first_time_through = False
                continue

	idnum += 1  # idnum is needed for checkboxes to work
	if line == "\n":
		# we don't want to run out of colors
		# better to loop back around
		coloriterator = (coloriterator + 1) % 9
		current_file.write("<br><br>\n") # put a space w/out checkbox
		continue
	
	current_file.write("<input type=\"checkbox\" id=%d>" % idnum)
	current_file.write("<label style=\"color:%s;\" for=%d>" % (colors[coloriterator], idnum))
        current_file.write(line)
	current_file.write("<br><br>\n")

current_file.write("</form>")
current_file.write("</html>")

