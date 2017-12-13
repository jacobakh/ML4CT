#Utility functions for our notebooks

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


def get_num_attacks_tuples(attribute, min_number_attacks = 0):
    '''
    Input: 
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    min_number_attacks: A cutoff point for the minimum number of attacks. 
    Any category with fewer attacks will not be returned.
    
    Output: A list of tuples whose keys are the different values of attribute, 
    and values are the number of attacks in that category.
    '''
    attribute_vals = raw[attribute].unique()
    out = {}
    for val in attribute_vals: 
        df_subset = raw[raw[attribute] == val]
        num_attacks = len(df_subset)
        if (num_attacks >= min_number_attacks and val != 'Unknown'):
            out[val] = num_attacks
    return sorted(out.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)

def plot_count_by_attribute(num_attacks_tuples, attribute, use_xticks = True):
    '''
    See get_num_attacks_tuples. 
    
    Input: 
    num_attacks_tuples: A list of tuples whose keys are the different values of attribute, 
    and values are the number of attacks in that category.
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    use_xticks: A boolean. The plot displays x_ticks if true.
    
    Output: A bar plot of number of attacks in the num_attacks_tuples, by key value. 
    '''
    plt.figure(figsize=(12, 6))

    y_pos = np.arange(len(num_attacks_tuples))
    plt.bar(y_pos, [x[1] for x in num_attacks_tuples], color='red')
    
    if use_xticks:
        plt.xticks(y_pos, [x[0] for x in num_attacks_tuples])
        plt.xticks(rotation=90)

    plt.ylabel('Number of Attacks')
    plt.title('Number of Terrorist Attacks by {}'.format(attribute))
    
    plt.show();