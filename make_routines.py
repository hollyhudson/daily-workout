# Reads a plaintext file of workout routines
# and splits them into an html file for each day of the week
# by Holly Hudson
#
# Reads from two files:
# rep_guide.txt:  Primes the dictionary with a definition for each exercise
# level
# routines.txt:  creates the daily routines for the .html file output

idnum = 0

# here's where we get the plaintext listing of all the routines for the week:
routines = open('routines.txt', 'r')
rep_guide = open('rep_guide.txt','r')
round_counter = 0
current_file = None
reps = {}


for line in rep_guide:
	# if we hit a blank line, skip it
	if line == "\n":
		continue
	# add a new definition to the dictionary
	current_pair = line.split(':')
	reps[current_pair[0]] = current_pair[1]

for line in routines:
	if line == "END\n":
		break

	# We're processing daily routines 
	# new .html file
        if line == "===\n":  # delineates different daily routines in .txt file
		if round_counter != 0:
			current_file.write("</form>\n")
			current_file.write("</body>\n")
			current_file.write("</html>\n")
                new_file_name = routines.next().rstrip('\n')
                current_file = open(new_file_name, 'w')
		current_file.write("<html>\n")
		current_file.write("<head>\n")
		current_file.write(" 	<title>Today's Routine</title>\n")
		current_file.write(" 	<link href=\"Site.css\" rel=\"stylesheet\">\n")
		current_file.write(" 	<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>\n")
		current_file.write(" 	<script>\n")
		current_file.write(" 	$(document).ready(function(){\n")
		current_file.write(" 		$(\".item\").click(function(){\n")
		current_file.write(" 			$(this).hide()\n")
		current_file.write(" 		});\n")
		current_file.write(" 	});\n")
		current_file.write(" 	</script>\n")
		current_file.write("</head>\n")
		current_file.write("<body>\n")
		current_file.write("<form>\n")
		
		# Write the heading, ie the exercise set title
		current_file.write("<h1>%s</h1>\n" % routines.next().rstrip('\n'))
		current_file.write("<p class=\"round%d\">\n" % round_counter)
		round_counter = (round_counter + 1) % 5
		continue

	# contents of one .html file
	idnum += 1  # idnum is needed for checkboxes to work
	if line == "\n":  # we're at a round boundary
		# put an html newline/space, but with no checkbox
		current_file.write("<br><br>\n") 
		# Set look and feel for this round
		current_file.write("</p>\n")
		current_file.write("<p class=\"round%d\">\n" % round_counter)
		# we don't want to run out of colors
		# better to loop back around
		round_counter = (round_counter + 1) % 5
		continue
	
	# write an actual workout item in the .html file
	current_file.write(" 	<a class=\"item\">")
       	current_file.write(reps[line.rstrip('\n')])
	current_file.write(" 	</a><br><br>\n")
	

current_file.write("</p>\n")
current_file.write("</form>\n")
current_file.write("</html>\n")

