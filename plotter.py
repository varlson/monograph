import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from os import makedirs

rc('text', usetex=True)
font = {'family' : 'normal',
         'weight' : 'bold',
         'size'   : 7}

rc('font', **font)
params = {'legend.fontsize': 7}
plt.rcParams.update(params)


months = ['Jan', 'Fev', 'Mar', 'Mai', 'Jun', 'Jul','Ago', 'Set', 'Out', 'Nov', 'dez']



# colors   = ['green', 'blue','Gray','Magenta', 'Purple', 'red', ] 
colors   = ['SlateBlue', 'DarkSlateBlue','RebeccaPurple','MediumOrchid', 'SteelBlue', 'DarkTurquoise', ] 
metric_lst = ['degree', 'strength', 'betweenness', 'betweenness_w', 'closeness', 'closeness_w']
lbls = [r'$k$', r'$s$', r'$b$', r'$b_w$', r'$c$', r'$c_w$', ]


def uniques(lst):
    uniqlst = []

    for item in lst:
        if item not in uniqlst:
            uniqlst.append(item)
    return uniqlst


def plot(x_axis, y_axis, labels, out_path, out_fileName, title):

    makedirs(out_path, exist_ok=True)

    markers = ['.', '^', '*', 7, 'p', 8]

    uniqueDates = uniques(x_axis)
    teste = []
    for index, date in enumerate(uniqueDates):
        if index % 3 == 0:
            teste.append(date)
        else:
            teste.append(' ')
    
 
            
    plt.figure(figsize=(6, 3))

    for index, metric_item in enumerate(labels):
        line ='aa'

        if (metric_lst[index][-1] == 'w') or (metric_lst[index][-1] == 'h'):
            plt.plot(x_axis, y_axis[index], color=colors[index], label=labels[index], marker=markers[5], lw=0.6, linestyle="--", markersize=0.8)
        else:
            plt.plot(x_axis, y_axis[index], color=colors[index], label=labels[index], marker=markers[0], lw=0.6, linestyle="-", markersize=0.8)

    plt.ylim([-0.05, 1.05])
    plt.xticks([])

    plt.xlim([0.5, 1.05])
    # plt.xlim([x_axis[1], x_axis[-1]])
    plt.legend(ncol=2, fontsize=7, loc='lower right')

    param = {'family': 'sans-serif', 'size': 5, 'rotation': 65}
    # plt.xticks(x_axis, labels=x_axis, fontdict=param)  # Substituir ax.set_xticklabels por plt.xticks
    print(uniqueDates)

    plt.xticks(uniqueDates,  rotation=65, ha='right', fontsize=5)  


    plt.xlabel('Datas aa/mm/dd')
    perc = r' correspond\^{e}ncia'
    plt.ylabel(f"Taxa de {perc} ")
    plt.title(title)

    plt.tight_layout()
    plt.savefig(f'{out_path}/{out_fileName}.png', dpi=350)
   
