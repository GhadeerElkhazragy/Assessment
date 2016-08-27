import csv
f = open('sample.csv')
csv_f = csv.reader(f)
committees = [line.strip() for line in open('sample.csv')]
l1 = [i.split(',')[1] for i in committees]
print "Total Number of Applicants =", len(l1)
print "IT:", l1.count('IT')
print "HR:", l1.count('HR')
print "PR:", l1.count('PR')
print "FR:", l1.count('FR')
print "L&R:", l1.count('L&R')
print "ADV:", l1.count('ADV')
l2 = [g.split(',')[2] for g in open('sample.csv')]
l3 = [y.split('\n')[0] for y in l2]
print "\n2017:", l3.count('2017')
print "2018:", l3.count('2018')
print "2019:", l3.count('2019')
print "2020:", l3.count('2020')
print "2021:", l3.count('2021')
doc = list(open('sample.csv'))
while True:
    f.seek(0, 0)
    preference = raw_input('\nPlease select a preference:')
    year = raw_input('\nPlease select a Graduation Year:')
    counter = 0
    for line in csv_f:
        if line[1] == preference and line[2] == year:
            counter += 1
    print "Number of applicants is:", counter


