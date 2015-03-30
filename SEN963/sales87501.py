# Name: Shashi Kanth Kangayam
# Student ID: 87501

# Description of the assignment:
# Read the individual sales information from SALES.TXT and write the aggregated
# information to a new file TOTALS.TXT

def main():
    sales=open('SALES.TXT')
    totals=open('TOTALS.TXT','w')

    totals.write("{0:^16}".format("Name")+"{0:>12}\n".format("Total"))
    grandTotal=0
    for line in sales:
        list = line.split()
        total = int(list[1])+ int(list[2])+int(list[3])+int(list[4])
        totals.write("{0:>16}".format(list[0])+"{0:12}\n".format(total))
        grandTotal += total
    totals.write("Grand Total:{0:15}\n".format(grandTotal))
    totals.close()

main()