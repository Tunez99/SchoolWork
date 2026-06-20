
class Genealogy:

    class Queue:
        """
        This Queue function is to support BFS. 
        A queue allows a first in, first out, methodology.
        This can be used in breadth first search as it allows us
        to process the nodes by levels

        During BFS, when a node is visited, all of its children are added to the queue
        Because the queue processes elements in a FIFO ordering, it makes sure all nodes
        at the current level are processed before moving down a level. This matches
        how we wish to handle seniority ordering. With nodes closer to the root
        processed first. 
        
        Raises:
            IndexError: For pop functions against an empty queue

        Returns:
            Array object: When a object is popped, we return that object.      
        """
        DEFAULT_CAPACITY = 8

        def __init__(self):
            # Build array with the default capacity
            self.data = [None] * self.DEFAULT_CAPACITY
            # Set the front of the queue
            self.front = 0
            # Set the size of the que to default
            self.size = 0
            
        def __len__(self):
            # Return size
            return self.size
        
        def __bool__(self):
            # Return True if array has items
            return self.size > 0
        
        def _index(self, i):
            # Move the front of the que by i positions, wrapping around
            return (self.front + i) % len(self.data)
        
        def _resize(self):
            # Set up new array with 2x size
            new_data = [None] * (len(self.data) * 2)

            # Move origional data into new data array
            for i in range(self.size):
                new_data[i] = self.data[self._index(i)]
            
            # Set the class array to the new data (2x Size)
            self.data = new_data
            # Reset the index to 0, (All data gets pushed to front)
            self.front = 0
            
        def push(self, item):
            # Check the size of the queue is smaller than array length
            if self.size == len(self.data):
                self._resize()
            
            # Set an index from front of que to the back. Without losing front index
            back_index = self._index(self.size)
            self.data[back_index] = item
            # Increase queue size
            self.size += 1
        
        def pop(self):
            # Check the que isn't empty
            if self.size == 0:
                raise IndexError("Pop from empty queue")
            # Take front item as a variable
            item = self.data[self.front]
            # Set that position to None
            self.data[self.front] = None
            # Move the front index to next item.
            self.front = (self.front + 1) % len(self.data)
            # Track queue size change
            self.size -= 1
            
            return item
        
        def push_many(self, items):
            # Push multiple times
            for item in items:
                self.push(item)
             
    class Tree:
        """ This class represents the genealogy structure
        
            No static fields as such to support multiple independent genealogy trees. 

            *** Look to __init__ method for data stroage explaination
        """

    def __init__(self, originator_name):
        # Explain how a dictionary can help track nodes by name."    
        """ Initialise the genealogy with a single root node.
        
            A dictionary can be used to track nodes effectively, using the following configuration
            Key:     Acts as the node name 
            Field_1: "parent" Allows the relation of the node to its parent with a string
            Field_2: "children" Allows relation to its children though an array
                        Note: Array gives functionality for multiple children
                        
            This structure allows:
            - O(1) look up of individuals
            - Easy traversal to parents and to children through relational fields.
            
        """  
        # Initialise instance level variables
        self.genealogy = {}
        self.origin = None
        
        # Add the origin node to be worked from
        self.genealogy[originator_name] = {"parent": None, "children": []}
        self.origin = originator_name
        
    def add_child(self, parent_name, child_name):
        """ Add child allows to add and entry to the tree system. 
            Adds the child to the parents node,
            Adds the child and relates the parent
            
            Note: It is O(1) because:
            hashLookUp = O(1)
            appendToList = O(1) amortized
            insertDictEntry = O(1)
            Overall Complexity = O(1)
            
            These operations are independent of the size of the data structure
            allowing the overall complexity to remain constant time.
            
            Args:
                parent_name (string): Defines the parent
                child_name (string): Defines the child
        """
        # Add children to parent relations, add new node
        self.genealogy[parent_name]["children"].append(child_name)
        self.genealogy[child_name] = {"parent": parent_name, "children": []}
    
    def get_primogeniture_order(self):
        """ This function uses depth-first traversal (DFS)
        
            Each node is visited before it's children, beginning from the root and 
            transversing down until no more children are present. Allowing us
            to fully transverse a branch before moving onto the next branch.
            Ensuring a primogeniture order. 

            While not explicitly a stack, the recursive function 
            works to use the call stack to simulate DFS
            
            Returns:
                Array: primogeniture order of the genealogy tree
        """
        order = []
        
        # Recersive function to perform DFS
        def visit(node):
            # Add node to the order
            order.append(node)
            # Check children, visit first child before returning to other children
            for child in self.genealogy[node]["children"]:
                visit(child)
        
        # Begin recursion from the root node
        visit(self.origin)
        return order
        
    def get_seniority_order(self):
        # Initialise Variables, array for the order, q, to use the Queue Class
        """ Function uses the queue class for breadth first search, allowing
            us to return the seniority order.
            
            For queue usage, see "class Queue" for explaination.
            
            Following the function, we see how each node is popped and placed into 
            the order array, the function then adds the next level children to the queue
            and finishes once the queue empties.
            This ensures all children of the current level, is added in order
            to the end of the queue, preserving seniority ordering.

            Returns:
                Array: seniority order of the genealogy tree
        """
        order = []
        q = self.Queue()
        
        # Initialise the order by pushing the origin node
        q.push(self.origin)
        
        # Loop while items exist in the queue
        while q:
            # Pop and append to order from front of the queue
            node = q.pop()
            order.append(node)
            
            # Add the children from popped member, A then B 
            for child in self.genealogy[node]["children"]:
                q.push(child)
                
        return order

    def get_cousin_dist(self, lhs_name, rhs_name):
        """ This functions handles solving the cousin degree and removal.
            
            This is solved by comparing the distance from the closest common ancestor
            of the 2 groups. We can pull the ancestor list from the 
            get_ancestors() function. 
            
            We compare the lists to find a common ancestor and set the 
            distance found to it from each node. 
                - dist1: distance from lhs node to the common ancestor
                - dist2: distance from rhs node to the common ancestor
            
            We then use whats found to calculate the outputs
            
            The cousin degree is calculated using:
                min(dist1, dist2) - 1
            The removal is calculated using:
                abs(dist1 - dist2)

            Args:
                lhs_name (string): Name of node we want to process
                rhs_name (string): Name of different node to compare with

            Returns:
                int: cousin degree 
                int: removal
        """
        # Get a list of ancestors for each node
        lhs_members = self.get_ancestors(lhs_name)
        rhs_members = self.get_ancestors(rhs_name)
        
        # Create a set, for easy comparison
        rhs_set = set(rhs_members)
      
        # lowest common ansestor
        lca = None
        dist1 = 0 
        
        # Check lhs ancestors are existing in rhs ancestors
        for i, item in enumerate(lhs_members):
            # Once a lca is found, update variables and the lhs distance from it
            if item in rhs_set:
                lca = item
                dist1 = i
                break
        
        # Find distance from lca for rhs members
        dist2 = 0
        for i, item in enumerate(rhs_members):
            if item == lca:
                dist2 = i
                break
        
        # Calculate removal
        removal = abs(dist1 - dist2)

        # Calculate cousin degree
        # Note, -1 is for root offset.
        if dist1 < dist2:
            degree = dist1-1
        else: 
            degree = dist2-1
            
        return degree, removal

    def get_ancestors(self, name):
        """
            Function starts from the node we wish to process, it adds it
            to the ancestor list, then moves up to the parent node until
            the tree root is reached.
            
            It's efficient as each node only has 1 parent so we only 
            need to use a constant-time dictionary lookup. This gives
            us the total cost O(h) where h is the height of the tree. 

            Args:
                name (str): node we want to begin with

            Returns:
                Array: list of ancestors starting from the node provided
        """
        ancestors = []
        # Starting child node
        current = name
        
        # Check if a parent exists and move up a node until root is reached
        while current != None:
            ancestors.append(current)
            current = self.genealogy[current]["parent"]
        return ancestors
        
