# -*- encoding: utf-8 -*-
#
# Social Network Analysis of Git, Hg, SVN, GitHub, BitBucket repositories
#
# Author: Massimo Menichinelli
# Homepage: http://www.openp2pdesign.org
# License: LGPL v.3
#


import networkx as nx
import datetime


def save_graph(graph, filename):
    """
    Transform date on a graph to string and save as a graphml
    """
    for u, v, key, attr in graph.edges(data=True, keys=True):
        if type(attr["start"]) is datetime.datetime:
            attr["start"] = attr["start"].strftime('%Y/%m/%d-%H:%M:%S')
        attr["endopen"] = str(attr["endopen"])

    nx.write_graphml(graph, filename)

    return

if __name__ == "__main__":
    pass
