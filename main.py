import pickle
from collections import Counter


def open_and_print_pickle_file(file_path):

    with open(file_path, 'rb') as file:

        contents = pickle.load(file)
        #print(contents)
        return contents
    
def label_nodes(adj_list, k):
    from collections import deque

    n = len(adj_list)  # Number of nodes
    labels = [-1] * n  # Initialize labels for all nodes
    visited = [False] * n
    queue = deque([0])  # Start BFS from node 0
    visited[0] = True
    label = 0  # Start labeling from 0

    while queue:
        current = queue.popleft()
        labels[current] = label
        label = (label + 1) % k  # Wrap label around k

        # Explore all adjacent nodes
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return labels
    
    


if __name__ == "__main__":
    adjList = open_and_print_pickle_file("./Examples_of_AdjLists_Of_Trees")
    kValues = open_and_print_pickle_file("./Examples_of_k_values")
    labeling = open_and_print_pickle_file("./Examples_of_labelling")
    

    # adj_list_example = [[[1, 2], [0, 3, 4], [0, 5, 6], [1, 7, 8, 9], [1, 10, 11], [2], [2], [3], [3], [3], [4], [4]]]
    # k_example = [6]

    # # Call the function on the first example
    # resulting_labels = label_nodes(adj_list_example[0], k_example[0])
    # print("Labeled nodes:", resulting_labels)
    
    results = []
    for i in range(len(adjList)):
        labels = label_nodes(adjList[i], kValues[i])
        results.append(labels)
        
    with open("MyResults.txt", 'w') as f:
        f.write(str(results))
    print(results)