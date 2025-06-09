# AGENTS Instructions

These rules guide automated coding agents working in this repository.

## General Guidelines
- Use **Python 3.11** features and follow PEP 8.
- Prefer the `sqlalchemy` ORM when interacting with PostgreSQL.
- Format all Python files with `black` and sort imports with `isort`.
- Lint code with `flake8` and run tests using `pytest` before committing.
- Document public functions with docstrings.

## Repository Commands
Run the following commands before each commit:

```bash
isort .
black .
flake8
pytest
```

Use these steps even if no tests are present to ensure code quality.
