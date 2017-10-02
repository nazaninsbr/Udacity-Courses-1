li = []
with open('/Users/User/Desktop/uni/Udacity-Courses/Introduction to Python Programming/files and modules/file.txt','r') as f:
	for line in f:
		line_data = line.split(',')
		li.append(line_data)
print(li)