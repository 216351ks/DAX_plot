# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:49:29 2021

@author: Hubert
"""

import pandas as pd 
import matplotlib.pyplot as plt

tab = pd.read_csv("dax.csv" ''', use_columns = ['Data','Otwarcie','Zamkniecie']''')

def select_rows():
    
    for row in tab.readlines(): 
        array = row.split(",")
        selected_rows = (row['Otwarcie'], row['Data'])
        return selected_rows
    
def draw_plot():
    
    x = []
    y= []
    
    for line in tab:
        x.append(int(line[0]))
        y.append(int(line[0]))
        
    plt.plot(x,y, label = 'Dax_price')
    plt.xlabel('Cena')
    plt.ylabel('Data')
    
    plt.title('Cena Daxa')
    plt.legend()
    
    plt.show()
    
    
print(select_rows())
print(draw_plot())

