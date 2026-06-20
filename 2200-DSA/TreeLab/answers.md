# CITS2200 Lab 2: Genealogy

## Question 1 (1 mark)
Write a simple description of how you are going to represent the problem as a data structure.
Your description should justify how the representation is going to help you solve the problem within the target complexities.

The problem introduces us to a family tree structure and using algorithms to solve for the next envoy.

The problem will be represented as a Tree structure to model the genealogy fo the Kiktil.

Each node in the tree will be stored in a dictionary containing the following:
Key     -> The node name
Field1  -> A reference to the parent of the node
Field2  -> A list containing associated children 

Dictionary operations allows efficient O(1) average time look ups and insertions. 

As a result, the structure allows us to use the relations to traverse the genealogy tree. 

This ensure, adding relationships are made in O(1) time, and meet the required constraints.

## Question 2 (1 mark)
Write a simple description of the algorithm you have designed for `get_cousin_dist()`.
Your description should justify the correctness of your algorithm, and make an argument as to its time complexity.

The algorithm for get_cousin__dist() computes the cousin degree and the removal between 2 members of the Kiktil.

First, the algorithm uses the get_ancestors() helper function to build a list of ancestors for each member. Which efficiently runs in O(h) as the tree can easily be traversed upwards using the parent referencing.

We then compare the lists to determine the lowest common ancestor between the members. This happens in O(h) also, as it at worst need to compare the full height of the tree.

Once a LCA is determined, we can measure the distance from each member to the LCA. This distance represents how many generations each individal is removed. 

Using the information found we can calculate:
The cousin degree:
    min(dist1, dist2) - 1

The removal:
    abs(dist1 - dist2)

This algorithm is correct as it uses the unquie properties of a Tree structure to map indiviuals and find the LCA to where they meet on the Tree.

The complexity of the algorith works in O(h) worst-case, where the common indiviuals are the youngest children and the LCA is the root node. h represents the height of the tree and comparison between lists is linear in length.

## Question 3 (5 marks)
Implement your design by filling out the method stubs in the `Genealogy` class found in `genealogy.py`.
You are **not** allowed to import any modules.
Your implementation must pass the tests given in `test_genealogy.py`, which can be invoked by running `python -m unittest`.

See `genealogy.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `get_primogeniture_order()` function.

The get_primogeniture_order() correctly produces a primogeniture order of the genealogy tree.

The algorithm features a recursive function that works through the use of the call stack.

From the root node, it visits the each node, then recursively visits each child in the order they appear. This means that every parent is seen before its decendents, and the oldest of children will be processed before the younger siblings. Which matches primogeniture ordering.

This provides us a correctness through the properties of depth-first traversal. Every node is visited once, and a branch is fully processed before moving onto the next sub-tree.

The time complexity of this function is O(n), where n is the number of nodes present in the tree. Due to every node being visited atleast once. 
The space complexity is O(h) where h is the height. This is afforded to us by using the call stack.

## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `get_seniority_order()` function.

The get_seniority_order() function correctly produces a seniority order of the genealogy tree.

The algorithm successfully leverages the Queue class to invoke a breadth first search. 
The queue manages the order of exploration, each level of the tree is processed in order of its addition to the queue. This ensures that individuals closer to the origin are listed before those further away, and that siblings are processed in birth order.
Correctly reflecting the seniority ordering we desire.

This provides us a correctness through the properties of breadth-first traversal. Meaning all nodes at depth d are processed before any nodes at d+1. 

The time complexity is also O(n), where n is the number of node present in the tree.
The space complexity is O(n) worst case. If the tree stores every node on the same level.

## Question 6 (1 mark)
Give a brief explanation of the function and purpose of any data structures you implemented.

Dictionary-based tree
Function is to work as the main structure in the system. It builds a tree structure, maintains relationships that supports traversal up and down the structure. It also provides O(1) look ups, meaning we can assess any node allowing more complex algorithms to function against it. 

Children list
A list implemented into each dictionary entry. This list stores the relationship from parent to children, it supports multiple children, which maintain sibling order and supports the traversal of BFS and DFS.

Custom Queue 
The queue works as a circular array, allowing us to achieve FIFO operations (push, pop) in O(1) amortized time and is crucial for implementing BFS.

These 3 main data structures enable the efficient construction of the geneology tree and supports the required operations within the time complexity constraints provided.

