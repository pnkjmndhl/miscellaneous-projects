import networkx as nx
import matplotlib.pyplot as plt
import pandas

G=nx.Graph()
relationships_df = pandas.read_csv("relationships.csv")

#adjacency_list_list = [["Pankaj","Baba","Ghanashyam"], ["Pankaj","Momy", "Kamala"], ["Ghanashyam","Chhora","Pankaj"] ]

relationships_df['Relationship'] =  relationships_df.index.astype(str) +"_"+ relationships_df['Relationship']
#relationships_df['Relationship'] =  relationships_df.index.astype(str)

adjacency_list_list = []
for i in range(len(relationships_df)):
    adjacency_list_list.append(relationships_df.iloc[i].tolist())

edge_name_nodes_dict = {xlist[1]:(xlist[2],xlist[0]) for xlist in adjacency_list_list}

edge_labels = {y:x for x,y in edge_name_nodes_dict.iteritems()}
edges=[list(x) for x in edge_name_nodes_dict.values()]
G.add_edges_from(edges)
pos = nx.spring_layout(G)

plt.figure()
nx.draw(G,pos,edge_color='black',width=2,linewidths=1.5,node_size=1500,node_color='pink',alpha=0.9,labels={node:node for node in G.nodes()})
#nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels, font_color='red')
plt.show()




edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])