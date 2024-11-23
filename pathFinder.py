import networkx as nx

# Example paths
paths = [['block1', 'block6', 'add_block', 'block2'], 
         ['block1', 'block9', 'mul_block', 'add_block', 'block2'],
         ['block1', 'block10', 'mul_block', 'block12', 'add_block', 'block33', 'block2'],
         ['CONST_block', 'mul_block']]

def build_pert_graph(paths):
    """
    Build a PERT graph (DAG) from the given paths.
    """
    G = nx.DiGraph()
    for path in paths:
        for i in range(len(path) - 1):
            G.add_edge(path[i], path[i + 1])  # Add edges between consecutive blocks
    return G

def execute_blocks_with_predecessors(graph):
    """
    Execute blocks in topological order using NetworkX built-ins.
    """
    for block in nx.topological_sort(graph):
        # Use built-in predecessors method
        predecessors = list(graph.predecessors(block))
        if predecessors:
            print(f"Execute {block}, \tpre: {', '.join(predecessors)}")
        else:
            print(f"Execute {block}, pre: None")

# Build the PERT graph
pert_graph = build_pert_graph(paths)

# Execute the blocks and print the predecessors
execute_blocks_with_predecessors(pert_graph)
