# import csv functionality
import csv


html = "<body>"

# opening in a way that will close the file when we are done
with open("recipes.csv", "rU") as csvfile:
	# reading file
	reader = csv.reader(csvfile)

	rownum = 0
	for row in reader:
		# Save header row.
		if rownum == 0:
			header = row
		if rownum == 1:
			colnum = 0
			for col in row:
				print '%s: %s' % (header[colnum], col)
				colnum += 1




		#else:
		#	colnum = 0
		#	for col in row:
		#		print '%s: %s' % (header[colnum], col)
		#		colnum += 1

		rownum += 1


		html = html + "div"
		#for data in row:
		#	html = html + "<td>" + data + "</td>"


		html = html +"</div>\n"




html = html + "</body>"