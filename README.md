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

To generate test reports and coverage:

```
pytest test_calculator.py -v --cov=calculator --cov-report=xml --html=pytest_report.html --self-contained-html
```

## CI/CD

This project includes a GitHub Actions workflow that:
1. Clones the repository
2. Sets up Python
3. Installs dependencies
4. Runs tests with coverage analysis
5. Generates HTML test reports and XML coverage reports
6. Uploads the reports as artifacts that can be downloaded from the GitHub Actions run

The workflow runs automatically on pushes to the main branch and pull requests. 