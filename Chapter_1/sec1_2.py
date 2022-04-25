"""
ID: jpgalla1
LANG: PYTHON3
TASK: ride
"""
rideIn = open ('ride.in', 'r')
#fout = open ('test.out', 'w')
# logic for program:
# read input of file
# split into line by line
# Convert to numbers
# product of each line of numbers
# length of list /2
# compare prod of line 2n == prod line 2n+1
# if == true then "GO"
# else: "Stay"
x,y = map(int, fin.readline().split())
sum = x+y
fout.write (str(sum) + '\n')
fout.close()
