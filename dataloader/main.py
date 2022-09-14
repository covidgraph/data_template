import os
import sys
import json
import py2neo


# we load the neo4j database connection details from the environment variable `NEO4J`
neo4j_config_str = os.getenv("NEO4J", {"host": "localhost"})
neo4j_config_dict = json.load(neo4j_config_str)
# Connect to the neo4j database
graph = py2neo.Graph(**neo4j_config_dict)


ENV = os.getenv("ENV", "prod")


# your dataloader logic
dataset_url = "https://data.org/mydata.txt"
download_dummy_function(dataset_url)
dummy_data = data_parsing_dummy_function(dataset_path)
for dd in dummy_data:
    # just an bad example :) dont do it like this
    graph.run(
        "CREATE (n:Person { name: '" + dd.name + "', title: '" + dd.title + "' })"
    )
