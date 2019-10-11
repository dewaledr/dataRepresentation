from bs4 import BeautifulSoup
import csv

with open("../week02/lab02.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# Read the entire file
# print(soup.prettify())  
# Extract the first <tr> from the file
# print(soup.tr)
employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


# Extract all the first <tr> from the file
rows = soup.findAll("tr")
# for row in rows:
#     print("------------")
#     print(row)
# Get the contents of the td for each row
# for row in rows:
#     cols = row.findAll("td")
#     for col in cols:
#         print(col.text)    

# # Modify to get text in the columns stored in a list 
# # and then write into a csv file
# for row in rows:
#     cols = row.findAll("td")
#     dataList = []
#     for col in cols:
#         dataList.append(col.text)
#     employee_writer.writerow(dataList)    
# employee_file.close()

# dataList = []
for row in rows:
    cols = row.findAll("td")
    dataList = []
    for col in cols:
        dataList.append(col.text)
    employee_writer.writerow(dataList[:4])    
employee_file.close()


'''
for row in soup.findAll('table')[0].tbody.findAll('tr'):
    first_column = row.findAll('th')[0].contents
    third_column = row.findAll('td')[2].contents
    print first_column, third_column
'''
