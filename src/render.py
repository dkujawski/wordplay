#!/usr/bin/env python

from networkx.algorithms import simple_paths as nxasp
import networkx as nx

import matplotlib.pyplot as plt
import datetime

import dictionary 
# load up the dictionary
dictionary.load_dict(min_len=3)	


def draw_traverse(graph):
	"""
	Traverse the graph but on the way draw an image of the current traversal.
	"""
	stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%s")
	frame = 1
	iteration = 1
	
	values = nx.get_node_attributes(graph, 'value')
	pos_layout = custom_nx_layout(graph)

	results = list()
	for src_node in graph.nodes():
		for tgt_node in graph.nodes():
			if src_node is tgt_node:
				continue
			for path in nxasp.all_simple_paths(graph, src_node, tgt_node):
				char_str = ''.join([values[n] for n in path])
				if char_str:					
					results.append(char_str)
					found = False
					if dictionary.is_word(char_str):
						nc = "b"
						ec = "g"
						found = True
					else:
						nc = "r"
						ec = "r"
					# draw
					plt.clf()
					nx.draw_networkx_nodes(graph, pos_layout, node_color='w')
					nx.draw_networkx_nodes(graph, pos_layout, nodelist=path, node_color=nc)
					nx.draw_networkx_edges(graph, pos_layout, arrows=False, style='dotted', alpha=0.25)
					el = []
					idx = 1
					while idx < len(path):
						el.append((path[idx-1], path[idx]))
						idx += 1
					nx.draw_networkx_edges(graph, pos_layout, edgelist=el, edge_color=ec)
					p_labels = dict()
					for p in path[1:]:
						p_labels[p] = values[p]
					if found:
						nx.draw_networkx_labels(graph ,pos_layout, p_labels, font_size=16, font_color='y')
					else:
						nx.draw_networkx_labels(graph ,pos_layout, p_labels, font_size=16)
					nx.draw_networkx_labels(graph ,pos_layout, {path[0]:values[path[0]]}, font_size=16, font_color='w')
					# set file name
					fn = "%s_%09d.png" % (stamp, frame)
					title = "iteration: %s\n%s" % (iteration, char_str)
					plt.title(title)
					plt.axis('off')
					plt.savefig(fn)
					frame += 1
					iteration += 1

					if found:
						print fn, iteration, char_str
						for i in xrange(3):
							fn = "%s_%09d.png" % (stamp, frame)
							plt.savefig(fn)
							frame += 1
					#plt.show()
				
	return results

def custom_nx_layout(G):
	import numpy as np
	n = float(np.sqrt(len(G)) - 1)
	pos = np.asarray([[x/n, y/n] for x,y in G])
	return dict(zip(G,pos))
