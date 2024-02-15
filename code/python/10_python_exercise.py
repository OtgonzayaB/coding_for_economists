# Count the number of times each country won a tender in the ted-sample.csv file.

# Task 1: Find the index position of the column "WIN_COUNTRY_CODE"

f = open("data/raw/european_commission/ted-sample.csv", "r") 

# Grab the headers
headers = f.readline().strip().split(",")

# Make sure to close the file.
f.close()

for idx, head in enumerate(headers):
  print(idx, head)

# WIN_COUNTRY_CODE at index 61


data = []

with open("data/raw/european_commission/ted-sample.csv", "r") as f:
  for line in f:
    data.append(list(line.split(",")))

print(data[0])
data = data[1:] # get rid of headers, don't need them.

# Count the number of wins by country.
d = {}
for row in data:
  country = row[61] #careful: some tenders are won by more than one country
  countries = country.split('---') # Returns a list of winning countries.
  for winning_country in countries:
    if not winning_country in d:
     d[winning_country] = 0
    d[winning_country] += 1

print(d)
 
    



  




