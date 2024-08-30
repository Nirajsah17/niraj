---
title: Python and Javascript Stack Snippet
description: A collection of useful Python code snippets for various tasks.
author: nirajkumar
date: Aug 30, 2024
tags: python, code snippets, programming
---

# Python and Javascript Stack Snippet 🐍📜

Welcome to my collection of Python and JavaScript code snippets! This repository contains a variety of code examples for common programming tasks, algorithms, data structures, and more. Whether you're a beginner or an experienced developer, you'll find something useful here to enhance your coding skills.

## Table of Contents

- [Overview](#overview)
- [Python Snippets](#python-snippets)
- [JavaScript Snippets](#javascript-snippets)
- [Algorithms](#algorithms)
- [Data Structures](#data-structures)
- [Web Development](#web-development)
- [Machine Learning](#machine-learning)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository serves as a reference guide for Python and JavaScript developers looking to improve their coding skills and learn new concepts. The code snippets cover a wide range of topics, including string manipulation, list operations, sorting algorithms, data structures, web development, and machine learning.

## Python Snippets

### 1. Reverse a String

```python
def reverse_string(s):
    return s[::-1]
```

### 2. Check for Anagrams

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

### 3. Find the Maximum Element in a List

```python
def find_max(lst):
    return max(lst)
```

## JavaScript Snippets

### 1. Reverse an Array

```javascript
function reverseArray(arr) {
    return arr.reverse();
}
```

### 2. Check for Palindromes

```javascript
function isPalindrome(str) {
    return str === str.split('').reverse().join('');
}
```

### 3. Find the Minimum Element in an Array

```javascript
function findMin(arr) {
    return Math.min(...arr);
}
```

## Algorithms 

### 1. Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### 2. Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

## Data Structures

### 1. Stack Implementation

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
```

### 2. Queue Implementation

```python
from collections import deque 

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0
```


## Web Development

### 1. Simple HTTP Server in Python

```python
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
```


### 2. Fetch API in JavaScript

```javascript
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

## Machine Learning

### 1. Linear Regression in Python

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression().fit(X, y)
print("Intercept:", model.intercept_)
print("Slope:", model.coef_)
```

### Utility Functions

<!-- Github GIST embed URL -->
<script src="https://gist.github.com/Nirajsah17/1563a5021bbc7893e0e2b1cf371e4ac5.js"></script>

<script src="https://gist.github.com/Nirajsah17/52c8c4c2c7c62e89a2a47191a979a489.js"></script>



### References

[python Github tutorials](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)
