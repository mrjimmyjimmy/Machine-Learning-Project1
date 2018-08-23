# coding=utf-8

import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd


def store_node(filename):
    f = open(filename)
    # read all the lines
    lines = f.readlines()

    node = []
    for i in range(0,lines.__len__(),1):

        list = []
        for word in lines[i].split():

            list.append(word);

        # print(list)
        node.append(list)

    # print(node)
    return node


def form_graph(node):
    g = nx.Graph()

    for i in range(len(node)):
        list = node[i]
        # print(list)
        g.add_node(int(list[0]))
        for i in range(len(list) -1 ):

            g.add_edge(int(list[0]),int(list[i + 1]))

        # for test use
        # print('now we have nodes : ' )
        # print(nx.nodes(g))
        # print('now we have edges : ' )
        # print(nx.edges(g))

    return g


def predict_jaca():

    G = nx.complete_graph(5)
    preds = nx.jaccard_coefficient(G, [(0, 1), (2, 3)])
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))


def try_predict_jaca(G):
    preds = nx.jaccard_coefficient(G, (1,3))
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))


def jaca_predict(graph, a,b):
    number_x = len(list(nx.neighbors(graph, a)))
    number_y = len(list(nx.neighbors(graph, b)))
    common = len(list(nx.common_neighbors(graph, a, b)))

    score = common/(number_x + number_y - common)
    return score



if __name__ == '__main__':
    node = store_node('train_test1.txt')
    graph = form_graph(node)

    print(jaca_predict(graph,2,4))










