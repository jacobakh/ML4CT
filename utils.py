#Utility functions for our notebooks

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


def get_success_tuples(df, attribute, min_number_attacks=0):
    '''
    Input: 
    df: The dataframe of attacks that we are drawing from.
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    min_number_attacks: A cutoff value. If a category (such as a region) has less 
    than this number of attacks, it is not used. 
    
    Output: A list of tuples whose keys are the different values of attribute, 
    and values are the percentage of successful attacks in that category.
    '''
    

    attribute_vals = df[attribute].unique()
    out = {}
    for val in attribute_vals: 
        df_subset = df[df[attribute] == val]
        if(len(df_subset) <= min_number_attacks or val == 'Unknown' or val == 'Other'): 
            continue 
        success_rate = sum(df_subset['success'])/(len(df_subset))
        out[val] = success_rate
    return sorted(out.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)

def plot_attribute_success(success_tuples, attribute, use_xticks = True, save_figure=False, fig_name=None):
    '''
    See get_success_tuples. 
    
    Input: 
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    success_tuples: A list of tuples whose keys are the different values of attribute, 
    and values are the percentage of successful attacks in that category. 
    use_xticks: A boolean. The plot displays x_ticks if true.
    save_figure: An option to save the resulting plot to file.
    fig_name: A string which contains the filepath and filename if we want to save the figure.
    
    Output: A bar plot of success rates in the success_rate, by key value. 
    '''
    fig = plt.figure(figsize=(12, 6))
    y_pos = np.arange(len(success_tuples))
    plt.bar(y_pos, [x[1] for x in success_tuples])
    
    if use_xticks: 
        plt.xticks(y_pos, [x[0] for x in success_tuples])
        plt.xticks(rotation=90)

    plt.ylabel('Success Rate')
    plt.title('Success Rate of Terrorist Attacks by {}'.format(attribute))
    plt.tight_layout()

    if save_figure: 
    	plt.savefig(fig_name)

    plt.show();

def get_num_attacks_tuples(df, attribute, min_number_attacks = 0):
    '''
    Input: 
    df: The dataframe of attacks that we are drawing from.
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    min_number_attacks: A cutoff point for the minimum number of attacks. 
    Any category with fewer attacks will not be returned.
    
    Output: A list of tuples whose keys are the different values of attribute, 
    and values are the number of attacks in that category.
    '''
    attribute_vals = df[attribute].unique()
    out = {}
    for val in attribute_vals: 
        df_subset = df[df[attribute] == val]
        num_attacks = len(df_subset)
        if (num_attacks >= min_number_attacks and val != 'Unknown'):
            out[val] = num_attacks
    return sorted(out.items(), key=lambda tup: (tup[1], tup[0]), reverse=True)

def plot_count_by_attribute(num_attacks_tuples, attribute, use_xticks = True, save_figure=False, fig_name=None):
    '''
    See get_num_attacks_tuples. 
    
    Input: 
    num_attacks_tuples: A list of tuples whose keys are the different values of attribute, 
    and values are the number of attacks in that category.
    attribute: A string corresponding to an attribute we are interested in, 
    such as region or weapon type.
    use_xticks: A boolean. The plot displays x_ticks if true.
    save_figure: An option to save the resulting plot to file.
    fig_name: A string which contains the filepath and filename if we want to save the figure.

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
    plt.tight_layout()
    if save_figure: 
    	plt.savefig(fig_name)

    plt.show();