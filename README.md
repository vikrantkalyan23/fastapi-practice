# FastAPI Practice

API development with Python and FastAPI.

## What is FastAPI?

[FastAPI](https://fastapi.tiangolo.com/) is a Python framework for building APIs using standard Python type hints. It uses Starlette for web functionality and Pydantic for data validation and serialization.

Routes use decorators such as `@app.get()` and `@app.post()`. Parameter types and Pydantic models help validate requests and generate an OpenAPI schema, Swagger UI, and ReDoc documentation. FastAPI supports both regular `def` and asynchronous `async def` route functions.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
```

## Repository examples

| Folder | Topics |
| --- | --- |
| `1_get-api/` | GET routes, path parameters, and query parameters |
| `2_post-api/` | POST requests, request bodies, and nested Pydantic models |
| `3_todo-app/` | Create, read, update, and delete todos |

The todo example stores data in memory; restarting the server clears it.

## Getting started

Install Python 3 and open a terminal in the repository root. Choose either setup option below. Both use an isolated `.venv` directory for dependencies.

### Option 1: venv and pip

Create the environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

With the environment active, install FastAPI and Uvicorn, the ASGI server that runs the application:

```bash
python -m pip install fastapi uvicorn
```

### Option 2: uv

[uv](https://docs.astral.sh/uv/) manages Python packages and virtual environments. Install it using the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
uv venv .venv
uv pip install --python .venv fastapi uvicorn
```

Activate `.venv` using the command for your operating system shown above. This uses uv's pip interface and does not require a `pyproject.toml`.

See the official guides for [FastAPI virtual environments](https://fastapi.tiangolo.com/virtual-environments/) and [uv environments](https://docs.astral.sh/uv/pip/environments/).

### Run an example

With the environment active, run one of these commands from the repository root:

```bash
# GET API example
python -m uvicorn main:app --app-dir 1_get-api --reload

# POST API example
python -m uvicorn index:app --app-dir 2_post-api --reload

# Todo CRUD example
python -m uvicorn main:app --app-dir 3_todo-app --reload
```

Run one server at a time; press `Ctrl+C` before starting another. In `main:app`, `main` is the Python module and `app` is the FastAPI instance. `--app-dir` selects the example folder. `--reload` restarts the server after code changes and is for development.

Open:

- API: <http://127.0.0.1:8000> (the GET example has a `/` route)
- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

Use **Try it out** in Swagger UI to send requests. Run `deactivate` to leave the virtual environment after stopping the server.

## Use cases

- **REST APIs:** backends for web and mobile applications.
- **Microservices:** focused services that communicate over HTTP.
- **Machine learning APIs:** validate inputs and return model predictions.
- **Internal tools:** APIs for dashboards, automation, and integrations.
- **I/O-heavy services:** concurrent database and HTTP requests using asynchronous libraries.
- **Real-time features:** WebSockets for live updates or messaging.

CPU-heavy work may need separate processes or workers. Using `async def` alone does not speed up CPU-bound code.

## Comparison with other Python frameworks

This is a practical selection guide. Performance depends on application code, database access, and deployment.

| Aspect | FastAPI | Flask | Django |
| --- | --- | --- | --- |
| Main focus | APIs using Python type hints | Lightweight, flexible web applications | Full-featured, database-driven web applications |
| Validation | Integrated through type hints and Pydantic | Usually manual or added through extensions | Forms and model validation; APIs commonly use an additional toolkit |
| API documentation | Automatic OpenAPI, Swagger UI, and ReDoc | Usually requires extensions | Usually requires an API toolkit such as Django REST Framework |
| Database and admin | Integrate your chosen tools | Integrate extensions and database tools | Built-in ORM, migrations, and admin |
| Async support | ASGI-based with async routes | WSGI-based; async views have limitations | ASGI and async views; some components remain synchronous |
| Typical fit | Typed APIs and concurrent I/O services | Small apps and services needing flexible choices | Apps needing integrated database, authentication, and admin features |

See the official [FastAPI](https://fastapi.tiangolo.com/), [Flask](https://flask.palletsprojects.com/en/stable/), and [Django](https://docs.djangoproject.com/en/stable/intro/overview/) documentation.

## Pros and cons

### Pros

- **Less boilerplate:** type hints and Pydantic models describe and validate inputs.
- **Automatic documentation:** interactive docs help developers explore endpoints.
- **Editor support:** types improve autocomplete and readability.
- **Async support:** integrates with asynchronous database drivers and HTTP clients.
- **Flexibility:** choose database, authentication, and deployment tools for your needs.

### Cons

- **More integration decisions:** ORM, migrations, and admin tools require additional setup.
- **Async requires care:** blocking operations inside async routes can stall the event loop.
- **Learning curve:** type hints, Pydantic, dependency injection, and ASGI take practice.
- **Validation has limits:** business rules, authorization, and database constraints still need implementation.
- **Production setup:** persistence, secrets, logging, monitoring, and deployment need configuration beyond these examples.
