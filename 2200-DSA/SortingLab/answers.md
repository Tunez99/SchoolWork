
Question 1 (1 mark)

Explain the relationship between this problem and more abstract computer science topics covered in class.

Answer:

The speed running leaderboard is a practical application of data structures and algorithms. The data stored can be viewed through the lens of a data structure, containing imformation like; rank, time, and identity. The way we organise data and display it represents the algorithm component. Though various methods supplied to us, we can use algorithms to understand, analyse and highlight the leaderboard in a way that's meaningful. 

In class, we have covered various applicable concepts, including arrays, recursive functions (merge-sort), searching algorithms, sorting algorithms, appending, removing items from a list, and other strategies to handle data. We also cover how these algorithms can provide different applications depending on the outcome desired. This allows us to analyse the time and space complexitiy and help improve performance and lower computational costs against various hardware set ups. 

Finally, we can say that this problem can be abstracted into a data structure, algoritms, and also a way to update the data. Updating leans more into design and implementation however is still an important concept to consider and will be discussed later. 

Question 2 (1 mark)

What data do you need to store in the Leaderboard class?
What algorithm do you intend to use for each method?

Your Answer:

It overall identifies the necessary data and respective algorithms for the functions.

The leaderboard class will need to hold the data time and name. We can store this in a list as tuples of (time, name). We also want to sort the list early so it can be acted on without using large algorithms. For this i'll use merge sort. Now that the array is sorted. The only other method that will require a larger algorithm is "submit_run". This is because we need to find a location then insert the new addition, this will mean a lot of data will need to be shifted. I'll use binary search for the index then insert it there. For the rest of the methods, simple loops with comparision operators should suffice. 

merge sort: O(nlog(n)) time
submit run: O(log(n) + O(n)) => O(n) time
Other methods: O(1) : O(n)

Question 3 (5 marks)

Implement your design by filling out the method stubs in speedrunning.py.
Your implementation must pass the tests in test\_speedrunning.py.

This question is assessed only on your code.

Question 4 (1 mark)

Give an argument for the correctness and complexity of your **init**() function.

Answer:

The __init__() function is both correctness and complexity. 

The goal is to store the data in a useful format. This takes the form of a sorted list of tuples. Merge sort correctly sorts the tuples in acending time and then alphabetically for tie breakers. This ensure it's correctly sorted on iinitializatoin. The time complexity is O(nlog(n)) for merge sort and O(n) for appending the entries. This means the overall complexity is O(nlog(n)).

I will note however, using different data structures may be more efficient. For example, a dictionary for quick lookups, and a linked list to reduce the amortize cost of inserting new runs. This would make the overall program more efficient on large datasets. 


Question 5 (1 mark)

Give an argument for the correctness and complexity of your submit\_run() function.

Answer:

The submit_run() function uses to distinct methods. Binary search and insert. Binary takes O(log(n)) time while inserting the element into the list requires a shift so will run in O(n) for the worst case. This, while acceptable for the scope, O(n) can scale when the dataset grows. This may need to be considered though a change of data structures such as a linked list to reduce amortized cost of insertions. Despite the limitations present, the implementation is correct. It works to maintain the structure and order of the list so that other functions can still function correctly.


Question 6 (1 mark)

Give an argument for the correctness and complexity of your count\_time() function.

Answer:

While the function runs in O(n) time. There is still space for improvements. One key point about this function is that we are looking for a group of numbers. We compare every number until we pass the times and can break. This allows for a better average case O(n-k) where k is the index position of the last occuring time. However we could use a binary search again to find the start of the list in O(log(n)+ m) where m is the size of the times with that time. 


