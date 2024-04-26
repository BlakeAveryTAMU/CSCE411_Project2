import pickle
from collections import deque

'''
Instructions on how to run this program:

1. In the command line run the following command: py main.py
2. You will be prompted to enter the file path for the adjacency list.
3. You will be prompted to enter the file path for the k values.
4. You will be prompted to enter the output file path.

'''

def open_and_print_pickle_file(file_path):

    with open(file_path, 'rb') as file:

        contents = pickle.load(file)
        #print(contents)
        return contents
    
def label_nodes(adj_list, k):
    

    n = len(adj_list)
    labels = [-1] * n
    visited = [False] * n
    queue = deque([0]) 
    visited[0] = True
    label = 0

    while queue:
        current = queue.popleft()
        labels[current] = label
        label = (label + 1) % k  # Wrap 

        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return labels


def calculate_r(tree, labels, v, k):
    visited = set()
    queue = [(v, 0)]
    while queue:
        node, distance = queue.pop(0)
        visited.add(node)
        if len(set(labels[u] for u in visited)) == k:
            return distance
        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

def calculate_m(tree, v, k):
    visited = set()
    queue = [(v, 0)]
    while queue:
        node, distance = queue.pop(0)
        visited.add(node)
        if len(visited) >= k:
            return distance
        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

def calculate_A(trees, labels_list, k_values):
    max_ratio = 0
    for tree, labels, k in zip(trees, labels_list, k_values):
        max_tree_ratio = 0
        for v in range(len(tree)):
            r = calculate_r(tree, labels, v, k)
            m = calculate_m(tree, v, k)
            ratio = r / m
            max_tree_ratio = max(max_tree_ratio, ratio)
        max_ratio = max(max_ratio, max_tree_ratio)
    return max_ratio

# Example usage
# A_small = calculate_A(small_trees, small_labels_list, small_k_values)
# A_medium = calculate_A(medium_trees, medium_labels_list, medium_k_values)
# A_large = calculate_A(large_trees, large_labels_list, large_k_values)
    
    


if __name__ == "__main__":

    '''
    adjList = open_and_print_pickle_file(input("Adjacency List File Path: "))
    kValues = open_and_print_pickle_file(input("K Values File Path: "))
    
    
    results = []
    for i in range(len(adjList)):
        labels = label_nodes(adjList[i], kValues[i])
        results.append(labels)
        

    output_file_path = input("Output File Path: ") #"./sol"
    with open(output_file_path, 'wb') as output:
        pickle.dump(results, output)
        
    '''
    small_adj = open_and_print_pickle_file("./Small_Examples_of_AdjLists_of_Trees")
    small_k = open_and_print_pickle_file("./Small_Examples_of_k_values")
    results = []
    for i in range(len(small_adj)):
        small_labels = label_nodes(small_adj[i], small_k[i])
        results.append(small_labels)

    A_small = calculate_A(small_adj, results, small_k)

    medium_trees = open_and_print_pickle_file("./Medium_Examples_of_AdjLists_of_Trees")
    medium_k_values = open_and_print_pickle_file("./Medium_Examples_of_k_values")
    medium_results = []
    for i in range(len(medium_trees)):
        medium_labels = label_nodes(medium_trees[i], medium_k_values[i])
        medium_results.append(medium_labels)

    A_medium = calculate_A(medium_trees, medium_results, medium_k_values)

    large_trees = open_and_print_pickle_file("./Large_Examples_of_AdjLists_of_Trees")
    large_k_values = open_and_print_pickle_file("./Large_Examples_of_k_values")
    large_results = []
    for i in range(len(large_trees)):
        large_labels = label_nodes(large_trees[i], large_k_values[i])
        large_results.append(large_labels)

    A_large = calculate_A(large_trees, large_results, large_k_values)

    print("A_small: " + str(A_small))
    print("A_Medium: " + str(A_medium))
    print("A_large: " + str(A_large))

