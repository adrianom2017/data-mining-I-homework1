import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import distance_fn as d

a = np.array([1,2,3])
b = np.array([2,3,4])

# print(d.hamming_dist(a,b))
# print(d.manhattan_dist(a,b))
# print(d.euclidean_dist(a,b))
# print(d.minkowski_dist(a,b,3))
# print(d.chebyshev_dist(a,b))

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

i = 1
plt.figure(figsize=(10,5))
p = sns.catplot(x="Pair of newsgroups", y = "Score", hue = "Compared", kind="point", data = data.loc[data['Metric']== metrics[i]], legend_out=False)
plt.title(metrics[i])
plt.show()
# p.savefig(metric + '.png')

