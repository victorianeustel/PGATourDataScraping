from helpers.pga_data_calls import *
import json

def write_sample_data(sample_data_name: str, value: str):
    with open('sample_data/' + sample_data_name + '.json', 'w', newline='\n') as file:
        json.dump(value, file)
        
