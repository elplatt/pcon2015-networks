import csv

def load_data(schedule_filename):
    with open(schedule_filename, 'rU') as schedule_file :
        reader = csv.DictReader(schedule_file)
        return list(reader)

def find_edges(schedule_data):
    '''Return an array of tuples: (panel, presenter, 'Undirected').'''
    edge_data = []
    for row in schedule_data:
        title = row['Title']
        for presenter in row['Presenters'].split(','):
            presenter = presenter.strip()
            if len(presenter) > 0:
                edge_data.append((title, presenter, 'Undirected'))
    return edge_data
        
def find_nodes(schedule_data):
    '''Return an array of tuples: (name, name, presenter/panel).'''
    node_data = []
    presenters = set()
    for row in schedule_data:
        title = row['Title']
        node_data.append((title, title, 'panel'))
        for presenter in row['Presenters'].split(','):
            presenter = presenter.strip()
            if len(presenter) > 0:
                presenters.add(presenter)
    for presenter in presenters:
        node_data.append((presenter, presenter, 'presenter'))
    return node_data

def write_csv(filename, headers, data):
    '''Write the header row and a row for each element of data.'''
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)
    
if __name__ == '__main__':
    main()