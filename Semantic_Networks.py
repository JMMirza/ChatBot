from py2neo import Node, Graph, Relationship
from nlp_start import create_tags
from ml import extractedName
password = "123"
graph = Graph(password=password)


def Semantics(sentence):
    nodes = []
    relation = None
    tags_list = create_tags(sentence)
    for tag in tags_list:

        if tag[1] == "NN" or tag[1] == "NNP" or tag[1]== "NNS" or tag[1] == "PRP" or tag[1] == "JJ":
            nodes.append(tag[0])

        elif tag[1] == "VBZ" or tag[1] == "VBP" or tag[1] == "JJR" or tag[1] == "VBN" or tag[1] == "VB" or tag[1] == "VBP":
            relation = tag[0]


    if relation != None:
        type = extractedName(nodes[0])
        type = extractedName(nodes[1])
        graph.run("""MERGE (n:object{name:'""" + nodes[0] + """'}) return n""")
        graph.run("""MERGE (m:object{name:'""" + nodes[1] + """'}) return m""")
        graph.run("""MATCH (n:object{name:'""" + nodes[0] + """'}), (m:object{name:'""" + nodes[1] + """'})
            MERGE (n)-[r:""" + relation + """]->(m) return n,m""")