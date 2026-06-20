
class Leaderboard:
    """A leaderboard of speedrunning record times.

    Each entry has a time in seconds and a runner name.
    Runners may submit multiple runs.
    The leaderboard is ranked fastest run first.
    Ties receive the same rank as each other, so for example if runners submit
    the times 10, 20, 20, and 30, they will have the ranks 1, 2, 2, and 4.
    """
    def __init__(self, runs=[]):
        """Constructs a leaderboard with the given runs.

        The given list of runs is not required to be in order.

        Args:
            runs: Initial leaderboard entries as list of (time, name) pairs.
        """
        
        # Initialise a list 
        self.ordered_list = []
        
        # Append every run to the leaderboard, in not particular order
        for items in runs:
            self.ordered_list.append(items)
        
        # Order the list at init for future use.
        # Merge sort is efficient in this case
        self.ordered_list = self.merge_sort(self.ordered_list)
        
        
    def get_runs(self):
        """Returns the current leaderboard.

        Leaderboard is given in rank order, tie-broken by runner name.

        Returns:
            The current leaderboard as a list of (time, name) pairs.
        """
        # List is already made ordered at init, so just return
        return self.ordered_list
        

    def submit_run(self, time, name):
        """Adds the given run to the leaderboard

        Args:
            time: The run time in seconds.
            name: The runner's name.
        """

        # instantiate variable, use, "run" for easy grouping
        # note, python will automatically compare time then name 
        # 
        run = (time, name)
        
        # Start boundaries
        left = 0
        right = len(self.ordered_list)

        # Implement binary search
        
        while left < right:
            # Find middle point
            mid = (left + right) // 2
            
            # if the run is slower, than the middle run, move right
            # else move right
            if self.ordered_list[mid] <= run:  
                left = mid + 1
            else: 
                right = mid

        # insert at the found index
        self.ordered_list.insert(left, run)
         
        
    def get_rank_time(self, rank):
        """Get the time required to achieve at least a given rank.

        For example, `get_rank_time(5)` will give the maximum possible time
        that would be ranked fifth.

        Args:
            rank: The rank to look up.

        Returns:
            The time required to place `rank`th or better.
        """
        # This is fun, we don't care about the actual rank
        # So just full the index and offset for 0 in arrays
        # Note, [0] at end defines the time found in (t, n) entries
        return self.ordered_list[rank - 1][0]
        

        


    def get_possible_rank(self, time):
        """Determine what rank the run would get if it was submitted.

        Does not actually submit the run.

        Args:
            time: The run time in seconds.

        Returns:
            The rank this run would be if it were to be submitted.
        """
        #initialise variable, rank starts at 1 
        # i converted to "data" here for readability at time. 
        rank = 1
        data = self.ordered_list

        # loop though the sorted array
        for items in data:
            # check each items time, if smaller, move the "entry"
            # up a rank, only when less than, if equal, will continue to 
            # some higher position
            if items[0] < time:
                rank += 1
            # Once found we can break to save time on larger sets.
            else: 
                break

        return rank

    def count_time(self, time):
        """Count the number of runs with the given time.

        Args:
            time: The run time to count, in seconds.

        Returns:
            The number of submitted runs with that time.
        """
        # instantiate count
        count = 0
        
        # Basic loop, for every item in the list, we add to count
        # This could be optimised to find first instance and exit once 
        # all have been read. (Note, it's in order)
        
        for i in range(len(self.ordered_list)):
            if self.ordered_list[i][0] > time:
                break
            if self.ordered_list[i][0] == time:
                count += 1
        return count
    
    
    def merge(self, lhs, rhs):
        """Merges a pair of sorted lists.

        Args:
            lhs: A sorted list to be merged with rhs.
            rhs: A sorted list to be merged with lhs.

        Returns:
            A sorted list containing all the elements of lhs and rhs.
        """
        # instantiate variables, array
        result = []
        i = 0
        j = 0

        # loop through both lists
        while i < len(lhs) and j < len(rhs):
            
            # compare elements
            # if the item in LHS <= RHS push the left hand side and progress
            # if RHS <= LHS push right
            if lhs[i] <= rhs[j]:
                result.append(lhs[i])
                i += 1
            else:
                result.append(rhs[j])
                j += 1

        # Add all remaining elements from either list
        while i < len(lhs):
            result.append(lhs[i])
            i += 1

        while j < len(rhs):
            result.append(rhs[j])
            j += 1

        return result


    def merge_sort(self, arr):
        """Sorts the given list using merge sort.

        Args:
            arr: The list to be sorted.

        Returns:
            The list in ascending order.
        """
        # Check for base case
        if len(arr) <= 1:
            return arr

        # find the mid point
        mid = len(arr) // 2
        
        # Assort left and right to the arrays this is recersive.
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        # Push to merge
        return self.merge(left, right)


    
        
