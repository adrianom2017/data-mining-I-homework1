import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import distance_fn as d

a = np.array([1,2,3])
b = np.array([2,3,4])

df = pd.read_csv('./results/output_distances.txt', sep='\t')

x = [i.split(':') for i in df['Pair of newsgroups']]
x = [item for sublist in x for item in sublist]

cat = []
for i in x:
    if i not in cat:
        cat.append(i)

for idx in range(len(cat)):
    tmp = df.loc[df['Pair of newsgroups'].str.contains(cat[idx])].copy()
    row_names = [i.replace(':', '').replace(cat[idx], '') for i in tmp['Pair of newsgroups']]
    row_names[row_names.index('')] = cat[idx]
    tmp['Pair of newsgroups'] = row_names
    tmp = pd.melt(tmp, id_vars=['Pair of newsgroups'], value_name= 'Score', var_name= 'Metric' )
    tmp.insert(0, 'Compared', cat[idx])
    if idx == 0:
        data = tmp.copy()
    else:
        data = data.append(tmp)

metrics = []
for i in data['Metric']:
    if i not in metrics:
        metrics.append(i)

for i in range(len(metrics)):
    fig, ax = plt.subplots(1,1,figsize=(10,5))
    sns.catplot(ax = ax, x="Pair of newsgroups", y = "Score", hue = "Compared", kind="point", data = data.loc[data['Metric']== metrics[i]], legend_out=True)
    # ax.legend(loc = 'upper right')
    fig.suptitle(metrics[i])
    fig.savefig('./img/'+ metrics[i] + '.png')

