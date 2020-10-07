import os
import sys
import json
import py2neo

if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(
        os.path.realpath(os.path.join(
            os.getcwd(), os.path.expanduser(__file__)))
    )
    PARENT_DIR = os.path.join(SCRIPT_DIR, "..")
    sys.path.append(os.path.normpath(PARENT_DIR))

dataset_path = os.path.join(PARENT_DIR, "dataset")

download_dummy_function(dataset_path)


neo4j_config_str = os.getenv('NEO4J', '{"host": "localhost"}')
neo4j_config_dict = json.load(neo4j_config_str)

ENV = os.getenv('ENV', 'prod')

graph = py2neo.Graph(**neo4j_config_dict)

dummy_data = data_parsing_dummy_function(dataset_path)

for dd in dummy_data:
    # just an bad example :) dont do it like this
    graph.run(
        "CREATE (n:Person { name: '"+dd.name+"', title: '"+dd.title+"' })")
