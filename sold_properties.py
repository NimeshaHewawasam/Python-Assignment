import csv

"""
1. open and read the give csv file
2. get average price from the csv
3. check each property that less than the average price 
4. write new csv file by adding selected less average price properties
"""

# Read CSV File 
def read_csv_file(name):
    with open (name,"r") as file:
        csv_data = csv.reader(file)
        
        header = next(csv_data)

        data = []
        for row in csv_data:
            data.append(row)

        return (header, data)

# Get Colum Index
def get_colum_index(headers, colum):
    header_index = None
    for header in headers:
        if header.lower() == colum:
            header_index = headers.index(header)
            break
    return header_index

# Get Avarage Price
def get_average_price(header, data, colum_index):
    total_price = 0
    for x in data:
        total_price = total_price + int(x[colum_index])
    total_row_count = len(data)
    return total_price / total_row_count

# Filter CSV Data Before Write to new CSV 
# Filter Logic : check each property that less than the average price 
def filter_csv_data(header, data):
    price_colum_index = get_colum_index(header, 'price')
    avarage_price = get_average_price(header, data, price_colum_index)

    filter_data = []
    for x in data:
        if int(x[price_colum_index]) < avarage_price:
            filter_data.append(x)
    return filter_data

# Write New CSV File
def write_csv_file(filename, header, data):
    with open(filename, 'w') as file:
        
        for header in header:
            file.write(str(header)+', ')
        file.write('\n')

        for row in data:
            for x in row:
                file.write(str(x)+', ')
            file.write('\n')

# CSV File Names
csv_file_name = 'sales_data.csv'
filter_csv_file_name = 'filter_sales_data.csv'

# Start Process Here
csv_header, csv_data = read_csv_file(csv_file_name)
filter_csv_data = filter_csv_data(csv_header, csv_data)
write_csv_file(filter_csv_file_name, csv_header, filter_csv_data)

# Print Success Message
print('Sales Data Filter Success Create a New File as ', filter_csv_file_name)

