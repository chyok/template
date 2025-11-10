# FastAPI 3-Tier Architecture Template

This is a template project for building FastAPI applications using a clean, scalable, and interface-driven 3-tier architecture.

## Core Concepts

This template is designed to enforce a strong separation of concerns, making the application easier to test, maintain, and scale.

- **Interface-Driven Design**: Both the Service and Repository layers are defined by interfaces (Abstract Base Classes). This allows for implementations to be easily swapped out, which is great for testing (e.g., swapping a real database repository with a mock repository) and for adapting the application to new requirements.

- **Dependency Injection**: The project heavily utilizes FastAPI's `Depends` system to manage dependencies. This Inversion of Control (IoC) approach means that components declare their dependencies, and the framework provides them. This makes the code decoupled and highly testable.

- **Clear Separation of Concerns**:
  - **API Layer** (`src/api`): Handles HTTP routing, request validation, and response serialization. It knows nothing about how data is stored or manipulated.
  - **Service Layer** (`src/service`): Contains the core business logic. It orchestrates data from repositories and performs operations. It is completely independent of the web layer.
  - **Repository Layer** (`src/repository`): Manages data access. Its only responsibility is to query and persist data, abstracting the underlying data source from the rest of the application.

## Project Structure

```
.
├── src
│   ├── api
│   │   └── v1
│   ├── repository
│   │   ├── abc
│   │   └── item.py
│   ├── schema
│   │   ├── model
│   │   ├── request
│   │   └── response
│   └── service
│       ├── abc
│       └── item.py
├── tests
│   └── service
│       └── test_item.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Getting Started

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    The project uses `pyproject.toml` to manage dependencies. To install all dependencies, including development tools like `pytest`, run:
    ```bash
    pip install '.[dev]'
    ```

### Running the Application

To run the web server, use `uvicorn`:
```bash
uvicorn src.main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### Running Tests

To run the unit tests, use `pytest`:
```bash
pytest
```
