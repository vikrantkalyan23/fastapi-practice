# FastAPI Development

------------------------------------------------------------------------

## Table of contents

-   [1. What is FastAPI?](#1-what-is-fastapi)
-   [2. How a FastAPI application
    works](#2-how-a-fastapi-application-works)
-   [3. What can you build with
    FastAPI?](#3-what-can-you-build-with-fastapi)
-   [4. FastAPI compared with other Python
    frameworks](#4-fastapi-compared-with-other-python-frameworks)
-   [5. Pros and cons](#5-pros-and-cons)
-   [6. Prerequisites](#6-prerequisites)
-   [7. Install uv](#7-install-uv)
-   [8. Create a project with uv](#8-create-a-project-with-uv)
-   [9. Understand the important
    files](#9-understand-the-important-files)
-   [10. Create your first API](#10-create-your-first-api)
-   [11. Start, stop, and run the
    server](#11-start-stop-and-run-the-server)
-   [12. Test the API and view
    documentation](#12-test-the-api-and-view-documentation)
-   [13. Add dependencies and manage Python
    versions](#13-add-dependencies-and-manage-python-versions)
-   [14. Debugging](#14-debugging)
-   [15. Testing](#15-testing)
-   [16. Code quality and formatting](#16-code-quality-and-formatting)
-   [17. Environment variables and
    secrets](#17-environment-variables-and-secrets)
-   [18. Recommended project
    structure](#18-recommended-project-structure)
-   [19. Database integration](#19-database-integration)
-   [20. Build, lock, sync, and deploy](#20-build-lock-sync-and-deploy)
-   [21. Docker quick start](#21-docker-quick-start)
-   [22. Common commands cheat sheet](#22-common-commands-cheat-sheet)
-   [23. Common beginner errors](#23-common-beginner-errors)
-   [24. Learning roadmap](#24-learning-roadmap)
-   [25. Official resources](#25-official-resources)

------------------------------------------------------------------------

## 1. What is FastAPI?

**FastAPI is a Python web framework for building APIs**, especially
HTTP/REST APIs. It lets you expose Python functions as endpoints that
web applications, mobile apps, other services, or AI systems can call.

Example: a Next.js frontend sends a request to a FastAPI backend. The
backend validates the input, runs business logic, optionally queries a
database or ML model, and returns JSON.

### Main features

-   **Type-driven validation:** Python type hints and Pydantic models
    describe and validate request data.
-   **Automatic API documentation:** OpenAPI schema, Swagger UI
    (`/docs`) and ReDoc (`/redoc`).
-   **Async support:** supports both `async def` and regular `def`
    endpoint functions.
-   **Dependency injection:** reusable dependencies for authentication,
    database sessions, configuration, and more.
-   **Standards-based:** uses HTTP and OpenAPI/JSON Schema standards.
-   **Python ecosystem:** works well with data science, machine
    learning, NLP, computer vision, and LLM libraries.

FastAPI is built on **Starlette** for web capabilities and **Pydantic**
for data validation and serialization.

### FastAPI is not

-   A database; you connect it to PostgreSQL, MySQL, MongoDB, or another
    data store.
-   A frontend framework; use React, Next.js, Vue, mobile apps, or
    another client.
-   A machine learning model; it can expose a trained model through an
    API.
-   A complete all-in-one application suite like Django; many components
    such as ORM choice, migrations, task queues, and admin UI are
    selected separately.

------------------------------------------------------------------------

## 2. How a FastAPI application works

``` text
Browser / React / Next.js / Mobile / Another service
                         |
                      HTTP/JSON
                         |
                  ASGI server
                 (Uvicorn)
                         |
                    FastAPI app
                         |
          Routing + validation + dependencies
                         |
                 Business logic/services
                    /           \
              Database       ML / LLM / APIs
                    \           /
                     JSON response
```

### Important terms

  -----------------------------------------------------------------------
  Term                                Meaning
  ----------------------------------- -----------------------------------
  **Endpoint / route**                A URL and HTTP method handled by
                                      your application,
                                      e.g. `GET /products`.

  **ASGI**                            The asynchronous server interface
                                      used by modern Python web
                                      applications.

  **Uvicorn**                         An ASGI server that runs the
                                      application.

  **Pydantic**                        Defines and validates structured
                                      data.

  **OpenAPI**                         A standard description of the API
                                      that powers generated documentation
                                      and client tooling.

  **Dependency injection**            A way to provide reusable objects
                                      or services to route handlers.

  **Middleware**                      Code that wraps request/response
                                      processing, e.g. CORS, timing, or
                                      request IDs.

  **CRUD**                            Create, Read, Update, Delete
                                      operations.
  -----------------------------------------------------------------------

### A first example

``` python
from fastapi import FastAPI

app = FastAPI(title="Learning API")


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}
```

The decorator `@app.get("/")` registers a handler for HTTP GET requests
at `/`. Returning a Python dictionary produces a JSON response.

------------------------------------------------------------------------

## 3. What can you build with FastAPI?

  -----------------------------------------------------------------------
  Application type        Example                 Fit
  ----------------------- ----------------------- -----------------------
  REST APIs               Product, customer,      Excellent
                          order, and user         
                          endpoints               

  Backend for web/mobile  React or Next.js        Excellent
  apps                    frontend with a Python  
                          backend                 

  AI/ML inference APIs    Serve a saved           Excellent
                          scikit-learn, PyTorch,  
                          or TensorFlow model     

  Generative AI / RAG     Chat endpoint, document Excellent
                          search, embeddings,     
                          retrieval pipeline      

  Microservices           Separate services for   Excellent
                          recommendations,        
                          inference, or document  
                          processing              

  Data processing         Validation,             Good
  services                transformation,         
                          analytics, and ETL      
                          triggers                

  Webhooks and            Receive payment, CRM,   Good
  integrations            or external-service     
                          callbacks               

  Internal tools          Admin APIs, automation  Good
                          endpoints, internal     
                          dashboards' backend     

  Real-time applications  WebSockets and          Possible; design
                          streaming endpoints     capacity and lifecycle
                                                  carefully

  Traditional             Templates, CMS, admin   Often Django is a
  content-heavy website   screens, user           better starting point
                          management,             
                          server-rendered pages   

  Small scripts and       Local automation        Usually use a regular
  command-line tools      without an HTTP API     Python script or Typer
                                                  instead
  -----------------------------------------------------------------------

### Example AI/ML use cases

-   Serve a temperature forecasting model through `POST /predict`.
-   Expose document extraction or image classification.
-   Build an embeddings endpoint and a retrieval-augmented generation
    (RAG) API.
-   Add an AI service beside an existing Node.js/NestJS application.
-   Create an API that queries PostgreSQL/pgvector and calls an LLM
    provider.

**Important:** loading a large ML model inside every request or every
worker can consume substantial RAM/VRAM. Consider model lifecycle
management, worker count, batching, timeouts, and separate inference
services.

------------------------------------------------------------------------

## 4. FastAPI compared with other Python frameworks

No framework is universally best. Choose based on the application rather
than benchmark claims alone.

  ---------------------------------------------------------------------------------
  Framework         Best suited for    Strengths         Trade-offs
  ----------------- ------------------ ----------------- --------------------------
  **FastAPI**       APIs, AI/ML        Automatic         You choose many
                    services, typed    validation and    surrounding components;
                    request/response   API docs; async   not a built-in full-stack
                    contracts          support; concise  admin/ORM solution
                                       route definitions 

  **Django**        Full web           ORM, migrations,  More conventions and
                    applications,      admin site,       framework surface area;
                    content sites,     authentication    may be more than a small
                    business           and many          API needs
                    applications       integrated        
                                       features          

  **Flask**         Small services,    Minimal core,     Validation, API schemas,
                    prototypes, simple flexible, mature  and architecture commonly
                    web apps           ecosystem         need additional libraries
                                                         and decisions

  **Starlette**     Lightweight ASGI   Minimal ASGI      Lower-level; you assemble
                    applications and   toolkit;          more of the API
                    framework building underpins FastAPI validation/documentation
                    blocks                               layer yourself

  **Litestar**      APIs and service   Typed handlers,   Smaller ecosystem and
                    applications       dependency        community footprint than
                    wanting more       injection, API    some established
                    built-in structure docs, broader     alternatives
                                       built-in features 

  **Sanic**         Async-first web    Async-oriented    Different conventions and
                    services where its server and web    ecosystem; evaluate
                    ecosystem fits     framework         project-specific support

  **Django REST     APIs inside Django Django            Requires Django; may be
  Framework (DRF)** projects           ORM/admin/auth    heavier for a small
                                       ecosystem and     standalone inference API
                                       mature API        
                                       tooling           
  ---------------------------------------------------------------------------------

### Which one should you choose?

-   Choose **FastAPI** for REST APIs, Python ML/AI services, typed JSON
    contracts, and automatic OpenAPI docs.
-   Choose **Django** for a business application that needs an ORM,
    admin interface, authentication, migrations, and many integrated web
    features.
-   Choose **Flask** for a small, flexible service when you prefer to
    assemble components yourself.
-   Choose **Starlette** when you want a lower-level ASGI toolkit and
    are comfortable adding the layers you need.
-   Choose **Django REST Framework** when your API belongs naturally
    inside an existing Django application.

### FastAPI vs Node.js / NestJS

  -----------------------------------------------------------------------
  Topic                   FastAPI                 NestJS
  ----------------------- ----------------------- -----------------------
  Language                Python                  TypeScript / JavaScript

  Main strengths          Python APIs, data and   Structured server-side
                          AI/ML integration       TypeScript applications

  Validation              Pydantic and type hints Pipes plus
                                                  class-validator or
                                                  other validation tools

  API documentation       OpenAPI integration     Swagger integration

  Dependency injection    Built-in dependency     Core architectural
                          system                  feature

  ML library access       Native Python ecosystem Often calls Python
                                                  services for
                                                  Python-only ML
                                                  workloads

  Typical fit             AI/ML service, Python   Business backend,
                          API, data service       TypeScript
                                                  microservices,
                                                  application APIs
  -----------------------------------------------------------------------

**A practical architecture:** keep the main business backend in NestJS
if that fits the system, and expose Python-specific inference or RAG
capabilities as a separate FastAPI service. Use clear service contracts
and secure service-to-service communication.

------------------------------------------------------------------------

## 5. Pros and cons

### Pros

-   Beginner-friendly route syntax.
-   Automatic request validation and helpful validation errors.
-   Interactive API documentation generated from the code.
-   Type hints make contracts clearer and improve editor support.
-   Async endpoint support for I/O-heavy workloads.
-   Strong fit for Python AI/ML libraries.
-   Supports modular applications, dependency injection, middleware, and
    testing.
-   Works with different databases, deployment platforms, and frontend
    stacks.

### Cons and limitations

-   It does not provide a built-in full-stack admin site or ORM
    comparable to Django's integrated ecosystem.
-   You must select and configure database access, migrations,
    authentication, task queues, and other components.
-   Async does not automatically make CPU-heavy Python work faster.
-   Blocking operations inside `async def` can hurt concurrency if
    handled incorrectly.
-   Production deployment still requires security, observability,
    timeouts, worker sizing, and infrastructure decisions.
-   A large application can become hard to maintain without deliberate
    module boundaries and tests.
-   Automatic docs do not replace good API design, authorization checks,
    or security reviews.

### Performance note

FastAPI is designed for high-performance API workloads, but real
performance depends on database queries, network latency, payload size,
blocking work, model inference, and deployment configuration. Benchmark
your actual workload before selecting an architecture.

------------------------------------------------------------------------

## 6. Prerequisites

You should have:

-   Basic Python syntax: variables, functions, imports, dictionaries,
    and lists.
-   Basic HTTP concepts: request, response, GET, POST, status codes, and
    JSON.
-   Terminal basics.
-   A code editor such as VS Code or Cursor.

Helpful later: SQL, Git, Docker, authentication, testing, and async
programming.

Check whether Python is installed:

``` bash
python3 --version
```

Check Git:

``` bash
git --version
```

If Python is missing or too old for your chosen dependencies, install a
supported Python version first. `uv` can also install and manage Python
versions.

------------------------------------------------------------------------

## 7. Install uv

`uv` is a fast Python package and project manager. It can manage Python
versions, virtual environments, dependencies, lockfiles, commands, and
Python package builds.

### macOS / Linux

Install with the official installer:

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal if necessary, then verify:

``` bash
uv --version
```

Alternative: install through Homebrew on macOS:

``` bash
brew install uv
```

Use one installation method and ensure the intended `uv` executable is
on your `PATH`.

Official installation instructions:
https://docs.astral.sh/uv/getting-started/installation/

### Windows PowerShell

``` powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then:

``` powershell
uv --version
```

------------------------------------------------------------------------

## 8. Create a project with uv

There are two useful workflows. **Recommended for a new project: use
uv's project commands** so dependency versions are recorded in
`pyproject.toml` and `uv.lock`.

### Option A --- Recommended: uv manages the environment

``` bash
mkdir fastapi-starter
cd fastapi-starter

uv init --bare
uv python install 3.12
uv python pin 3.12

uv add "fastapi[standard]"
uv add --dev pytest httpx ruff
```

What these commands do:

-   `uv init --bare` creates a minimal project configuration.
-   `uv python install 3.12` installs Python 3.12 managed by uv if
    needed.
-   `uv python pin 3.12` records the project's Python version preference
    in `.python-version`.
-   `uv add "fastapi[standard]"` adds FastAPI and its standard optional
    dependencies.
-   `uv add --dev ...` adds development tools for tests and code
    quality.

Create `main.py` in the project root, then follow the next sections.

**Do I need to activate `.venv`?** No. `uv run` automatically runs
commands in the project's environment. The environment is usually
created at `.venv` when dependencies are synchronized. If you want
manual activation, use:

``` bash
source .venv/bin/activate
```

Exit the activated environment with:

``` bash
deactivate
```

### Option B --- Explicit venv workflow

Use this if you specifically want to create and activate a virtual
environment yourself:

``` bash
mkdir fastapi-venv
cd fastapi-venv

uv python install 3.12
uv venv --python 3.12 .venv
source .venv/bin/activate

uv pip install "fastapi[standard]" pytest httpx ruff
```

This workflow uses `uv pip` to install packages into the active virtual
environment. For a team project, record and lock dependencies rather
than relying on an untracked environment alone.

### venv vs uv

  -----------------------------------------------------------------------
  Tool                                Role
  ----------------------------------- -----------------------------------
  `venv`                              Python's standard-library virtual
                                      environment module

  `uv venv`                           Creates virtual environments using
                                      uv

  `pip`                               Installs Python packages

  `uv pip`                            A fast pip-compatible interface
                                      provided by uv

  `uv add`                            Adds a dependency to a uv-managed
                                      project

  `uv run`                            Runs commands in the project
                                      environment

  `uv sync`                           Synchronizes the environment with
                                      project dependencies and lockfile
  -----------------------------------------------------------------------

You do not need to use `venv` and `uv` as competing solutions: `uv` can
create and manage `.venv`. Choose one consistent dependency-management
workflow for each project.

------------------------------------------------------------------------

## 9. Understand the important files

A minimal project can look like this:

``` text
fastapi-starter/
├── .venv/             # Local virtual environment; do not commit
├── .python-version    # Preferred Python version
├── .gitignore
├── main.py            # FastAPI application
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Resolved dependency lockfile
└── README.md
```

### `pyproject.toml`

This file records project metadata and declared dependencies. A uv
project may contain something like:

``` toml
[project]
name = "fastapi-starter"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]",
]

[dependency-groups]
dev = [
    "httpx",
    "pytest",
    "ruff",
]
```

Your actual file may differ depending on the `uv` version and commands
used. Prefer `uv add` and `uv add --dev` instead of manually editing
dependency lists unnecessarily.

### `uv.lock`

The lockfile records the resolved dependency versions and related
resolution information. Commit it to Git for reproducible team and CI
environments.

### `.gitignore`

At minimum, ignore local environments, secrets, and generated caches:

``` gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.env
.env.*
!.env.example
dist/
build/
```

Do not commit credentials, API keys, private certificates, or production
`.env` files.

------------------------------------------------------------------------

## 10. Create your first API

Create `main.py`:

``` python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Starter",
    description="A beginner-friendly API",
    version="1.0.0",
)


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items", status_code=201)
def create_item(item: Item):
    return {
        "message": "Item received",
        "item": item,
    }
```

### What the routes demonstrate

  Route                    Purpose
  ------------------------ -----------------------------
  `GET /`                  Basic endpoint
  `GET /health`            Health response example
  `GET /items/10?q=book`   Path and query parameters
  `POST /items`            Validated JSON request body

Try a request:

``` bash
curl "http://127.0.0.1:8000/items/10?q=book"
```

Expected JSON:

``` json
{
  "item_id": 10,
  "q": "book"
}
```

Try creating an item:

``` bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook","price":49.5,"in_stock":true}'
```

A successful request returns HTTP `201 Created` and the item data.
Invalid input produces a validation error response.

------------------------------------------------------------------------

## 11. Start, stop, and run the server

### Development mode

From the project directory:

``` bash
uv run fastapi dev main.py
```

Development mode enables auto-reload and is intended for local
development.

Open:

-   API: http://127.0.0.1:8000/
-   Swagger UI: http://127.0.0.1:8000/docs
-   ReDoc: http://127.0.0.1:8000/redoc
-   OpenAPI schema: http://127.0.0.1:8000/openapi.json

Stop the server with `Ctrl+C`.

### Choose a port or host

For example:

``` bash
uv run fastapi dev main.py --host 127.0.0.1 --port 8001
```

To listen on all interfaces for a controlled development/container
environment:

``` bash
uv run fastapi dev main.py --host 0.0.0.0 --port 8000
```

Binding to `0.0.0.0` can expose the service to other machines depending
on firewall and network configuration. Do not expose a development
server publicly.

### Production-style server command

``` bash
uv run fastapi run main.py --host 0.0.0.0 --port 8000
```

This disables development auto-reload, but the command alone does not
make an application production-ready. Review worker count, process
management, secrets, logging, HTTPS termination, health checks, resource
limits, and deployment platform requirements.

### Uvicorn alternative

You can also start Uvicorn directly:

``` bash
uv run uvicorn main:app --reload
```

Here `main:app` means the `app` object inside `main.py`.

For a module in a package, use the corresponding import path, such as
`uv run uvicorn app.main:app --reload`.

------------------------------------------------------------------------

## 12. Test the API and view documentation

FastAPI generates interactive documentation automatically from the
application and its schemas.

### Swagger UI

Visit:

``` text
http://127.0.0.1:8000/docs
```

Select an endpoint, click **Try it out**, enter parameters or JSON, and
execute the request.

### ReDoc

Visit:

``` text
http://127.0.0.1:8000/redoc
```

### curl

``` bash
curl -i http://127.0.0.1:8000/health
```

The `-i` option displays HTTP response headers as well as the body.

### Useful HTTP status codes

  -----------------------------------------------------------------------
  Code                    Meaning                 Common use
  ----------------------- ----------------------- -----------------------
  `200`                   OK                      Successful read or
                                                  update

  `201`                   Created                 Resource created

  `204`                   No Content              Successful operation
                                                  without a response body

  `400`                   Bad Request             Invalid request
                                                  semantics

  `401`                   Unauthorized            Authentication missing
                                                  or invalid

  `403`                   Forbidden               Authenticated caller
                                                  lacks permission

  `404`                   Not Found               Resource or route not
                                                  found

  `422`                   Unprocessable Content   FastAPI/Pydantic
                                                  request validation
                                                  failure

  `500`                   Internal Server Error   Unexpected server
                                                  failure
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 13. Add dependencies and manage Python versions

### Add a production dependency

``` bash
uv add sqlalchemy
uv add "psycopg[binary]"
```

Example: SQLAlchemy is an ORM/SQL toolkit; `psycopg` is a PostgreSQL
driver. Install only what the project actually uses.

### Add development dependencies

``` bash
uv add --dev pytest httpx ruff
```

### Remove a dependency

``` bash
uv remove sqlalchemy
```

### Synchronize the environment

``` bash
uv sync
```

### Refresh the lockfile

``` bash
uv lock
```

`uv lock` resolves and updates the lockfile as needed. To keep an
existing lockfile's selected versions, use the appropriate locked/sync
workflow rather than casually updating dependencies.

### Install exactly from the lockfile in CI

``` bash
uv sync --locked
```

This fails if the lockfile would need to change, helping detect
out-of-date dependency metadata.

### Inspect installed dependency tree

``` bash
uv tree
```

### Install/select another Python version

``` bash
uv python list
uv python install 3.12
uv python pin 3.12
```

Changing Python versions can require dependency re-resolution or
recreating `.venv`. Test the application after changing versions.

------------------------------------------------------------------------

## 14. Debugging

### A. Read the terminal logs

Run the app in the terminal and reproduce the problem. Check the
traceback, file name, line number, and exception type.

Common categories include:

-   `ModuleNotFoundError`: dependency missing or wrong environment
    selected.
-   `ImportError`: incorrect import or incompatible package.
-   `ValidationError` / HTTP `422`: request body or parameter does not
    match the schema.
-   `Address already in use`: another process already occupies the port.
-   HTTP `500`: unhandled server-side exception; inspect server logs.

### B. Use a breakpoint

``` python
@app.get("/debug")
def debug_example():
    user = {"id": 1, "name": "Alex"}
    breakpoint()
    return user
```

Run the application, then call `/debug`. Python enters its debugger in
the terminal where the server is running. Use `n` to step to the next
line, `p user` to inspect a value, and `c` to continue.

Remove or disable breakpoints before deployment.

### C. Debug with VS Code

1.  Open the project folder.
2.  Select the Python interpreter from `.venv`.
3.  Add a breakpoint by clicking beside a line number.
4.  Create `.vscode/launch.json`:

``` json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI: debug",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["main:app", "--host", "127.0.0.1", "--port", "8000"],
      "jinja": true
    }
  ]
}
```

5.  Install `debugpy` in the project if VS Code requests it:

``` bash
uv add --dev debugpy
```

6.  Choose **FastAPI: debug** in the Run and Debug panel and press F5.

This configuration starts Uvicorn without auto-reload, which keeps
breakpoint behavior easier to understand. For nested modules, update
`main:app` to the actual import path.

### D. Diagnose port conflicts on macOS/Linux

``` bash
lsof -i :8000
```

Stop the process you own using the appropriate method. Avoid killing
unrelated services blindly.

------------------------------------------------------------------------

## 15. Testing

Install the test tools if you have not already:

``` bash
uv add --dev pytest httpx
```

Create `tests/test_main.py`:

``` python
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item():
    response = client.post(
        "/items",
        json={"name": "Notebook", "price": 49.5},
    )
    assert response.status_code == 201
    assert response.json()["item"]["name"] == "Notebook"


def test_invalid_item():
    response = client.post(
        "/items",
        json={"name": "Notebook", "price": "not-a-number"},
    )
    assert response.status_code == 422
```

Run tests:

``` bash
uv run pytest -v
```

`TestClient` lets you test the API without manually starting a network
server. Add tests for authorization, error cases, database behavior, and
important business rules as the project grows.

------------------------------------------------------------------------

## 16. Code quality and formatting

Use Ruff for linting and formatting:

``` bash
uv run ruff check .
uv run ruff format .
```

To check formatting without modifying files:

``` bash
uv run ruff format --check .
```

Run tests and checks before committing:

``` bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

These checks complement---not replace---code review and functional
tests.

------------------------------------------------------------------------

## 17. Environment variables and secrets

Keep configuration out of source code. For local development, a `.env`
file is convenient.

Install settings support:

``` bash
uv add pydantic-settings
```

Create `.env`:

``` dotenv
APP_NAME="FastAPI Starter"
ENVIRONMENT="development"
```

Create `config.py`:

``` python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI"
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
```

Use it in `main.py`:

``` python
from fastapi import FastAPI
from config import settings

app = FastAPI(title=settings.app_name)


@app.get("/config")
def get_config():
    return {"environment": settings.environment}
```

Do not return secrets in API responses or commit `.env` files containing
credentials. In production, use your platform's secret manager or
environment configuration. `.env.example` should contain placeholder
values only.

------------------------------------------------------------------------

## 18. Recommended project structure

For a small learning project, a single `main.py` is fine. For a growing
API, separate routes, schemas, configuration, and business logic.

``` text
fastapi-starter/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── services/
│   │   └── item_service.py
│   └── db/
│       └── session.py
├── tests/
│   └── test_main.py
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

Suggested responsibilities:

-   `main.py`: create the app, register routers, and configure
    lifespan/middleware.
-   `api/routes/`: HTTP endpoints and request/response orchestration.
-   `schemas/`: Pydantic request and response models.
-   `services/`: business logic, independent of HTTP details where
    practical.
-   `db/`: database engine, sessions, and persistence configuration.
-   `core/`: settings, security, and shared configuration.
-   `tests/`: endpoint and business-logic tests.

For larger systems, add repositories, migrations, domain modules,
workers, and integration clients when they solve a real need. Avoid
creating empty layers just to make the project look enterprise-ready.

------------------------------------------------------------------------

## 19. Database integration

FastAPI does not force you to use a particular database or ORM.

  -----------------------------------------------------------------------
  Database                            Common Python options
  ----------------------------------- -----------------------------------
  PostgreSQL                          SQLAlchemy, SQLModel, psycopg,
                                      asyncpg

  MySQL                               SQLAlchemy, PyMySQL, mysqlclient

  SQLite                              Python `sqlite3`, SQLAlchemy

  MongoDB                             PyMongo, Motor (check its current
                                      maintenance/status before choosing)

  Vector search                       PostgreSQL with pgvector, or a
                                      dedicated vector database
  -----------------------------------------------------------------------

A typical request flow is:

1.  FastAPI validates the request.
2.  A dependency provides a database session.
3.  The route or service executes database operations.
4.  The result is converted into a response schema.
5.  The session is cleaned up.

For production, plan database migrations, transactions, connection
pooling, indexes, timeouts, access controls, and backup/restore
procedures. Never assume an in-memory demo is a production persistence
layer.

------------------------------------------------------------------------

## 20. Build, lock, sync, and deploy

These words mean different things.

### `uv sync` --- install project dependencies

``` bash
uv sync
```

Creates or updates the project's environment to match its dependency
configuration and lockfile.

### `uv lock` --- resolve dependency versions

``` bash
uv lock
```

Updates the dependency lockfile as needed.

### `uv build` --- build Python package archives

``` bash
uv build
```

This builds distribution artifacts, typically a source distribution and
a wheel, in `dist/` when the project has a configured build system.

**Important:** `uv build` does not compile a FastAPI server into a
standalone executable or create a production container. It builds Python
package distributions. A deployable application may instead be shipped
as source plus locked dependencies or as a Docker image.

If your project was created with `uv init --bare`, it may not have a
build system configured. Add one only if you intend to package the
project as a distributable Python package.

### Prepare a clean environment

For a locked project:

``` bash
uv sync --locked
uv run pytest
uv run ruff check .
```

### Run without development auto-reload

``` bash
uv run fastapi run main.py --host 0.0.0.0 --port 8000
```

### Production checklist

-   Run behind an appropriate reverse proxy or managed ingress when
    required.
-   Terminate HTTPS correctly.
-   Keep secrets outside source control.
-   Configure structured logs, monitoring, and error reporting.
-   Use health checks, timeouts, and graceful shutdown.
-   Size workers and resources according to measured load.
-   Validate and authorize every sensitive operation.
-   Configure CORS for the intended frontend origins.
-   Use database migrations and backups.
-   Pin and review dependencies; run tests in CI.
-   Do not expose debug mode or development reload publicly.

The exact deployment process depends on the platform (Docker, VM,
Kubernetes, or a managed service).

------------------------------------------------------------------------

## 21. Docker quick start

A simple container is useful for learning. For production, adapt it to
your Python version, dependency workflow, user permissions, health
checks, and deployment platform.

Create a `Dockerfile`:

``` dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY main.py ./

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

``` bash
docker build -t fastapi-starter .
docker run --rm -p 8000:8000 fastapi-starter
```

Visit `http://127.0.0.1:8000/docs`.

This example assumes the project dependencies and lockfile are
consistent and `main.py` is at the project root. For a larger package,
copy the application package and any required files into the image. For
ML apps, also account for model artifacts, model download strategy,
memory, and startup time.

------------------------------------------------------------------------

## 22. Common commands cheat sheet

  Task                           Command
  ------------------------------ -------------------------------------
  Check uv                       `uv --version`
  Initialize project             `uv init --bare`
  Install/select Python          `uv python install 3.12`
  Pin Python version             `uv python pin 3.12`
  Add runtime dependency         `uv add "fastapi[standard]"`
  Add dev dependency             `uv add --dev pytest httpx ruff`
  Remove dependency              `uv remove package-name`
  Sync environment               `uv sync`
  Enforce lockfile consistency   `uv sync --locked`
  Run dev server                 `uv run fastapi dev main.py`
  Run without auto-reload        `uv run fastapi run main.py`
  Run tests                      `uv run pytest -v`
  Lint                           `uv run ruff check .`
  Format                         `uv run ruff format .`
  Check dependency tree          `uv tree`
  Build Python distributions     `uv build`
  Inspect port 8000              `lsof -i :8000`
  Build Docker image             `docker build -t fastapi-starter .`

------------------------------------------------------------------------

## 23. Common beginner errors

### `uv: command not found`

-   Confirm installation completed.
-   Restart the terminal or configure your `PATH`.
-   Check which executable is being used with `which uv`.

### `No module named fastapi`

Run commands from the project directory and use:

``` bash
uv add "fastapi[standard]"
uv run fastapi dev main.py
```

For the explicit venv workflow, activate `.venv` and install into that
environment.

### `Could not import module "main"`

-   Ensure `main.py` exists in the current directory.
-   Ensure the application object is named `app`.
-   Use the correct module path, such as `app.main:app`, if the file is
    inside a package.

### Port 8000 is already in use

``` bash
lsof -i :8000
```

Stop the process you recognize or select another port.

### Request returns `422 Unprocessable Content`

Check the request body, parameter types, required fields, and content
type. Use `/docs` to see the expected schema.

### Environment variables are not loaded

-   Confirm the `.env` file path and spelling.
-   Confirm settings are configured to load it.
-   Do not assume a `.env` file is automatically loaded by every Python
    library.

### Docker build cannot find `uv.lock`

Run `uv lock` in the project and commit the generated lockfile, or
adjust the Dockerfile for the dependency workflow you deliberately
chose.

------------------------------------------------------------------------

## 24. Learning roadmap

Learn the framework in a practical sequence:

1.  **Python essentials:** functions, modules, dictionaries, type hints,
    exceptions, virtual environments.
2.  **HTTP and JSON:** methods, URLs, headers, status codes,
    request/response lifecycle.
3.  **First FastAPI app:** routes, path parameters, query parameters,
    request bodies.
4.  **Pydantic:** validation, nested models, response schemas.
5.  **CRUD:** create, list, retrieve, update, delete resources.
6.  **Project structure:** routers, dependencies, services, settings.
7.  **Errors and middleware:** `HTTPException`, custom exception
    handling, CORS.
8.  **Databases:** PostgreSQL, SQLAlchemy, sessions, migrations,
    transactions.
9.  **Security:** password hashing, OAuth2/JWT concepts, authorization,
    rate limiting.
10. **Testing:** pytest, TestClient, fixtures, dependency overrides.
11. **Async:** `async def`, `await`, blocking I/O, thread pools,
    concurrency.
12. **Production:** logs, configuration, Docker, reverse proxy, HTTPS,
    health checks.
13. **AI/ML APIs:** load a model safely, validate prediction input,
    return structured output.
14. **Advanced projects:** RAG API, background processing, streaming,
    observability, service integration.

### Suggested projects

-   Beginner: Hello API and a calculator API.
-   Beginner/intermediate: In-memory product CRUD API.
-   Intermediate: PostgreSQL task manager with validation and tests.
-   Intermediate: JWT-protected user API.
-   Advanced: ML prediction API serving a saved model.
-   Advanced: RAG document question-answering API using
    PostgreSQL/pgvector and an LLM provider.
-   Production practice: Dockerized API with CI tests, logs, health
    checks, and documented deployment.

------------------------------------------------------------------------

## 25. Official resources

-   [FastAPI documentation](https://fastapi.tiangolo.com/)
-   [FastAPI first
    steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
-   [FastAPI request body and
    Pydantic](https://fastapi.tiangolo.com/tutorial/body/)
-   [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
-   [FastAPI deployment
    concepts](https://fastapi.tiangolo.com/deployment/)
-   [uv documentation](https://docs.astral.sh/uv/)
-   [uv project guide](https://docs.astral.sh/uv/guides/projects/)
-   [uv Python
    versions](https://docs.astral.sh/uv/guides/install-python/)
-   [Django documentation](https://docs.djangoproject.com/)
-   [Flask documentation](https://flask.palletsprojects.com/)
-   [Starlette documentation](https://www.starlette.io/)
-   [Litestar documentation](https://docs.litestar.dev/)

------------------------------------------------------------------------

## Final recommendation

For learning FastAPI from scratch, begin with **`uv` + `.venv` +
`fastapi[standard]` + `pytest`**. Build a small API first, then
introduce Pydantic schemas, routers, database access, authentication,
and deployment in that order.

Use FastAPI when you want a well-documented Python API---especially for
AI/ML or data-heavy services. Use Django when the value of an integrated
full-stack framework outweighs the flexibility of assembling your own
components.
