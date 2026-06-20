
def trains_planes(trains, planes):
    """Find what flights can be replaced with a rail journey.

    Initially, there are no rail connections between cities. As rail connections
    become available, we are interested in knowing what flights can be replaced
    by a rail journey, no matter how indirect the route. All rail connections
    are bidirectional.

    Target Complexity: O(N lg N) in the size of the input (trains + planes).

    Args:
        trains: A list of `(date, lcity, rcity)` tuples specifying that a rail
            connection between `lcity` and `rcity` became available on `date`.
        planes: A list of `(code, date, depart, arrive)` tuples specifying that
            there is a flight scheduled from `depart` to `arrive` on `date` with
            flight number `code`.

    Returns:
        A list of flights that could be replaced by a train journey.
    """
    
    # Sort the trains and planes by date
    trains.sort(key=lambda x: x[0])            
    planes.sort(key=lambda x: x[1])
    
    dsu = DSU()     # Create class instance
    result = []     # Create list for results
    t = 0           # Set train index
    
    # Loop though planes
    for (code, p_date, src, dst) in planes:
        
        # Loop conditions
        # Train pointer isn't out of domain -> no new trains to be added 
        # Only process the trains that exist before the plane flight
        while t < len(trains) and trains[t][0] <= p_date:
            _, a, b = trains[t]     # Get the source and destination
            dsu.union(a,b)          # Perform a union 
            t+=1                    # Move to next train

        # If a planes source and destination exist in a connected network
        # Replace the flight with train
        if dsu.find(src) == dsu.find(dst):
            result.append((code, p_date, src, dst))
    
    return result

class DSU:
    """Disjoint Set Union
    
    Maintains a forest of disjoint sets using parent pointers
    Each set represents interconnected cities (By train)
    Creates new edges and updates the paths
    
    Returns:
        String: Representative of a network 
    """
    # Initiate class with parent and rank
    def __init__(self):
        self.parent = {}    # Dict of city, representative pairs
        self.rank = {}      # The height of each tree (Representative, height)
    
    def find(self, x):
        
        # If a city has never been seen before, create a new tree
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        
        # If the city is not its own representative, find the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Compress path
        
        # Return the representative of the city
        return self.parent[x]
    
    def union(self, a, b):
        # Find representative of each city
        ra = self.find(a)       
        rb = self.find(b)
        
        # If the they are in the same tree just return
        if ra == rb:
            return
        
        # Merge the 2 conencted cities
        # Attach smaller network to larger network.
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1       