# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

input_currency = input('Enter a name: ')
tab = pd.read_csv(input_currency + ".csv", usecols=['Otwarcie', 'Data'], delimiter=';', header=0)


# TODO: csv for all currency, import functions to Flask
def select_rows(tab):
    global selected_rows
    for index, row in tab.iterrows():
        selected_rows = (row['Otwarcie'], row['Data'])
    return selected_rows


def draw_plot(tab, name):
    x = []
    y = []

    plt.figure(figsize=(16, 15))

    for index, line in tab.iterrows():
        x.append(line[0])
        y.append(line[1])

    plt.plot(x[0::20], y[0::20], label=name + ' chart')
    plt.xlabel('Data')
    plt.ylabel('Cena')

    plt.title('Cena ' + name)
    plt.legend()
    plt.savefig(name + '.png')
    plt.show()


print(select_rows(tab))
print(draw_plot(tab, input_currency))
