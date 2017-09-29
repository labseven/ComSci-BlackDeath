''' Import the OWTRAD csvs into two pandas dataframes

By default, it looks for the files in ./OWTRAD-Files/
You can change that by setting the envirnoment variable OWTRAD_DIR

'''

import pandas as pd
import os

def import_owtrad():
    # Set OWTRAD_DIR to the envirnoment variable, if not set, default to OWTRAD_DIR
    OWTRAD_DIR = os.getenv('OWTRAD_DIR') or "./OWTRAD-Files/"

    if not os.path.isdir(OWTRAD_DIR):
        raise Exception("OWTRAD files dir does not exist! Please set correct OWTRAD_DIR envirnoment variable.")

    print("Importing OWTRAD files from", OWTRAD_DIR)

    nodes = pd.DataFrame()
    for filename in [OWTRAD_DIR + filename for filename in os.listdir(OWTRAD_DIR) if 'nodes' in filename]:
        new_csv = pd.read_csv(filename.strip(), header=0)
        nodes = pd.concat([nodes, new_csv], ignore_index=True)

    print("Imported", len([OWTRAD_DIR + filename for filename in os.listdir(OWTRAD_DIR) if 'nodes' in filename]), 'node files')

    edges = pd.DataFrame()
    for filename in [OWTRAD_DIR + filename for filename in os.listdir(OWTRAD_DIR) if ('routes' in filename or 'edges' in filename)]:
        new_csv = pd.read_csv(filename.strip(), header=0)
        edges = pd.concat([edges, new_csv], ignore_index=True)

    print("Imported", len([OWTRAD_DIR + filename for filename in os.listdir(OWTRAD_DIR) if ('routes' in filename or 'edges' in filename)]), 'route files')

    # print(nodes.info())
    # print()
    # print(edges.info())

    return nodes, edges
