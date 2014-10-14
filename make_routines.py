idnum = 0
colors = ["#000000", "#6f7072", "#f27f20"]
coloriterator = 0
color = colors[coloriterator]
routines = open('routines.txt', 'r')
current_file = None

for line in routines:
        if line == "===\n":
                new_file_name = routines.next().rstrip('\n')
                current_file = open(new_file_name, 'w')
		current_file.write("<html>")
		current_file.write("<form>")

        #elif line == "*.html\n":
                continue
	idnum += 1
	print "<input type=\"checkbox\" id=%d>" % idnum
	print "<label style=\"color:%s;\" for=%d>" % (colors[coloriterator], idnum)
        current_file.write(line)

print "</form>"
print "</html>"

