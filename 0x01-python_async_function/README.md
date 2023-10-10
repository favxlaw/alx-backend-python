# Asynchronous Programming with asyncio and Random Module

Tasks here are on asynchronous programming using Python's `async` and `await` syntax, how to execute async programs with the `asyncio` library, run concurrent coroutines, create asyncio tasks, and utilize the `random` module for various applications.

## Asynchronous Programming and Async/Await Syntax

Python's `async` and `await` syntax allows you to write asynchronous code that doesn't block the program's execution, enabling more efficient use of resources and parallelism. Here's a simple example of async syntax:

```python
import asyncio

async def example_coroutine():
    await asyncio.sleep(1)
    print("Async code executed after 1 second")

async def main():
    await example_coroutine()

if __name__ == "__main__":
    asyncio.run(main())
