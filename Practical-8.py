fh = open('Practical-8.txt', 'w')
a=[28,6,30,46,1,54,5,31,45,26,4,56,-5,-28,25]
a.sort()
fh.write('Ascending Order: ' + ', '.join(map(str, a)) + '\n')
a.sort(reverse=True)
fh.write('Descending Order: ' + ', '.join(map(str, a)) + '\n')
fh.close()
