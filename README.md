# Data Structures and Algorithms Learning Journey

Hi!   
In this repository, I document my Data Structures and Algorithms (DSA) learning journey.  
I use this repo to store notes, learning resources, and code implementations in one place. 
Good luck on our DSA journey! 

## My notes on concepts covering data structures and algorithms.
- [Introduction to Data Structures](#introduction-to-data-structures)

## Introduction to Data Structures

- [Why Data Structures Matter?](#why-data-structures-matter)
- [Basics](#basics)

### Why Data Structures Matter?

When we learn to code our focus is getting code run properly. Our code measured using one simple metric: does the code actually work?

As software engineers gain more experience, though, we begin to learn about additional layers like the *quality* of code. We learn that there can be two snippets of code that both accomplish the same task, but that one snippet is better than the other.

There are numerous measures of code quality. One important measure is code maintainability. Maintainability of code involves aspects such as the readability, organization, and modularity.

However, there’s another aspect of high-quality code, and that is code efficiency. For example, we can have two code snippets that both achieve the same goal, but one runs faster than the other.

Take a look at these two functions, both of which print all the even numbers from 2 to 100:

```python
def print_even_numbers_v1():
    number = 2

    while number <= 100:
        # If number is even print it:
        if number % 2 == 0:
            print(number)

        number += 1


def print_even_numbers_v2():
    number = 2
    
    while number <= 100:
        print(number)

        # Increase the number by 2, which means next even number
        number += 2
```

Version 2 will runs faster. This is because Version 1 ends up looping 100 times, while Version 2 only loops 50 times.

The first step in writing fast code is to understand what data structures are and how different data structures can affect the speed of our code. 

### Basics

- Data is broad term that refers to all types of information. *Data Structures* are storage used to store and orginize the data. Depending on how we choose to organize our data, our program may run faster or slower. 



