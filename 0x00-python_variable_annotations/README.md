# Python Annotations README

## Introduction

Annotations in Python are used to provide hints or metadata about the types of variables, function parameters, and return values. They are a way to document and enforce the expected types in your code, which can improve code readability and catch type-related errors early.



## Type Hinting

Type hinting is the practice of adding annotations to variables, function parameters, and return values to indicate their expected types. Type hints are not enforced at runtime but can be used by code analysis tools to check for type-related errors.

### Basic Type Hints

```python
# Variable annotation
x: int = 5

# Function parameter and return type annotations
def add(a: int, b: int) -> int:
    return a + b
