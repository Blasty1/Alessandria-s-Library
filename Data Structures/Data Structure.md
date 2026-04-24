An abstract data type ( ADT ) is an abstraction of a data structure which provides only the interface to which a data structure must adhere to. Its implementation is a data structure ( DS ).
![[Screenshot 2026-02-27 alle 19.33.52.png]]
Big-O Notation gives an upper bound of the complexity in the worst case.
![[Screenshot 2026-02-27 alle 19.37.49.png]]
Examples:
![[Screenshot 2026-02-27 alle 19.41.14.png]]
It does not depend on the input, so the loop is O(1).
![[Screenshot 2026-02-27 alle 19.47.09.png]]
This is the binary search algorithm.

# Static and Dynamic Arrays
- A static array is a fixed length container containing n elements indexable from the range [0,n-1]
- A dynamic array can grow and shrink in size
	- It is implemented using a static array with an initial capacity : if adding another element will exceed the capacity, then create a new static array with twice the capacity and copy the original elements into it.
![[Screenshot 2026-02-27 alle 19.52.34.png]]
![[Pasted image 20260227195416.png]]
Array indexing is zero based.

# Singly and Doubly Linked List
A linked list is a sequential list of nodes that hold data which point to other nodes also containing data
	- Head is the first node in a linked list
	- Tail is the last node in a linked list
	- A node is an object containing data and pointer(s)
There are two types of linked list:
- Singly linked list: each node holds a reference to the next node.
- Doubly linked list: each node holds a reference to the next and previous node
![[Screenshot 2026-02-27 alle 20.06.39.png]]
![[Screenshot 2026-02-27 alle 20.12.29.png]]

# Stack
A stack is one-ended linear data structure which models a real world stack by having two primary operations: **push** ( insert an element at the top of the stack ) and **pop** ( removing an element at the top of the stack ).
![[Screenshot 2026-02-27 alle 20.20.04.png]]
It is a LIFO data structure: the last element inserted is the first element out.
![[Screenshot 2026-02-27 alle 20.23.05.png]]

# Queues
A queue is a linear data structure which models real world queues by having two primary operations: **enqueue/adding** ( insert the element at the back ) and **dequeue/polling** ( remove the element from the front ).
![[Screenshot 2026-02-27 alle 20.29.23.png]]
It is a FIFO data structure: the first element inserted is the first element out.
![[Screenshot 2026-02-27 alle 20.32.37.png]]
Peeking means that we are seeing the value at the front of the queue without removing it.
It can be implemented using an array or a linked list.

## Priority Queue
A priority queue is an Abstract Data Type ( ADT ) is a queue where each element has a certain priority which determine the removal order of each element.
Priority queue only supports comparable data.

### Heap
**An Heap is a tree based Data Structure that satisfies the heap invariant** ( also called heap property ): if A is a parent node of B then A is ordered with respect to B for all nodes A , B in the heap. It means that the value of the parent node is always greater or equal than the values of the child nodes ( for all nodes ) or the other way around.
We have two types of heaps:
- Max Heap ( bigger number at the root )
- Min Heap ( lower number at the root )
![[Screenshot 2026-02-28 alle 15.01.48.png]]
Examples:
- Is it an heap? 
![[Screenshot 2026-02-28 alle 15.03.01.png]]
Answer: No ( right bottom, there 2 upper 3 ).
- Is it an heap?
![[Screenshot 2026-02-28 alle 15.03.38.png]]
Answer: Yes.
- Is it an heap? 
![[Screenshot 2026-02-28 alle 15.04.47.png]]
Answer: Yes.
- Is it an heap?
![[Screenshot 2026-02-28 alle 15.07.19.png]]
Answer : No ( this structure is not a tree because it contains a cycle, heaps must be trees )
![[Screenshot 2026-02-28 alle 15.09.05.png]]
It is implemented as an array in Java.
Peak means see the root value.
![[Screenshot 2026-02-28 alle 15.10.05.png]]
Searching and removing is linear because heap guarantees us only a relation between the parent and the childrens ( we have a partially ordered data structure ) not like a **BST** ( Binary Search Tree ) where for every node, smaller values are strictly on the left and larger values are on the right.
Techniques:
- Turning Min PQ into Max PQ $\rightarrow$  negate the elements when i enter them in the data structure and negate them again when they are taken out.

#### Binary Heap
There are different types of heap, we can use **binary heaps** for implementing a Priority Queue.
A binary heap is a binary tree ( every node has exactly two children ) that supports the heap invariant.
![[Screenshot 2026-02-28 alle 15.21.53.png]]
A complete binary tree is a tree in which at every level ( except the last ) is completely filled and all the nodes as far left as possible.
![[Screenshot 2026-02-28 alle 15.23.08.png]]

How to **add** an element to binary heap?
Using the **bubbling up technique**: we insert the new element as the far most left leaf and then if this element is lower than its parent, we swap them and so on untilll the heap property is satisfied/restored.
![[Screenshot 2026-02-28 alle 15.31.00.png]]
![[Screenshot 2026-02-28 alle 15.31.09.png]]

How to **dequeue/poll** an element from the binary heap?
It means removing the head of the tree.
We just swap the root with the left most leaf and we remove it. After that we need to restore the heap property by swapping the root with its children ( **bumbling down** technique )

How to **remove** an element from the binary heap?
We need a linear scanning to find the element and we swap it with the last node of our tree. After that we need to restore the heap property.
The remove operation is linear because it requires a linear search to find out where an element is indexed at. We can improve it by using a Hashtable: a look up table where we map the node with its index inside the heap ( if there are collisions, we keep a list of indices and we can delete any node in any positions as long as the heap property is satisfied ).
We can represent a binary heap by using an array:
![[Screenshot 2026-02-28 alle 15.24.01.png]]
Considering **i** the parent node index:
- Left child index is **2i+1**
- Right child index is **2i+2**

# Union Find / Disjoint Set
It is a data structure that keeps track of elements which are split into one or more disjoint sets.
It has two primary operations:**find** ( given an element, it says what group the element belongs to ) and **union** ( it merges two groups together ).
![[Screenshot 2026-02-28 alle 16.02.16.png]]
Amortized constant time means almost constant time but not quite constant time.

It is implemented using an array:
- We need to build a bijection ( a mapping ) between our objects and the integers in the range [0,n] 
![[Screenshot 2026-02-28 alle 16.17.05.png]]
- We store Union Find information in an array , each index has an associated object 
![[Screenshot 2026-02-28 alle 16.20.07.png]]
Each value in the array represents that letter to which letter is linked.
![[Screenshot 2026-02-28 alle 16.21.15.png]]
We merge smaller components into larger ones.
![[Screenshot 2026-02-28 alle 16.21.55.png]]
We use 2 arrays: 
- one for tracking the mapping between the group and the element
- one for tracking the dimension of each group

Operations:
- Find a component means find the root of that component by following the parent nodes untill a self loop is reached
- Unify two elements means make one of the root nodes be the parent of the other

**Path Compression**:  each component of the group just points to the root node which allows us to get the root node in a constant time.
Before:
![[Screenshot 2026-02-28 alle 16.29.31.png]]
With path compression ( only)
![[Screenshot 2026-02-28 alle 16.30.03.png]]

## Kryskal's Algorithm
It is an application of the Union Find data structure.
A **minimum spanning tree** is a subset of the edges of a graph which connect all vertices in the graph with the minimal total edge cost.
This algorithm helps to find a MST ( Minimum Spanning Tree ) in a given graph **G = (V,E)**  ( it may not be unique ).
![[Screenshot 2026-02-28 alle 16.05.13.png]]
A possible Minimum Spanning tree is:
![[Screenshot 2026-02-28 alle 16.05.40.png]]
It works in 3 steps:
1. Sort edges by ascending edge weight
![[Screenshot 2026-02-28 alle 16.08.07.png]]
2. We iterate over the sorted edges and look at the two nodes the edge belongs to:
	1. If they are already unified ( belongs to the same group ), we just skip this edge
	2. If they are not unified, we unify them (merge the groups) and we include the edge
![[Screenshot 2026-02-28 alle 16.08.39.png]]
We are trying to connect C and J but they are already connected in the yellow group, we skip it.
![[Screenshot 2026-02-28 alle 16.09.34.png]]
3. The algorithm ends when every edge has been processed or all the vertices have been unified ( we have only only one group )

# Tree
A tree is an undirected graph which satisfies any of the following definitions:
- Acyclic connected graph
- A connected graph with N nodes and N-1 edges
- An graph in which any two vertices are connected by exactly one path
![[Screenshot 2026-02-28 alle 18.34.53.png]]
A leaf node is a node with no children ( highlighted in orange )
![[Screenshot 2026-02-28 alle 18.37.08.png]]
A Binary tree is a tree for which every node has at most two child nodes.

## Binary Search Tree ( BST )
It is a binary tree that satisfies the BST invariant: left subtree has smaller elements and right subtree has larger elements.
![[Screenshot 2026-02-28 alle 18.39.15.png]]
BST operations allow for duplicate values but most of the time we are only interested in having unique elements inside our tree.
Is this a BST?
![[Screenshot 2026-02-28 alle 18.40.50.png]]
It is not: 9 is larget than 9 then it should be in the right subtree of 8.
Is this a BST?
![[Screenshot 2026-02-28 alle 18.42.09.png]]
Yes.
![[Screenshot 2026-02-28 alle 18.43.12.png]]
Worst case is when our tree degenerate in a list/line.

Operations:
- Add an element : we start from the root and we move to right or left if the element is greater or lower than the root and so on untill we reach a leaf where we can place the new value.
![[Screenshot 2026-02-28 alle 18.46.16.png]]
- Removing an element: we need to find the element we wish to remove and we replace it with its successor to maintain the BST invariant 
	- If the value is a leaf, we just delete it without side effects
	- If the value has only a successor ( right or left not both ):  we just replace it with the root of the successor subtree.
![[Screenshot 2026-02-28 alle 18.52.10.png]]
![[Screenshot 2026-02-28 alle 18.52.28.png]]
	- If the value has two subtree successors ( right and left ): the successor can be either the smallest value in right subtree ( go right and always as left as possible ) or largest in left subtree(go left and always as right as possible).
![[Screenshot 2026-02-28 alle 18.55.13.png]]
We pick the smallest value in the right subtree: 11. 
We replace the root with it and then we delete the old 11.
If we traverse it by using InOrder strategy ( see it below ) we get a sorted list of the elements of the BST.


## Tree Traversals
- Preorder traversal $\rightarrow$ prints the current node before the recursive calls
	- it prints left left left and then right right right
![[Screenshot 2026-03-01 alle 09.04.58.png]]
- Inorder traversal $\rightarrow$ prints the current node between the recursive calls
	- It prints left parent right ( it prints the values in ascending order )
![[Screenshot 2026-03-01 alle 09.06.40.png]]
- Postorder traversal $\rightarrow$ prints after the recursive calls
![[Screenshot 2026-03-01 alle 09.03.40.png]]
	- It prints the right , left and then center 
- Level order traversal  $\rightarrow$  we need **BFS** ( Breadth First Search )from the root node down to the leaf nodes to do that ( it explores all the nodes in levels )
	- We maintain a queue of the nodes left to explore, we begin with the root and we finish when the queue is empty.
	- We extract an element from the front of the queue and we put inside the queue its children.
![[Screenshot 2026-03-01 alle 09.13.24.png]]
You can implement it iteratively by using a stack: go left and when the next is null, you check for the right and you go back by extracting an element.


## Balanced Binary Search Tree ( BSST )
A BSST is a **self-balancing** binary search tree: it will adjust itself in order to maintain a low height allowing for faster operations such as insertions and deletions.
![[Screenshot 2026-03-01 alle 10.44.12.png]]
The secret ingredient to most BBST algorithms is the usage of two things:
- Tree invariant property $\rightarrow$  it is a property ( imposed by us to the tree ) that must be meet after every operation ( to ensure that a series of tree rotations are usually applied )
- Tree rotations $\rightarrow$ we can transform the values and nodes in the tree as we please as loong as the BST invariant remain satisfied
![[Screenshot 2026-03-01 alle 10.46.33.png]]
![[Screenshot 2026-03-01 alle 11.03.07.png]]
![[Screenshot 2026-03-01 alle 11.03.37.png]]
There is a slight problem here: the parent of this node rotated is still linked to the old subtree root A , we need to recursively callback using the return value of rotateRight.

### AVL Tree
An AVL tree is one of many types of BSSTs which allow for logarithmic $O(log n)$ insertion, deletion and search operations.
It was the first type of BSST to be discovered. 
The Balanced Factor ( BD ) is the property that keeps an AVL tree balanced
$$
\text{BF}(\text{node}) = H(\text{node.right}) - H(\text{node.left})
$$
H(x) is the height of the node x ( number of edges between x and the furthest leaf ). AVL tree forces the Balanced Factor always to be either -1, 0 or 1 ( if it is not, it is adjusted by using tree rotations).
 ![[Screenshot 2026-03-01 alle 11.15.39.png]]
Each node in the tree contains:
- Actual value
- Node's balance factor
- Height of this node in the tree
- Pointer to left/right child nodes

*How to insert a value?*
![[Screenshot 2026-03-01 alle 11.16.57.png]]
![[Screenshot 2026-03-01 alle 11.17.04.png]]
![[Screenshot 2026-03-01 alle 11.18.06.png]]
-1 becomes for leaf nodes.
![[Screenshot 2026-03-01 alle 11.18.30.png]]

*How to remove a value?*
It is very similar to what we have seen in BST.
We need to find the node and after that we can have 4 cases:
![[Screenshot 2026-03-01 alle 11.21.20.png]]
1. Leaf node $rightarrow$ we just remove it without side effects
2. Either left/right child node is a sub tree $rightarrow$  the successor is its immediate child and it becomes the new root
3. Both right and left child nodes are subtrees  $rightarrow$  the success can be either the largest value in the left subtree or the smallest values in the right subtree
	1. We replace the  node to delete with the new found one but in this way we have duplicates , we need to remove it
![[Screenshot 2026-03-01 alle 11.29.58.png]]
![[Screenshot 2026-03-01 alle 11.30.14.png]]
![[Screenshot 2026-03-01 alle 11.30.21.png]]
![[Screenshot 2026-03-01 alle 11.30.40.png]]
After each removal we need to balance it.

# Hash Tables
It is a data structure that provides a mapping from keys to values using a technique called hashing.
![[Screenshot 2026-03-01 alle 09.24.08.png]]
All the keys must be unique ( not the values ).
An **hash function** $H(x)$ is a function that maps a key $x$ to a whole number in a fixed range.
![[Screenshot 2026-03-01 alle 09.26.01.png]]
If the hash functions are equal ( $H(x) = H(y)$ ) than objects x and y **might be** equal while if they are different ( $H(x) \neq H(y)$ ) then x and y are **certainly** not equal.
An hash function $H(x)$ must be deterministic: if $H(x) = y$ then the hash function $H(x)$ must produce always $y$ and never another value.
We also try to make uniform hash functions to minimize the number of **hash collisions** ( it is when two objects x,y hash to the same value $H(x) = H(y) \quad x \neq y$.
We use the hash function as a way to index into a hash table: we have o(1) time complexity if our hash function is uniform and we avoid too much collisions.
There are 2 most popular techniques to handle hash collisions:
- Separate chaining $\rightarrow$ it maintains a data structure ( a linked list usually ) to hold all the different values hashed to a particular key.
![[Screenshot 2026-03-01 alle 09.47.24.png]]
- Open addressing  $\rightarrow$ it finds another place within the hash table for that object.
![[Screenshot 2026-03-01 alle 09.44.50.png]]

## Open Addressing
We need to take care of the size of our hash table and how many elements are currently in the table
$$
\text{Load Factor} \alpha = \frac{\text{\#items in table}}{\text{\#size of table}}
$$
The constant time behaviour is valid only if our load factor $\alpha$ is kept below a certain fixed value ( if it is too big, we need to grow the table size )
![[Screenshot 2026-03-01 alle 09.53.04.png]]
*How it works?*
If the position of our key is occupied, we try another position in the hash table by offsetting the current position subject to a probing sequence $P(x)$ and we keep doing that until an unoccupied slot is found.
There are a lot of probing sequences:
- Linear probing ( a, b are constants )
$$
P(x) = ax+b
$$
- Quadratic probing ( a,b,c, are constans )
$$
P(x) = ax^2 + bx + c
$$
- Double Hashing
$$
P(k,x) = x H_2(k)
$$
Where $H_2$ is a secondary hash function and k is the key.
We are multiplying our x value by the hashing of the key.
$H_2(k)$ must hash the same type of keys as $H_1(k)$
- Pseudo random number generator
$$
P(k,x) = x \text{RNG(H(k), x)}
$$
RNG is a random number generator function seed with H(k).
![[Screenshot 2026-03-01 alle 10.03.48.png]]
Using probing sequences can produce a cycle shorter than the table size: when we want to insert a key-value pari and all the buckets on the cycle are occupied and we get stuck in an infinite loop.
- It can be avoided, for linear probing $P(x) = ax + b$, when $a$ and $N$ ( the size of the hash table ) are relatively prime. Two numbers are relatively prime if their GCD ( Greatest Common Denominator ) is equal to 1. In other words , when $GCD(a,N) = 1$ our probing function will be able to generate a complete cycle. A common choice of $a$ is 1 because no matter the choice of N it is always true that $GCD(N,1) = 1$.
- It can be avoided, for quadratic probing by picking one of this most popular approaches
	- $P(x) = x^2$ and $N$ a prime number > 3 with $\alpha \leq 0.5$
	- $P(x) = \frac{x^2+x}{2}$ and $N$ be a power of two
	- $P(x) = (-1^x)x^2$ and $N$ a prime number that satisfy N = 3 mod 4.
- It can be avoided, for double hashing, we pick $N$ as a prime number and we compute the value of delta as $\delta = H_2(k) \text{mod} N$, when $\delta=0$ means we are stuck in a cycle and we set $\delta = 1$

Removing an element means place a unique marker ( **tombstone** ) to indicate that a (k,v) pair has been deleted and that the bucket should be skipped during a search.  Tombstones count as a filled slots in the HT so they increase the load factor but when we are inserting a new key value pair, we can replace buckets with tombstones ( they are useful for the probing sequences , to avoid to loose last elements if we delete an middle element ).

# Graph
It is a collection of nodes and edges ( an edge is a connection between a pair of nodes )
![[Pasted image 20260301113711.png]]
Nodes are just things and edges are just relationships between them.
There are two types of graph:
- Directed Graph $\rightarrow$ edges have a specific direction
	- the relationship is a **one-way street**
- Undirected Graph $\rightarrow$ edges have not a specific direction
	- The relationship is **mutual**
![[Screenshot 2026-03-01 alle 11.39.40.png]]
A neighbour is any node accessible through one edge ( A has B and C has neighbours ).
A graph can be represented in two ways:
- Adjacency matrix
- Adjacency list ( an hashmap with lists as entries ).
![[Screenshot 2026-03-01 alle 11.43.31.png]]
## DFS
Depth First Search/Traversal explores a graph by going **as deep as possible** along each branch before backtracking. It wants to see the end of a path before trying a different one.
![[Screenshot 2026-03-01 alle 11.47.26.png]]
I started from A and i went deep ( going through B and then D coming back to C and then E): i am not able to reach F.
It uses a Stack or Recursion.
We insert in the stack the starting node then the algorithm is the following one:
- Pop a node from the stack
- I print the node
- I insert the neighbours of the node in the stack
And so on until my stack becomes empty.
![[Screenshot 2026-03-01 alle 15.06.51.png]]
![[Screenshot 2026-03-01 alle 15.07.46.png]]
It is possible that we are not able to hit every node of the graph.

Code 
```java
import java.util.*;

public class Main {
    public static void depthFirstPrint(Map<Character, List<Character>> graph, char source) {
        // In Java, we use the Stack class (or Deque for better performance)
        Stack<Character> stack = new Stack<>();
        stack.push(source);

        while (!stack.isEmpty()) {
            char current = stack.pop();
            System.out.print(current + " ");

            // Get neighbors from the map and add to stack
            for (char neighbor : graph.get(current)) {
                stack.push(neighbor);
            }
        }
    }

    public static void main(String[] args) {
        // Representing the graph from your screenshot
        Map<Character, List<Character>> graph = new HashMap<>();
        graph.put('a', Arrays.asList('b', 'c'));
        graph.put('b', Arrays.asList('d'));
        graph.put('c', Arrays.asList('e'));
        graph.put('d', Arrays.asList('f'));
        graph.put('e', new ArrayList<>());
        graph.put('f', new ArrayList<>());

        System.out.println("DFS Output:");
        depthFirstPrint(graph, 'a'); 
        // Note: The order might be 'acebdf' or 'abdfce' depending on 
        // how the stack processes the neighbor list.
    }
}
```

## BFS
Breadth-First Search/Traversal explores a graph layer by layer: it starts at a source node and visits all its immediate neighbors first, then moves on to the neighbors' neighbors, and so on.
It uses a Queue.
![[Screenshot 2026-03-01 alle 11.51.18.png]]
I enqueue the starting node and the algorithm can start:
- We extract/poll the front element of the queue
- We insert the neighbours of the extracted node in the back of the queue 
We do this until the queue is empty.
![[Screenshot 2026-03-01 alle 15.10.10.png]]
![[Screenshot 2026-03-01 alle 15.10.55.png]]

Code:
```java
public static void BFS(Map<Character,List<Character>> graph,Character startingNode)
    {
        LinkedList<Character> queue = new LinkedList<>();
        
        queue.add(startingNode);
        
        while(queue.size() != 0)
        {
            Character currentNode = queue.pollFirst();
            
            System.out.println(currentNode);
            
            for(Character neighbour : graph.get(currentNode))
            {
                queue.add(neighbour);
            }
            
        }
    }
```

## DFS vs BFS
![[BFS-and-DFS-Algorithms.png]]
![[Screenshot 2026-03-01 alle 11.50.56.png]]
If the target is likely near the start, use BFS. If the graph is very deep and the target is at the bottom (or you need to visit every single node anyway), DFS is often cleaner to code using recursion.

For both:
- Space complexity O(V)
	- If we use a the adjacency list
	- O(V^2) for adjacency matrix.
- Time Complexity O(V+E)
V = # nodex
E = # edges

## Common Problems

### Handling Cycles in undirected graphs
When we work with undirected graph and we receive a list of edges, just transform it into a graph:
![[Screenshot 2026-03-01 alle 15.51.22.png]]
When we work with graph just visualizes it to have a better understanding.
![[Screenshot 2026-03-01 alle 15.52.25.png]]
*Starting from the node i we want to understand if we can reach l*
We mark our nodes as visited if we travel through them ( we can do it through a set ).
In this example we use DFS
![[Screenshot 2026-03-01 alle 15.55.04.png]]
After that we select i from the stack, i check if it is present in the set : i understand that i have already visited it and i should not go deep on that path.
![[Screenshot 2026-03-01 alle 15.56.28.png]]

### Handling Cycles in directed graphs
- To detect a cycle in a Directed Graph using **BFS**, you cannot use the standard "visited set" approach. Instead, you must use **Kahn’s Algorithm**.
- To detect a cycle in a Directed Graph using **DFS**, you use the Three-State or Recursion Stack logic.
	- if you encounter a node that is **already in the current path** you are exploring, you’ve found a cycle.
	- We use a
		- visited set to store nodes that have been completely explored ( all their neighbours are finished )
			-  If we hit a node which is already in the visited set, we stop exploring that path.
		- recursion stack to store nodes currently in the active recursion path.
			- If we hit a node which is already in the recStack, there is a cycle.

### Counting Connected Components
*How many islands are in your graph?*
To count the number of connected components, iterate through every node in the graph. If a node has not yet been visited, initiate a traversal (BFS or DFS) starting from that node to mark all reachable nodes as visited. After the traversal of that specific component is complete, increment the component count by one.
![[Screenshot 2026-03-01 alle 16.09.38.png]]
The 2 node is skipped: it has been already visited.
![[Screenshot 2026-03-01 alle 16.10.04.png]]
![[Screenshot 2026-03-01 alle 16.11.59.png]]
Time Complexity is O(V+E)

### Largest Component Problem
We iterate through every node in the graph. If a node has not yet been visited, initiate a traversal (BFS or DFS) starting from that node to mark all reachable nodes as visited and count the number of nodes visited. After the traversal of that specific component is complete, we have the number of nodes for that component and it can be used to understand which one is the largest.
![[Screenshot 2026-03-01 alle 16.17.53.png]]
![[Screenshot 2026-03-01 alle 16.18.40.png]]
Time Complexity is O(V+E)

### Shortest Path Problem with  Unweighted Graph
We want to return the smallest path between two nodes ( in this example between w and z).
![[Screenshot 2026-03-01 alle 16.25.55.png]]
The path length is given by the number of edges.
![[Screenshot 2026-03-01 alle 16.27.34.png]]
We use BFS from the starting node because it guarantees to find the node ( DFS does not guarantee it ): we traverse the graph in layers and we stop when we encounter the target node.
![[Screenshot 2026-03-01 alle 16.33.28.png]]
In our example we just store in the queue both the node and its distance from the starting node.
![[Screenshot 2026-03-01 alle 16.35.07.png]]
Code:
```java
 static class Tuple
    {
        public Character value;
        public int distance;
        
        public Tuple(Character value, int distance)
        {
            this.value = value;
            this.distance = distance;
        }
    }
    
    public static void BFS(Map<Character,List<Character>> graph,Character startingNode, Character target)
    {
        LinkedList<Tuple> queue = new LinkedList<>();
        Set<Character> visited = new HashSet<>();

        queue.add(new Tuple(startingNode,0));
        
        while(!queue.isEmpty())
        {
            Tuple currentNode = queue.pollFirst();
            if(visited.contains(currentNode.value))
            {
                continue;
            }
            visited.add(currentNode.value);
            if(currentNode.value.equals(target))
            {
                System.out.println("Shortest path: " + currentNode.distance);
                return;
            }
            for(Character node : graph.get(currentNode.value))
            {
                queue.add(new Tuple(node, currentNode.distance+1));
            }
        }
    }
```


### Shortest Path Problem with weighted graph
Edges are associated with weights.

#### Dijkstra's Algorithm
It works perfectly if there are not negative weights otherwise it will fail.
Dijkstra is designed to **never re-process** a node. It assumes that if you've reached a node through the currently shortest known path, any other path (which must involve _more_ edges) will only be _more_ expensive.
Negative weights turn that logic upside down: a path with **more** edges can actually be **cheaper**.

Time Complexity is O( (E+V) log V ) if we use an heap as priority queue.
Algorithm:
- We start by associating all the nodes to a distance equal to $\infty$ excepting for the starting node ( its distance is 0 )
![[Screenshot 2026-03-01 alle 17.25.34.png]]
- We put all the nodes into a priority queue ( based on the distance )
- We take the closer node and look at its neighbours. If going through this node is faster than we we previously knew, we update its neighbor's distance ( **Relaxation** process )
	- Once I remove a node from my Priority Queue and mark it as 'Visited', I have found the absolute shortest path to that node. I never need to look at it again.
	- This is true only if we don't have negative weights.
	- It is a greedy approach.
![[Screenshot 2026-03-01 alle 17.26.20.png]]
![[Screenshot 2026-03-01 alle 17.28.04.png]]
![[Screenshot 2026-03-01 alle 17.28.21.png]]
![[Screenshot 2026-03-01 alle 17.28.30.png]]
We extract E but no relaxation can be done ( 30 + 25 > 45 and 30 + 30 > 35 )
![[Screenshot 2026-03-01 alle 17.29.13.png]]
![[Screenshot 2026-03-01 alle 17.29.18.png]]
We repeat it until the queue is empty

To turn your BFS into Dijkstra, you only need three major "upgrades":
1. **Queue → PriorityQueue:** Instead of a simple `LinkedList`, use a `PriorityQueue<Tuple>`. You must tell Java how to compare them (usually by the `distance` field).
	1. In Java, the `PriorityQueue` doesn't have a `decreaseKey` method (which is how the algorithm is taught in textbooks).
	2. When you find a shorter path to a neighbor, you just `add()` a new `Tuple` to the PQ with the smaller distance. The PQ will now have two entries for the same node. When you `poll()` the smaller one, you process it. When you eventually `poll()`the larger, "stale" one, you simply check if its distance is greater than the best distance you've already found—if it is, you **ignore it**.
2. **The "Relaxation" Step:** In BFS, you just check if a node is visited. In Dijkstra, you check: _"Is the distance I just found (dist[u]+weight) smaller than the distance I previously recorded for this neighbor (dist[v])?"_ If yes, you update it. This is called **Relaxation**.
3. **The Distance Map:** Instead of just a `Set<Character>` for visited nodes, you usually use a `Map<Character, Integer>` to store the **best known distance** to every node.

#### Bellman-Ford Algorithm
Bellman-Ford is less "smart" than Dijkstra but much more **robust**. Instead of picking the best node, it just relaxes **every single edge** in the graph over and over again.
Time complexity O(N E)
Algorithm:
- We start by associating all the nodes to a distance equal to $\infty$ excepting for the starting node ( its distance is 0 )
- Iterate over every edge in the graph and perform relaxation for V-1 times  ( the longest possible shortest path in a graph without cycles can only have V-1 edges )
	- We can stop it early if there is no update after the relaxation.
If we run the algorithm for V times ( and not V-1 ) and after performed our last relaxation any distance still decreases, we have a negative cycle.

A directed acycle graph is called DAG.
# Sorting Algorithms
## Merge Sort
It is a Divide and Conquer algorithm: it splits the array in half recursively until we have one single element and then we merge them back together ì
Time complexity O(n log n)
Space Complexity O(n) -> it needs a temporary array to merge

## Quick Sort
It also uses a Divide and Conquer approach but instead of splitting in the middle, it picks a pivot element and partitions the array ( element smaller than the pivot go left, larger go right ).
The average case is O(n log n) but the worst case is O(n^2) that happens if the pivot is the smallest or the highest (if we are in a sorted array ).
Space complexity is O( log n) because it uses a recursion stack.
It is usually faster than Merge Sort because it has better **Cache Locality** and works **In-place** (doesn't need a big extra array).

# Java
It is designed for simplicity and portability , its key feature is write once and run anywhere ( WORA ) which means you can compile you java code and it runs on any platform that supports java without recompiling.
Java is not a pure objected oriented language because in Java not everything is an object ( primitive data types ) while it offers class wrappers for primitive data type.
**Static** means you don't require to create an object of that class to access the method.

*How does a java program work?*
When you write a Java program, you first create a Java source file and it needs to be compiled before it can be run.
The compilation is done through multiple steps:
- Java compiler ( part of JDK ) takes our .java source file and turns it into bytecode.
- The bytecode is stored in .class files and it is pltaform independent
Execution:
- JVM ( Java Virtual Machine ) takes the bytecode and make sure it is run correctly.

The tools of Java are:
- JDK ( Java Development Kit) provides all the tools to create Java applications ( including the compiler )
- JRE ( Java Runtime Environment ) is needed to run the compiled bytecode which includes JVM
- JVM ( Java Virtual Machine ) executes the bytecode ensuring the program runs consistently across different platforms 


 # Laws of clean code
 - **SOLID**: is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin:
	 - S ( Single Responsibility principle ) $\rightarrow$ a class should have one and only one reason to change, meaning that a class should have only one job
		 - In a banking app, if a `TransactionProcessor` is responsible for calculating tax, updating the database, and sending a Push Notification, it violates SRP. Instead, use a Mediator or Service pattern to delegate these tasks to specialized classes like `TaxCalculator` and `NotificationService`.
	 - O ( Open-Closed principle ) $\rightarrow$ Objects or entities should be open for extension but closed for modification.
		 - You have a `PaymentService` that uses a `switch` statement to handle different currencies we should change it to use the Strategy Pattern where we create an interface `PaymentHandler` and we implement a class for each currency.
	 - L ( LSP ) $\rightarrow$  every subclass or derived class should be substitutable for their base or parent class.
		 - You have a base class `Account` with a `withdraw()` method. You create a subclass `FixedDepositAccount`. However, in a fixed deposit, you _cannot_ withdraw money until the term ends. If you make `withdraw()` throw an `Exception`, you’ve broken the parent's contract.
	 - I ( Interface Segregation Principle ) $\rightarrow$ Many client-specific interfaces are better than one general-purpose interface.
		 - General-purpose interfaces should be broken down into smaller, more specific ones. This way, client classes only need to know about the methods that are relevant to them.
	 - D ( Dependency Inversion Principle ) $\rightarrow$ Entities must depend on abstractions, not on concretions.
		 - Imagine you are building a service and you need have a password recovery system that sends a unique reset link to a user via email or SMS. In a traditional your PasswordRecoveryService would directly instantiate a concrete class like DigitalOceanPostmarkMailer or SendGridClient to handle the actual delivery. This creates a rigid dependency where your high-level business logic—the rules for generating tokens and verifying identity—is forced to know the technical details of a low-level infrastructure tool. If the mailing API changes, or if you decide to switch to a different provider for better deliverability rates, you are forced to modify and re-test your core security logic, which violates the goal of stable software. By applying the Dependency Inversion Principle, you invert this relationship so that the PasswordRecoveryService no longer depends on a specific mailer; instead, both the recovery service and the mailer depend on a high-level abstraction, such as an IMessageSender interface. This interface defines a generic contract like 'send(Recipient, Content)' without specifying how the message travels. The PasswordRecoveryService simply calls this method on whatever implementation is provided to it at runtime via constructor injection. This means you can easily swap a DigitalOcean-based mailer for an SMS-based Twilio provider or even a 'MockMailer' for unit testing without changing a single line of your password recovery logic. The high-level policy is protected from changes in low-level details, ensuring that your core service remains robust, decoupled, and easily maintainable as your infrastructure evolves on the cloud
		 - Entities should depend on abstraction and not concrete implementation technology related.
- **DRY (Don't Repeat Yourself)**: Minimizing redundancy through abstractions.
- **KISS (Keep It Simple, Stupid)**: Avoiding "over-engineering" where a simple `if` statement would suffice over a complex design pattern
- **YAGNI (You Ain't Gonna Need It):** Don't add functionality until it's actually necessary
- **Separation of Concerns (SoC):** A program should be split into distinct sections, each addressing a separate concern
- 
# Essential Design Patterns (GoF)
Design patterns in Java refer to structured approaches involving objects and classes that aim to solve recurring design issues within specific contexts. 
These patterns offer reusable, general solutions to common problems encountered in software development, representing established best practices.
There rare three types of Design Patterns:
- Creational patterns $\rightarrow$  focus on efficient and flexible object creation
	- Singleton pattern: ensures a class has only one instance and provides a global point of access ( used for a database connection manager )
	- Factory pattern: provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
	- Prototype pattern: creates new objects by cloning existing instances instead of instantiating new ones (creating an object can be time consuming )
	- Builder pattern: building a complex object step-by-step instead of stuffing 15 arguments into a single constructor.
	- Abstract pattern: provides an interface to create families of related objects without specifying their concrete classes
![[Screenshot 2026-03-07 alle 09.53.04.png]]
- Structural Design Patterns  $\rightarrow$ define how classes and objects are combined to form larger, flexible structures
	- Adapter pattern: allows incompatible interfaces to collaborate by creating a wrapper (adapter) around an existing class.
	- Bridge pattern: splitting a massive class into two separate pieces (the remote control and the TV) so you can upgrade one without breaking the other ( you can have different TV that works with the same remote control)
	- Composite pattern: lets you compose objects into tree structures and then work with these structures as if they were individual objects.
	- Decorator pattern: lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
	- Facade pattern: provides a simplified interface to a complex subsystem
	- Flyweight pattern: minimizes RAM memory use by sharing common object data instead of creating duplicates
	- Proxy pattern: provides a surrogate or placeholder to control access to another object.
- Behavioral Design Patterns $\rightarrow$ patterns that focus on how objects and classes interact and communicate in software development
	- Observer pattern: a subscription model. When one thing changes, it automatically yells out to notify everyone who subscribed to it.
	- State pattern: allows an object to change behavior dynamically when its internal state changes.
	- Command pattern: encapsulates a request as an object to parameterize clients and support undo/redo. ( e.g. a restaurant order )
	- Chain of Responsibility pattern: passes a request along a chain of handlers until one processes it
		- Support. You call in and get an automated bot. The bot can't help, so it passes you to a Level 1 human agent. They can't help, so they pass you to a Level 2 Manager. The request travels down the chain until it's handled.
	- Strategy pattern: defines a family of algorithms and makes them interchangeable at runtime.
	- Template pattern: defines the skeleton of an algorithm , letting subclasses override specific step.
		- Building a house. The template says: 1. Pour foundation, 2. Build walls, 3. Add roof. You _cannot_ change that order (you can't add a roof before the walls). But, subclasses can choose to build brick walls instead of wood walls, or a metal roof instead of shingles

# Big Three Architecture Patterns
- **Monolithic** refers to a traditional approach where an application is built as a single, tightly-coupled unit. All components, modules, and functionalities reside within the same codebase and are deployed as a single unit. While it offers simplicity and ease of development, it can become challenging to scale and maintain as the application grows.
- **Microservices Architecture** is an architectural style that structures an application as a collection of services that are  Independently deployable, Highly maintainable and testable, Loosely Decoupled and organized around business capabilities ( DDD - Domain Driven Design )
	- Services can talk by using sychronous (  the caller sends a request and waits for a response, it uses REST or gRPC ) or asynchronous (The caller sends a message and moves on. It doesn't wait. Uses Message Brokers like Kafka/RabbitMQ.) techniques
	- SAGA Pattern:a sequence of local transactions. Each local transaction updates the database and triggers the next step. If one step fails, the Saga executes "undo" steps (compensating transactions) to reverse the previous successful steps.
- **Hexagonal Architecture**  also known as Ports and Adapters architecture, emphasizes the separation of concerns by structuring the application around the core business logic. The core is shielded from external dependencies, such as frameworks or databases, through ports and adapters.
- **Layered Architecture**  divides an application into distinct layers, each responsible for a specific set of functionalities. These layers typically include presentation, business logic, and data acces

# CQRS ( Command Query Responsibility Segregation )
It splits the application into two distinct parts:
- Commands: change the state of the system through create/update/delete operation and they do not return data ( just success/Fail or an ID )
- Queries: return data but do not change the state.

Why use it?
- **Independent Scaling:** In most apps, reads happen 100x more often than writes. CQRS allows you to scale your "Read" database (like Elasticsearch or a NoSQL cache) independently from your "Write" database (Relational/ACID).
- **Optimized Schemas:** Your write model is optimized for transaction integrity (normalized), while your read model is optimized for fast UI rendering (denormalized).
- **Security:** It’s easier to ensure only the right people are executing commands when they are isolated from query logic.


# Dynamic Programming
We solve problem using DP by first identifying and solving subproblems and then bring subproblem results together to solve larger problems.
We will see how to use it through some examples:
1. **LIS** ( Longest Increasing Subsequence )
Given a sequence $a_1, a_2 , . . . , a_n$ we want to find the length of the longest increasing subsequence $a_{i_1} , a_{i_2} , . . . a_{i_k}$ where
$$
a_{i_1} < a_{i_2} < . . . < a_{i_k}
$$
$$
i_1 < i_2 < . . . < i_k
$$
![[Screenshot 2026-03-22 alle 18.03.41.png]]

**Step for solving a DP problem**:
	1. Visualize Examples ( sometimes it is useful to write down that as a graph )
	![[Screenshot 2026-03-22 alle 18.05.47.png]]
	2. Find an appropriate subproblem ( simpler version of our overall problem )
	In this case compute the LIS of a window that has always the same start index and a moving end index ( k ) .
	We want to compute LIS[k]
	3. Find relationships among subproblems
	For computing LIS[4] we need LIS[0] , LIS[1] , LIS[2] and LIS[3].
	![[Screenshot 2026-03-22 alle 18.11.05.png]]
	4. Generalize the relationships
	![[Screenshot 2026-03-22 alle 18.12.21.png]]
	5. Implement by solving subproblems in order
	![[Screenshot 2026-03-22 alle 18.13.46.png]]

In this case to get the actual sequence we need to keep track of previous indices.

2. Box Stacking
Given n boxes $[(L_1,W_1, H_1) , (L_2,W_2,H_2) , .... ,(L_n,W_n,H_n)]$ where box $i$ has length $L_i$, width $W_i$ and height $H_i$. Find the height of the tallest possible stack with the constrain that a box can be on top of box if its width W and length L are smaller. 
![[Screenshot 2026-03-22 alle 18.21.55.png]]
Steps:
	1. Visualize Examples 
![[Screenshot 2026-03-22 alle 18.23.05.png]]
	2. Find an appropriate subproblem
Select the highest box between the available ones.
	3. Find relationships among subproblems
We add the maximum height of on top boxes plus the current height of the box.
![[Screenshot 2026-03-22 alle 18.29.44.png]]
	4. Generalize the relationship
![[Screenshot 2026-03-22 alle 18.30.21.png]]
	5. Implement by solving subproblems in order
We sort boxes by length or width.
Solution:
![[Screenshot 2026-03-22 alle 18.32.55.png]]


# Prompting Engineering
*Prompting* is the process of providing specific instructions to a generative AI tool to receive new information ( or to achieve a desired outcome on a task )

*Prompting Engineering* involves human writing, refining and optimizing prompts in a structured way.
It is done with the intention to improve the interaction between humans and AI.

Generative AI techniques can create realistic text responses and even images, music and other media thanks to the huge amounts of training data.

LLMs are trained with tons of books, articles websites and they take as input images or text: they compute the relation between words ( e.g. their order and how they fit together ) and try to define their meanings. Then the LLM would generate a prediction or a continuation of the sentence that makes sense based on its understanding of the language.
The first LLM was ELIZA ( created at MIT ) from 1964 to 66 designed to simulate a conversation with an human being ( it did not understand truly what we are saying : it used pattern matching with some algorithm to create the illusion of understanding , in reality it was just following a set of predefined rules ). 
True LLMs come into play in 2010 with deep learning and neural networks: we know GPT which stands for Generative Pre-trained Transformer. 
Right now we have different types of LLMs:
![[Screenshot 2026-03-22 alle 23.20.12.png]]

*How to use GPT-4?*
GPT-4 processes all texts in chunks called **tokens** ( approximately 4 characters or 0.75 words for english text ): we are charged by tokens when we are using APIs or ChatGPT ( we can use the tokenizer app to understand how many tokens we are using ).

*Best Practises: TCREI framework*
5 Step framework for how to design a prompt:
1. Task ( what you want the AI to do )
	1. We can add a persona: we are asking the AI to respond you as a certain character (e.g. act as a finance expert )
	2. We can specify the format of the output ( limiting words or specifying if we wanna a summary or detailed explanation )
	3. We want to avoid leading the answer ( It may bias the response )
	4. Add constraints ( it is harder when the research space is very huge )
	5. We can also break our prompt into simpler sentences
![[Screenshot 2026-03-22 alle 23.56.37.png]] 
2. Context ( tumble rule : more context we can provide the better the output will be )
3. References ( we can provide examples to the AI )
4. Evaluate ( we understand if the output is what we need )
5. Iterate ( if the evaluation was not fully positive , which happens so often because the process itself is circular )

*Multimodal Prompting*
We can interact with LLMs with different modalities as pictures, audio , video and even code. We can use the same framework seen above ( TCREI ) we need just to be a bit more careful about specifying what kind of input/output we are looking for and the context

*Major issues with using AI tools*
1.  *AI Hallucination*: when a LLM generates false information when it misinterprets data ( there can be conflict data )
2. *Biases*: AI systems are trained on human-generated content and it often inherits the biases present in that content included those related to gender and race
To avoid these problems we need always to check our outputs by verifying whatever the Gen AI gives us.
This is a checklist:
- Evaluate suitability : check if AI fits the task
- Get approval: obtain company consent before using AI on projects
- Protect privacy use secure tools and avoid exposing sensitive data
- Validate Outputs: review all AI-generated content before sharing
- Be transparent: disclose AI use to teams and clients.

*Prompting Techniques*:
- Prompt chaining: it guides ai tool through series of interconnected prompts, adding new layers of complexity along the way
	- Uses the output of a prompt for the next prompt
- Chain of thought ( COT ) prompting: ask to the AI to explain his reasoning as a step by step process
	- It forces the AI to decompose complex problems in subproblems and to show its reasoning
- Tree of thought prompting: it allows to explore multiple reasoning paths simultaneously ( we want to find the best option)
	- E.g. you ask for three options, you select one and you ask much more options for that and so on
- Meta prompting: asking the AI to create a prompt.
- Zero-shot prompting: we ask a task without providing any examples
- Few-show prompting: we ask a task and we provide examples of input/output 
	- Iterative prompting: fine-tuning of the prompt based on the results until we get the final and correct output from the LLM

*Vectors/Text Embedding* 
In machine learning and NLP ( Natural Language Processing ) text embedding is a popular technique to represent textual information in a format that can be easily processed by algorithm ( especially by deep learning models ).
It means converting text into a high dimensional vector that captures its semantic information ( meaning behind the words )
![[Screenshot 2026-03-22 alle 23.42.57.png]]
It is done in order to apply algorithms and operations on them ( it allows to define the concept of similarity between words ).

*AI Agent*
An AI agent is like an expert designed to help with tasks and answer questions ( e.g. coding agent as claude code, marketing agent , learning agent ecc... )


*RAG*
LLMs are trained on internet data, RAG are used to take domain-specific knowledge to the model:
- The retriever brings the context of our domain knowledge base to the generated part of the LLM
When we ask questions to the LLM, it is now responding to our questions baed on the domain specificity of our content
![[Screenshot 2026-03-23 alle 00.41.53.png]]
e.g. the retriever can be really simple as a vector database.
The retriever gives internal information useful to respond specific and internal questions for the LLM.