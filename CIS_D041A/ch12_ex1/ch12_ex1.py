# ch12_ex1
# Uyen Nguyen
# 06/12/22
# Python 3.10.0
# Description:
'''
Read the CSV file 'order.csv' using 'assert' for testing
'''

import csv

# Read the file order.csv and reformat data into dictionary
def read_order(input_file):
    order_dict = {}
    total_order_dict = {}
    
    with open(input_file) as infile:
        reader = csv.reader(infile)
        # Create a dictionary (order_dict) that the key is the burger number, and the value is a list of the quantities.
        for line in reader:
            value_list = []
            for num in range(1, len(line)):
               value_list.append(int(line[num]))
            order_dict[line[0]] = value_list

        # Create a dictionary (total_order_dict) that the key is the burger number, and the value is the total of the quantities for that burger
        for key in order_dict:
            value_sum = sum(order_dict[key])
            total_order_dict[key] = value_sum

    return total_order_dict

def test_sum():
    expected_result_ototal_order_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}
    assert actual_result_ototal_order_dict['1'] == expected_result_ototal_order_dict['1'], 'The actual result is not the same as expected result for the order number 1!'
    assert actual_result_ototal_order_dict['2'] == expected_result_ototal_order_dict['2'], 'The actual result is not the same as expected result for the order number 2!'
    assert actual_result_ototal_order_dict['3'] == expected_result_ototal_order_dict['3'], 'The actual result is not the same as expected result for the order number 3!'
    assert actual_result_ototal_order_dict['4'] == expected_result_ototal_order_dict['4'], 'The actual result is not the same as expected result for the order number 4!'
    assert actual_result_ototal_order_dict['5'] == expected_result_ototal_order_dict['5'], 'The actual result is not the same as expected result for the order number 5!'

# Write this dictionary in a csv file which the first is the key (number of the burger ) and the next number after comma is the value ( the total of the quantities for that burger)
def write_order_csv(actual_result_ototal_order_dict, outputFile):
    with open(outputFile, 'w') as outfile:
        for key, value in actual_result_ototal_order_dict.items():
            writer = csv.writer(outfile)
            writer.writerow([key, value])

if __name__ == '__main__':
    actual_result_ototal_order_dict = read_order('ch12_ex1/order.csv')
    test_sum()
    print('Everything passed')
    write_order_csv(actual_result_ototal_order_dict, 'outputfile.csv')

'''
1,91
2,100
3,32
4,62
5,64
'''
