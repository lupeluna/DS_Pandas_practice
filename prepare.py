import pandas as pd
import numpy as np



# function for get_city from an address

def get_city(address):
    return address.split(',')[1]

# This function can be used within:
# add_data['Column'] = all_data['Purchase Address'].apply(lambda x: get_city(x))




# function to get state from address

def get_state(address):
    return address.split(',')[2]