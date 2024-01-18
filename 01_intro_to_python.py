# Exercise: Indexing and slicing

url = 'https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv'
# Use indexing, slicing to fill in the following output.
# Copy/ paste not allowed

len('ted-sample.csv')
file_name = url[-14:]
print(file_name) # 'ted-sample.csv'



protcol = url[0:5]
print(protcol) # 'https'

len(github.com)
host_name = url[8:18]
print(host_name) # 'github.com'


#Use string composition to construct http://github.com/ted-sample.csv

output = protcol + '://' + host_name + "/" + file_name
print(output) # 'http://github.com/ted-sample.csv'


