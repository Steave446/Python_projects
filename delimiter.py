import csv

reader = csv.reader(open("contacts.csv", "rU"), delimiter=',')
writer = csv.writer(open("contacts_output.txt", 'w'), delimiter=',,')
writer.writerows(reader)

print("delimiter successfully changed.")