from ctypes import resize
import regex as re
import csv

with open('fb_sub.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)

    for row in reader:
        line = ', '.join(row)

endWithINC = re.compile(r"INC$")

res = ""

for item in line.split(','): 
  if endWithINC.search(item) != None:
    res = item
    print(res)
    # break;
  
with open("company.txt", "a+") as f:
  f.write(res) 
