import csv

import schedule

schedule_filename = "data/schedule_raw.csv"
edges_filename = "output/edges.csv"
nodes_filename = "output/nodes.csv"

def main():
    schedule_data = schedule.load_data(schedule_filename)
    edge_data = schedule.find_edges(schedule_data)
    node_data = schedule.find_nodes(schedule_data)
    schedule.write_csv(edges_filename, ('Source', 'Target', 'Type'), edge_data)
    schedule.write_csv(nodes_filename, ('Id', 'Label', 'Type'), node_data)
    
if __name__ == '__main__':
    main()