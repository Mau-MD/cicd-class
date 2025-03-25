# Simple Calculator

A simple Python calculator library with basic arithmetic functions and tests.

## Functions

- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract b from a
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide a by b (raises ZeroDivisionError if b is 0)

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests manually:

```
pytest test_calculator.py -v
```

## CI/CD

This project includes a GitHub Actions workflow that:
1. Clones the repository
2. Sets up Python
3. Installs dependencies
4. Runs tests
5. Reports test results

The workflow runs automatically on pushes to the main branch and pull requests. 