# Algorithms and Data Structures: A Learning Journey

My notes on concepts covering algorithms and data structures, as well as solved Leetcode problems.

---

## Table of Contents
* [Introduction to Data Structures](#introduction-to-data-structures)

---

## Introduction to Data Structures
[**Basics**](#basics) • [**Stacks**](#stacks) • [**Linked List**](#linked-list)

### Basics
A data structure is a way to store data.

#### Types of Data Structures
1. **Linear Data Structures**
   - Elements are arranged in sequential order.
   - Easier to implement for less complex use cases.
   - **Arrays**: Elements are arranged in continuous memory; all elements are of the same type.
   - **Stacks**: Elements stored in LIFO (Last In First Out).
   - **Queues**: Elements stored in FIFO (First In First Out).
   - **Linked List**: Elements connected through a series of nodes, where each node contains an item and address to the next node.

2. **Non-Linear Data Structures**
   - Non-sequential and arranged in hierarchical order.
   - One element can be connected to one or multiple elements.
   - **Graphs**: Each node is called a vertex and vertices are connected via edges.
   - **Trees**: Similar to graphs, but there can only be one edge between two vertices.

| Feature | Linear Data Structures | Non-Linear Data Structures |
| :--- | :--- | :--- |
| **Order** | Sequential | Non-Sequential |
| **Hierarchy** | Single layer | Multiple layers |
| **Traversal** | Traversed in a single run | Requires multiple runs |
| **Memory** | Inefficient utilization | Relatively efficient utilization |
| **Complexity** | Time complexity increases with data | Time complexity remains the same/stable |

![](https://github.com/mekanbaymyradov/dsa/Resources/images/DST-neetcode.jpg)
---

### Stacks
A linear data structure that follows the principle of **LIFO (Last In First Out)**—the last element added to the stack is the first one to be removed.

#### Key Concepts
* **PUSH**: Add an element to the top of the stack.
* **POP**: Remove an element from the top of the stack.
* **IsEmpty**: Check if the stack is empty.
* **PEEK**: Check the value of the top element without removing it.


#### Implementation in Python
There are two primary ways to implement stacks in Python:

**1. List-Based Implementation**
* Python lists are dynamic arrays that resize automatically.
* **Pros**: Simple and easy to use with `append()` and `pop()`.
* **Cons**: **Amortized cost.** While $O(1)$ average, resizing can cause occasional $O(n)$ operations. Memory overhead can be wasteful as lists allocate extra space for future growth.

**2. Deque-Based Implementation**
* Implemented as a doubly linked list via `collections.deque`.
* **Pros**: Guaranteed $O(1)$ operations for append and pop. More memory efficient (no over-allocation).
* **Cons**: Does not support random access by index like lists.

**Summary**: Lists are sufficient for most stack use cases unless you need guaranteed $O(1)$ for all operations, in which case a **deque** is better.
* **Space Complexity**: $O(n)$

### Linked List
