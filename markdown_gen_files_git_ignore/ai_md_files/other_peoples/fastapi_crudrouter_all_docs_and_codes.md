# markdown content namespace: fastapi_crudrouter all docs and codes 


## Included Files


- `CONTRIBUTING.md`

- `README.md`

- `setup.py`

- `docs/en/docs/contributing.md`

- `docs/en/docs/dependencies.md`

- `docs/en/docs/index.md`

- `docs/en/docs/pagination.md`

- `docs/en/docs/releases.md`

- `docs/en/docs/routing.md`

- `docs/en/docs/schemas.md`

- `docs/en/docs/backends/async.md`

- `docs/en/docs/backends/gino.md`

- `docs/en/docs/backends/memory.md`

- `docs/en/docs/backends/ormar.md`

- `docs/en/docs/backends/sqlalchemy.md`

- `docs/en/docs/backends/tortoise.md`

- `fastapi_crudrouter/_version.py`

- `fastapi_crudrouter/__init__.py`

- `fastapi_crudrouter/core/databases.py`

- `fastapi_crudrouter/core/gino_starlette.py`

- `fastapi_crudrouter/core/mem.py`

- `fastapi_crudrouter/core/ormar.py`

- `fastapi_crudrouter/core/sqlalchemy.py`

- `fastapi_crudrouter/core/tortoise.py`

- `fastapi_crudrouter/core/_base.py`

- `fastapi_crudrouter/core/_types.py`

- `fastapi_crudrouter/core/_utils.py`

- `fastapi_crudrouter/core/__init__.py`

- `tests/conftest.py`

- `tests/test_base.py`

- `tests/test_custom_ids.py`

- `tests/test_exclude.py`

- `tests/test_integrity_errors.py`

- `tests/test_openapi_schema.py`

- `tests/test_overloads.py`

- `tests/test_pagination.py`

- `tests/test_pks.py`

- `tests/test_prefix.py`

- `tests/test_router.py`

- `tests/test_sqlalchemy_nested_.py`

- `tests/test_two_routers.py`

- `tests/test_version.py`

- `tests/utils.py`

- `tests/__init__.py`

- `tests/conf/config.py`

- `tests/conf/__init__.py`

- `tests/implementations/databases_.py`

- `tests/implementations/gino_.py`

- `tests/implementations/memory.py`

- `tests/implementations/ormar_.py`

- `tests/implementations/sqlalchemy_.py`

- `tests/implementations/tortoise_.py`

- `tests/implementations/__init__.py`

- `tests/test_dependencies/test_disable.py`

- `tests/test_dependencies/test_per_route.py`

- `tests/test_dependencies/test_top_level.py`

- `tests/test_integration/test_backend_not_installed.py`

- `tests/test_integration/test_typing.py`

- `tests/test_integration/__init__.py`


---


### code file start: CONTRIBUTING.md 

Pull requests and contributions are welcome. Please read the [contributions guidelines](https://fastapi-crudrouter.awtkns.com/contributing) for more details.


**code file end: CONTRIBUTING.md**
-------------------------------------------


### code file start: README.md 

<p align="center">
  <img src="https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/logo.png" height="200" />
</p>
<p align="center">
  <em>⚡ Create CRUD routes with lighting speed</em> ⚡</br>
  <sub>A dynamic FastAPI router that automatically creates CRUD routes for your models</sub>
</p>
<p align="center">
<img alt="Tests" src="https://img.shields.io/github/actions/workflow/status/awtkns/fastapi-crudrouter/.github/workflows/pytest.yml?color=%2334D058" />
<img alt="Downloads" src="https://img.shields.io/pypi/dm/fastapi-crudrouter?color=%2334D058" />
  <a href="https://pypi.org/project/fastapi-crudrouter" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi-crudrouter?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
  <img alt="License" src="https://img.shields.io/github/license/awtkns/fastapi-crudrouter?color=%2334D058" />
</p>
<p align="center">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi-crudrouter">
</p>

---

**Documentation**: <a href="https://fastapi-crudrouter.awtkns.com" target="_blank">https://fastapi-crudrouter.awtkns.com</a>

**Source Code**: <a href="https://github.com/awtkns/fastapi-crudrouter" target="_blank">https://github.com/awtkns/fastapi-crudrouter</a>

---
Tired of rewriting generic CRUD routes? Need to rapidly prototype a feature for a presentation
or a hackathon? Thankfully, [fastapi-crudrouter](https://github.com/awtkns/fastapi-crudrouter) has your back. As an 
extension to the APIRouter included with [FastAPI](https://fastapi.tiangolo.com/), the FastAPI CRUDRouter will automatically
generate and document your CRUD routes for you, all you have to do is pass your model and maybe your database connection.

FastAPI-CRUDRouter is **lighting fast**, well tested, and **production ready**.


## Installation
```bash
pip install fastapi-crudrouter
```

## Basic Usage
Below is a simple example of what the CRUDRouter can do. In just ten lines of code, you can generate all 
the crud routes you need for any model. A full list of the routes generated can be found [here](https://fastapi-crudrouter.awtkns.com/routing).

```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
app.include_router(CRUDRouter(schema=Potato))
```

## Advanced Usage
fastapi-crudrouter provides a number of features that allow you to get the most out of your automatically generated CRUD
routes. Listed below are some highlights.

- Automatic Pagination ([docs](https://fastapi-crudrouter.awtkns.com/pagination/))
- Ability to Provide Custom Create and Update Schemas ([docs](https://fastapi-crudrouter.awtkns.com/schemas/))
- Dynamic Generation of Create and Update Schemas ([docs](https://fastapi-crudrouter.awtkns.com/schemas/))
- Ability to Add, Customize, or Disable Specific Routes ([docs](https://fastapi-crudrouter.awtkns.com/routing/))
- Native Support for FastAPI Dependency Injection ([docs](https://fastapi-crudrouter.awtkns.com/dependencies/))

## Supported Backends / ORMs
fastapi-crudrouter currently supports a number of backends / ORMs. Listed below are the backends currently supported. This list will
likely grow in future releases.

- In Memory ([docs](https://fastapi-crudrouter.awtkns.com/backends/memory/))
- SQLAlchemy ([docs](https://fastapi-crudrouter.awtkns.com/backends/sqlalchemy/))
- Databases (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/async/))
- Gino (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/gino.html)) 
- Ormar (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/ormar/))
- Tortoise ORM  (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/tortoise/))

## OpenAPI Support
By default, all routes generated by the CRUDRouter will be documented according to OpenAPI spec.

Below are the default routes created by the CRUDRouter shown in the generated OpenAPI documentation.

![OpenAPI Route Overview](https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/RouteOverview.png)

The CRUDRouter is able to dynamically generate detailed documentation based on the models given to it.

![OpenAPI Route Detail](https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/RouteDetail.png)


**code file end: README.md**
-------------------------------------------


### code file start: setup.py 

```python
from setuptools import setup, find_packages
from distutils.util import convert_path


def get_version():
    ver_path = convert_path("fastapi_crudrouter/_version.py")
    with open(ver_path) as ver_file:
        main_ns = {}
        exec(ver_file.read(), main_ns)
        return main_ns["__version__"]


setup(
    name="fastapi-crudrouter",
    version=get_version(),
    author="Adam Watkins",
    author_email="hello@awtkns.com",
    packages=find_packages(exclude=("tests.*", "tests")),
    url="https://github.com/awtkns/fastapi-crudrouter",
    documentation="https://fastapi-crudrouter.awtkns.com/",
    license="MIT",
    description="A dynamic FastAPI router that automatically creates CRUD routes for your models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["fastapi"],
    python_requires=">=3.7",
    keywords=["fastapi", "crud", "restful", "routing", "generator", "crudrouter"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
    ],
)

```

**code file end: setup.py**
-------------------------------------------


### code file start: docs/en/docs/contributing.md 

As an open source package, fastapi-crudrouter accepts contributions from **all members** of the community. If you are interested in the
contributing, reading the development guidelines below may help you in the process. 😊

## Github

#### Issues
Please create an issue to report a bug, request a feature or to simply ask a question.


#### Pull Requests
Unless the pull request is a simple bugfix, please try to create an issue before starting on the implementation of your pull request.
This ensures that the potential feature is in alignment with CRUDRouter's goals moving forward. This also allows for feedback
on the feature and potential help on where to start implementation wise.

## Development

### Installing the Dev Requirements
FastAPI-Crudrouter requires as set of development requirements that can installed with `pip` be found in `tests/dev.requirements.txt`

<div class="termy">

```console
$ pip install -r tests/dev.requirements.txt
---> 100%
```

</div>

### Testing
When adding additional features, please try to add additional tests that prove that your implementation
works and is bug free.

#### Test requirements
Tests require a postgres database for tests to run. The easiest way to accomplish this is with docker. This project offers
a docker-compose file at tests/conf/dev.docker-compose.yml. You can use this file with

```bash
docker compose -f tests/conf/dev.docker-compose.yml up -d
```

After testing you can tear down the running containers with

```bash
docker compose -f tests/conf/dev.docker-compose.yml down
```

#### Running tests
Crudrouter utilizes the [pytest](https://docs.pytest.org/en/latest/) framework for all of its unittests. Tests can be run 
as shown below. 

<div class="termy">

```console
$ pytest
---> 100%
```

</div>

### Linting, Formatting and Typing

With `dev.requirements.txt` installed above you also install tools to lint, format and static type check the project.

To format the project run: 

```bash
black fastapi_crudrouter tests
```

To check styles, imports, annotations, pep8 etc. run:

```bash
flake8 fastapi_crudrouter
```

To check static types annotations run: 

```bash
mypy fastapi_crudrouter tests
```

### Documentation
Crudrouter's documentation was built using [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). To start the development
documentation server, please first install mkdocs-material and then run the server as shown below.

<div class="termy">

```console
$ pip install mkdocs-material
---> 100%
$ cd docs/en
$ mkdocs serve
```

</div>


**code file end: docs/en/docs/contributing.md**
-------------------------------------------


### code file start: docs/en/docs/dependencies.md 

All the CRUDRouters included with `fastapi_crudrouter` support FastAPI dependency injection.

!!! tip
    Since all CRUDRouter's subclass the [FastAPI APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=+router#apirouter),
    you can use any features APIRouter features.

Below is a simple example of how you could use OAuth2 in conjunction with a CRUDRouter to secure your routes.

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_crudrouter import MemoryCRUDRouter

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def token_auth(token: str=Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(401, "Invalid token")

router = MemoryCRUDRouter(schema=MySchema, dependencies=[Depends(token_auth)])
app.include_router(router)
```

## Custom Dependencies Per Route
All CRUDRouters allow you to add a sequence of dependencies on a per-route basis. The dependencies can be set when 
initializing any CRUDRouter using the key word arguments below.

```python
CRUDRouter(
    # ...
    get_all_route=[Depends(get_all_route_dep), ...],
    get_one_route=[Depends(get_one_route_dep), ...],
    create_route=[Depends(create_route_dep), ...],
    update_route=[Depends(update_route_dep), ...],
    delete_one_route=[Depends(user), ...],
    delete_all_route=[Depends(user), ...],
)

```

!!! tip "Multiple Dependencies Per Route"
    As they are passed as a sequence, you are able to set multiple dependencies individually per route. 

!!! attention "Disabling Routes Entirely"
    Setting the key word arguments shown above to `False`, disables the route entirely.


### Example
In the example below, we are adding a fictitious dependency to the "create route" (POST) which requires the user to be 
logged in to create an object. At the same time, we are also independently adding an admin dependency to only the "delete all 
route" which limits the route's usage to only admin users.

```python
MemoryCRUDRouter(
    schema=MySchema,
    create_route=[Depends(user)],
    delete_all_route=[Depends(admin)]
)
```




**code file end: docs/en/docs/dependencies.md**
-------------------------------------------


### code file start: docs/en/docs/index.md 

<p align="center">
  <img src="assets/banner.png" alt="CRUD Router Logo" style="margin-bottom: 20px" />
</p>
<p align="center">
  <em>⚡ Create CRUD routes with lighting speed</em> ⚡</br>
  <sub>A dynamic FastAPI router that automatically creates routes CRUD for your models</sub>
</p>
<p align="center">
<img alt="Tests" src="https://img.shields.io/github/actions/workflow/status/awtkns/fastapi-crudrouter/.github/workflows/pytest.yml?color=%2334D058" />
<img alt="Downloads" src="https://img.shields.io/pypi/dm/fastapi-crudrouter?color=%2334D058" />
<a href="https://pypi.org/project/fastapi-crudrouter" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi-crudrouter?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<img alt="License" src="https://img.shields.io/github/license/awtkns/fastapi-crudrouter?color=%2334D058" />
</p>
<p align="center">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi-crudrouter">
</p>

---

**Documentation**: <a href="https://fastapi-crudrouter.awtkns.com" target="_blank">https://fastapi-crudrouter.awtkns.com</a>

**Source Code**: <a href="https://github.com/awtkns/fastapi-crudrouter" target="_blank">https://github.com/awtkns/fastapi-crudrouter</a>

---
Tired of rewriting the same generic CRUD routes? Need to rapidly prototype a feature for a presentation
or a hackathon? Thankfully, [fastapi-crudrouter](https://github.com/awtkns/fastapi-crudrouter) has your back. As an 
extension to the APIRouter included with [FastAPI](https://fastapi.tiangolo.com/), the FastAPI CRUDRouter will automatically
generate and document your CRUD routes for you, all you have to do is pass your model and maybe your database connection.

FastAPI-CRUDRouter is also **lightning fast**, well tested, and production ready.

## Installation

<div class="termy">

```console
$ pip install fastapi-crudrouter

---> 100%
```

</div>



## Basic Usage
Below is a simple example of what the CRUDRouter can do. In just ten lines of code, you can generate all 
the crud routes you need for any model. A full list of the routes generated can be found [here](./routing).

```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
app.include_router(CRUDRouter(schema=Potato))
```

## Advanced Usage
fastapi-crudrouter provides a number of features that allow you to get the most out of your automatically generated CRUD
routes. Listed below are some highlights.

- Automatic Pagination ([docs](https://fastapi-crudrouter.awtkns.com/pagination/))
- Ability to Provide Custom Create and Update Schemas ([docs](https://fastapi-crudrouter.awtkns.com/schemas/))
- Dynamic Generation of Create and Update Schemas ([docs](https://fastapi-crudrouter.awtkns.com/schemas/))
- Ability to Add, Customize, or Disable Specific Routes ([docs](https://fastapi-crudrouter.awtkns.com/routing/))
- Native Support for FastAPI Dependencies Injection ([docs](https://fastapi-crudrouter.awtkns.com/dependencies/))

## Supported Backends / ORMs
fastapi-crudrouter supports a number of backends / ORMs. Listed below are the backends currently supported. This list will
likely grow in future releases.

- In Memory ([docs](https://fastapi-crudrouter.awtkns.com/backends/memory/))
- SQLAlchemy ([docs](https://fastapi-crudrouter.awtkns.com/backends/sqlalchemy/))
- Databases (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/async/))
- Ormar (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/ormar/))
- Gino (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/gino/)) 
- Tortoise ORM  (async) ([docs](https://fastapi-crudrouter.awtkns.com/backends/tortoise/))

## OpenAPI Support

!!! tip "Automatic OpenAPI Documentation"
    By default, all routes generated by the CRUDRouter will be documented according to OpenAPI spec.

Below are the default routes created by the CRUDRouter shown in the generated OpenAPI documentation.

![OpenAPI Route Overview](https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/RouteOverview.png)

The CRUDRouter is able to dynamically generate detailed documentation based on the models given to it.

![OpenAPI Route Detail](https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/RouteDetail.png)


**code file end: docs/en/docs/index.md**
-------------------------------------------


### code file start: docs/en/docs/pagination.md 

The CRUDRouter is set up to automatically paginate your routes for you. You can use the `skip` and `limit` query parameters to
paginate your results.

**Skip**:
Using the `skip` (int) parameter, you can skip a certain number of items before returning the items you want.

**Limit**:
Using the `limit` (int) parameter, the maximum number of items to be returned can be defined.

!!! tip "Setting a Maximum Pagination Limit"
    When creating a new CRUDRouter you are able to set the maximum amount of items that will be returned per page.
    To do this, use the `paginate` kwarg when creating a new CRUDRouter as shown in the example below.

    ```python
    CRUDRouter(
        schema=MyPydanticModel, 
        paginate=25
    )
    ```

    Above a new CRUDRouter is being created that will paginate items at 25 items per page.


### Example
Shown below is an example usage of pagination; using `skip` and `limit` to paginate results from the backend. More information on how to 
`skip` and `limit` can be used with fastapi can be found [here](https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils).

=== "Python"

    ```python
    import requests

    requests.get('http://localhost:5000/potatoes' params={
        'skip': 50,
        'limit': 25
    })
    ```

=== "Bash"

    ```bash
    curl -X GET -G \
    'http://localhost:5000/potatoes' \
    -d skip=50 \
    -d limit=25
    ```

In the example above, 25 items on the third page are being returned from our fictitious CRUDRouter endpoint. It is the third
page because we specified a `skip` of 50 items while having a `limit` of 25 items per page. If we were to want items on the fourth 
page we would simply have to increase the `skip` to 75.



### Validation
CRUDRouter will return HTTP Validation error, status code 422, if any of these conditions are met:

- The skip parameter is set to less than 0
- The limit parameter is set to less than 1
- The limit parameter is set to more than the maximum allowed number of records if a maximum is specified.

Shown below is a sample validation error. In the example, a negative value for the `skip` parameter was supplied.
```json
{
  "detail": {
    "detail": [
      {
        "loc": ["query", "skip"],
        "msg": "skip query parameter must be greater or equal to zero",
        "type": "type_error.integer"
      }
    ]
  }
}
```







**code file end: docs/en/docs/pagination.md**
-------------------------------------------


### code file start: docs/en/docs/releases.md 

Release Notes
===

## [v0.8.5 - Typing](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.8.5) { .releases } 
2022-01-27
### 🎉 Highlights
With the release of v0.8.5 fastapi-crudrouter now officially supports both **Python 3.10** and **typed python**. This release also includes significant improvements to the documentation, test suite, and developer experience. 

Keep an eye of for the next release which will contain support for **async SQLAlchemy** ([#122](https://github.com/awtkns/fastapi-crudrouter/pull/122)). 

Big thanks to all contributors that made this possible!

### ✨ Features
- Typed python support [#132](https://github.com/awtkns/fastapi-crudrouter/pull/132) [#111](https://github.com/awtkns/fastapi-crudrouter/pull/111)
- Python 3.10 support [#114](https://github.com/awtkns/fastapi-crudrouter/pull/114)
- Test suite now runs against multiple databases [#86](https://github.com/awtkns/fastapi-crudrouter/pull/86)
- Documentation improvements [#79](https://github.com/awtkns/fastapi-crudrouter/pull/79) [#91](https://github.com/awtkns/fastapi-crudrouter/pull/91) [#117](https://github.com/awtkns/fastapi-crudrouter/pull/117) [#123](https://github.com/awtkns/fastapi-crudrouter/pull/123) [#124](https://github.com/awtkns/fastapi-crudrouter/pull/124) [#125](https://github.com/awtkns/fastapi-crudrouter/pull/125) [@andrewthetechie](https://github.com/andrewthetechie)
- More informative exceptions [#94](https://github.com/awtkns/fastapi-crudrouter/pull/94) [#137](https://github.com/awtkns/fastapi-crudrouter/pull/137)
- General test suite improvements [#96](https://github.com/awtkns/fastapi-crudrouter/pull/96) [#97](https://github.com/awtkns/fastapi-crudrouter/pull/97)

### 🐛 Bug Fixes
- OrderBy not working correctly with Microsoft SQL Server [#88](https://github.com/awtkns/fastapi-crudrouter/pull/88)
- 404 response not documented in OpenAPI spec [#104](https://github.com/awtkns/fastapi-crudrouter/pull/104) [@sondrelg](https://github.com/sondrelg)
- DatabasesCRUDRouter not functioning for inserts and deletes with AsyncPG [#98](https://github.com/awtkns/fastapi-crudrouter/pull/98)

**Full Changelog**: [`v0.8.0...v0.8.5`](https://github.com/awtkns/fastapi-crudrouter/compare/v0.8.0...v0.8.5)

---

## [v0.8.0 - Gino Backend](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.8.0) { .releases } 
2021-07-06
### 🎉 Highlights
With the release of v0.6.0  fastapi-crudrouter **now supports [Gino](https://github.com/python-gino/gino)** as an async backend! When generating routes, GinoCRUDRouter will automatically tie into your database using your Gino models. To use it, simply pass your Gino database model, a database reference, and your pydantic.

```python
GinoCRUDRouter(
    schema=MyPydanticModel,
    db_model=MyModel, 
    db=db
)
```

Check out the [docs](https://fastapi-crudrouter.awtkns.com/backends/gino.html) for more details on how to use the GinoCRUDRouter.

### ✨ Features
- Full Gino Support [@Turall](https://github.com/Turall) [#78](https://github.com/awtkns/fastapi-crudrouter/pull/78) 
- Documentation improvements [#69](https://github.com/awtkns/fastapi-crudrouter/pull/69) [#75](https://github.com/awtkns/fastapi-crudrouter/pull/75) 

### 🐛 Bug Fixes
- All Path Prefixes are now correctly lowercase [#64](https://github.com/awtkns/fastapi-crudrouter/pull/64) [#65](https://github.com/awtkns/fastapi-crudrouter/pull/65)  


---

## [v0.7.0 - Advanced Dependencies ](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.7.0) { .releases } 
2021-04-18
### 🎉 Highlights
With the release of v0.7.0 fastapi-crudrouter now provides the ability to set custom dependencies on a per route basis; a much requested feature. Prior to this release, it was only possible to set dependencies for all the routes at once. 

```python
MemoryCRUDRouter(
    schema=MySchema,
    create_route=[Depends(user)],
    delete_all_route=[Depends(admin)]
)
```

Shown above is a brief example on how limiting each route to specific access rights would work using this new feature. Check out the [docs](https://fastapi-crudrouter.awtkns.com/dependencies/) for more details.

### ✨ Features
- Custom Dependencies Per Route [#37](https://github.com/awtkns/fastapi-crudrouter/pull/37) [#59](https://github.com/awtkns/fastapi-crudrouter/pull/59) [#60](https://github.com/awtkns/fastapi-crudrouter/pull/60) [@DorskFR](https://github.com/DorskFR) [@jm-moreau](https://github.com/jm-moreau) 
- Ability to Provide a List of Custom Tags for OpenAPI [#57](https://github.com/awtkns/fastapi-crudrouter/pull/57) [@jm-moreau](https://github.com/jm-moreau) 
- Improved Documentation [#52](https://github.com/awtkns/fastapi-crudrouter/pull/52) 
- Dark Mode for Documentation

---

## [v0.6.0 - Ormar Backend](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.6.0) { .releases } 
2021-03-26
### 🎉 Highlights
With the release of v0.6.0  fastapi-crudrouter **now supports [ormar](https://github.com/collerek/ormar)** as an async backend! When generating routes, the OrmarCRUDRouter will automatically tie into your database using your ormar models. To use it, simply pass your ormar database model as the schema.

```python
OrmarCRUDRouter(
    schema=MyPydanticModel, 
    paginate=25
)
```

Check out the [docs](https://fastapi-crudrouter.awtkns.com/backends/ormar/) for more details on how to use the `OrmarCRUDRouter`.

### ✨ Features
- Full Ormar Support [@collerek](https://github.com/collerek) [#46](https://github.com/awtkns/fastapi-crudrouter/pull/46)
- Better handling of database errors in the update route [@sorXCode](https://github.com/sorXCode) [#48](https://github.com/awtkns/fastapi-crudrouter/pull/48) 
- Improved typing [#46](https://github.com/awtkns/fastapi-crudrouter/pull/46) [#43](https://github.com/awtkns/fastapi-crudrouter/pull/43)
- Black, Flake8 and Mypy linting [#46](https://github.com/awtkns/fastapi-crudrouter/pull/46) 
- Additional Tests for nested models [#40](https://github.com/awtkns/fastapi-crudrouter/pull/40) 

### 🐛 Bug Fixes
- Pagination issues when max limit was set to null [@ethanhaid](https://github.com/ethanhaid) [#42](https://github.com/awtkns/fastapi-crudrouter/pull/42) 

---

## [v0.5.0 - Pagination](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.5.0) { .releases } 
2021-03-07
### 🎉 Highlights
With the release of v0.5.0 all CRUDRouters  **now supports pagination**. All "get all" routes now accept `skip` and `limit` query parameters allowing you to easily paginate your routes.  By default, no limit is set on the number of items returned by your routes.  Should you wish to limit the number of items that a client can request, it can be done as shown below.

```python
CRUDRouter(
    schema=MyPydanticModel, 
    paginate=25
)
```

Check out the [docs](https://fastapi-crudrouter.awtkns.com/pagination/) on pagination for more information!

### ✨ Features
- Pagination Support [#34](https://github.com/awtkns/fastapi-crudrouter/pull/34) 
- Ability to set custom update schemas [@andreipopovici](https://github.com/andreipopovici) [#31](https://github.com/awtkns/fastapi-crudrouter/pull/31) [#27](https://github.com/awtkns/fastapi-crudrouter/pull/27) 
- Better documentation of past releases [#36](https://github.com/awtkns/fastapi-crudrouter/pull/36)

### 🐛 Bug Fixes
- Prefixing not available for versions of fastapi below v0.62.0 [#29](https://github.com/awtkns/fastapi-crudrouter/pull/29) [#30](https://github.com/awtkns/fastapi-crudrouter/pull/30) 
- Fixed an Import Issue SQLAlchemy and Integrity Errors [@andreipopovici](https://github.com/andreipopovici)  [#33](https://github.com/awtkns/fastapi-crudrouter/pull/33)

---

## [v0.4.0 - Tortoise ORM Support](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.4.0) { .releases } 
2021-02-02
### ✨Features
- Full support for tortoise-orm [#24](https://github.com/awtkns/fastapi-crudrouter/pull/24)
- Dynamic pk/id types for get_one, delete_one, and update_one routes [#26](https://github.com/awtkns/fastapi-crudrouter/pull/26)

### 🐛 Bug Fixes  
- Fixed the summary  for the delete one route [#16](https://github.com/awtkns/fastapi-crudrouter/pull/16) 
- Fixed import errors when certain packages are not installed [#21](https://github.com/awtkns/fastapi-crudrouter/pull/21) 
- Improved SQLA type hinting 

---

## [v0.3.0 - Initial Release](https://github.com/awtkns/fastapi-crudrouter/releases/tag/v0.3.0) { .releases } 
2021-01-04
<p align="center">
  <img src="https://raw.githubusercontent.com/awtkns/fastapi-crudrouter/master/docs/en/docs/assets/logo.png" height="200" />
</p>
<h1 align="center">
🎉 Initial Release 🎉
</h1>

Tired of rewriting the same generic CRUD routes? Need to rapidly prototype a feature for a presentation or a hackathon? Thankfully, fastapi-crudrouter has your back. As an extension to the APIRouter included with FastAPI, the FastAPI CRUDRouter will automatically generate and document your CRUD routes for you.

**Documentation**: <a href="https://fastapi-crudrouter.awtkns.com" target="_blank">https://fastapi-crudrouter.awtkns.com</a>

**Source Code**: <a href="https://github.com/awtkns/fastapi-crudrouter" target="_blank">https://github.com/awtkns/fastapi-crudrouter</a>


### Installation
```python
pip install fastapi_crudrouter
``` 

### Usage
Below is a simple example of what the CRUDRouter can do. In just ten lines of code, you can generate all the crud routes you need for any model. A full list of the routes generated can be found here.
```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
app.include_router(CRUDRouter(model=Potato))
```

### Features
- Automatic pydantic model based route generation and documentation ([Docs](https://fastapi-crudrouter.awtkns.com/routing/))
- Ability to customize any of the generated routes ([Docs](https://fastapi-crudrouter.awtkns.com/routing/#overriding-routes))
- Authorization and FastAPI dependency support ([Docs](https://fastapi-crudrouter.awtkns.com/dependencies/))
- Support for both async and non-async relational databases using SQLAlchemy ([Docs](https://fastapi-crudrouter.awtkns.com/backends/sqlalchemy/)) 
- Extensive documentation.
- And much more 😎

**code file end: docs/en/docs/releases.md**
-------------------------------------------


### code file start: docs/en/docs/routing.md 

Automatic route generation is the meat and potatoes of CRUDRouter's features.  Detail below is how you can prefix, customize,
and disable any routes generated by the CRUDRouter.

## Default Routes
By default, the CRUDRouter will generate the six routes below for you. 

| Route        | Method   | Description
| ------------ | -------- | ----
| `/`          | `GET`    | Get all the resources 
| `/`          | `POST`   | Create a new resource 
| `/`          | `DELETE` | Delete all the resources
| `/{item_id}` | `GET`    | Get an existing resource matching the given `item_id`
| `/{item_id}` | `PUT`    | Update an existing resource matching the given `item_id`
| `/{item_id}` | `DELETE` | Delete an existing resource matching the given `item_id`

!!! note "Route URLs"
    Note that the route url is prefixed by the defined prefix.

    **Example:** If the CRUDRouter's prefix is set as *potato* and I want to update a specific potato the route I want to access is
    `/potato/my_potato_id` where *my_potato_id* is the ID of the potato.

## Prefixes
Depending on which CRUDRouter you are using, the CRUDRouter will try to automatically generate a suitable prefix for your
model.  By default, the [MemoryCRUDRouter](backends/memory.md) will use the pydantic model's name as the prefix.  However,
the [SQLAlchemyCRUDRouter](backends/sqlalchemy.md) will use the model's table name as the prefix.

!!! tip "Custom Prefixes"
    You are also able to set custom prefixes with the `prefix` kwarg when creating your CRUDRouter. This can be done like so:
    `router = CRUDRouter(model=mymodel, prefix='carrot')`

## Disabling Routes
Routes can be disabled from generating with a key word argument (kwarg) when creating your CRUDRouter. The valid kwargs 
are shown below.

| Argument         | Default | Description 
| ---------------- | ------  | ---
| get_all_route    | True    | Setting this to false will prevent the get all route from generating
| get_one_route    | True    | Setting this to false will prevent the get one route from generating
| delete_all_route | True    | Setting this to false will prevent the delete all route from generating
| delete_one_route | True    | Setting this to false will prevent the delete one route from generating
| create_route     | True    | Setting this to false will prevent the create route from generating
| update_route     | True    | Setting this to false will prevent the update route from generating

As an example, the *delete all* route can be disabled by doing the following:
```python
router = MemoryCRUDRouter(schema=MyModel, delete_all_route=False)
```

!!! tip "Custom Dependencies"
    Instead to passing a bool to the arguments listed about, you can also pass a sequence of custom dependencies to be 
    applied to each route. See the docs on [dependencies](dependencies.md) for more details.


## Overriding Routes
Should you need to add custom functionality to any of your routes any of the included routers allows you to do so. 
Should you wish to disable a route from being generated, it can be done [here](../routing/#disabling-routes).

Routes in the CRUDRouter can be overridden by using the standard fastapi route decorators. These include:

 -  `@router.get(path: str, *args, **kwargs)`
 -  `@router.post(path: str, *args, **kwargs)`
 -  `@router.put(path: str, *args, **kwargs)`
 -  `@router.delete(path: str, *args, **kwargs)`
 -  `@router.api_route(path: str, methods: List[str] = ['GET'], *args, **kwargs)`

!!! tip
    All of CRUDRouter's are a subclass of fastapi's [APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter)
    meaning that they can be customized to your heart's content.

### Overriding Example
Below is an example where we are overriding the routes `/potato/{item_id}` and `/potato` while using the MemoryCRUDRouter.

```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
router = CRUDRouter(schema=Potato)

@router.get('')
def overloaded_get_all():
    return 'My overloaded route that returns all the items'

@router.get('/{item_id}')
def overloaded_get_one():
    return 'My overloaded route that returns one item'

app.include_router(router)
```


**code file end: docs/en/docs/routing.md**
-------------------------------------------


### code file start: docs/en/docs/schemas.md 

The CRUDRouter is able to generate and document your routes based on the schema, a 
[pydantic model](https://pydantic-docs.helpmanual.io/usage/models/#basic-model-usage), that is passed to it.

In general, the all provided CRUDRouter's have the option to pass both a `schema` and a `create` schema to it.  If no
create schema is provided, the CRUDRouter will automatically generate one. Optionally you can also pass an `update` schema
allowing for custom update behavior.

```python
CRUDRouter(
    schema=MyPydanticModel, 
    create_schema=MyPydanticCreateModel, 
    update_schema=MyPydanticUpdateModel
)
```

!!! tip "Automatic Create and Update Schema Generation"
    Leaving the create and/or update schema argument blank when creating your CRUDRouter will result in the crud router automatically
    generating and documenting a create and/or update schema in your routes. In doing so, it automatically removes any field which
    matches the primary key in the database as this will be generated server side.

## Create Schemas
Create schemas are models which typically don't include fields that are generated by a database or other backends. An example of this 
is an `id` field in a model.

```python
from pydantic import BaseModel

class Potato(BaseModel):
    id: int
    color: str
    mass: float

class CreatePotato(BaseModel):
    color: str
    mass: float
```

## Update Schemas
Update schemas allow you to limit which fields can be updated. As an example, the update schema below will only allow you to
update the `color` field when used in the CRUDRouter.

```python
from pydantic import BaseModel

class Potato(BaseModel):
    id: int
    color: str
    mass: float

# Allowing the user to only update the color
class UpdatePotato(BaseModel):
    color: str
```


**code file end: docs/en/docs/schemas.md**
-------------------------------------------


### code file start: docs/en/docs/backends/async.md 

Asynchronous routes will be automatically generated when using the `DatabasesCRUDRouter`. To use it, you must pass a 
[pydantic](https://pydantic-docs.helpmanual.io/) model, your SQLAlchemy Table, and the databases database. 
This CRUDRouter is intended to be used with the python [Databases](https://www.encode.io/databases/) library. An example
of how to use [Databases](https://www.encode.io/databases/) with FastAPI can be found both 
[here](https://fastapi.tiangolo.com/advanced/async-sql-databases/) and below.

!!! warning
    To use the `DatabasesCRUDRouter`, Databases **and** SQLAlchemy must be first installed.

## Minimal Example
Below is a minimal example assuming that you have already imported and created 
all the required models and database connections.

```python
from fastapi_crudrouter import DatabasesCRUDRouter
from fastapi import FastAPI

app = FastAPI()

router = DatabasesCRUDRouter(
    schema=MyPydanticModel, 
    table=my_table,
    database=my_database
)
app.include_router(router)
```

## Full Example

```python
import databases
import sqlalchemy

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import DatabasesCRUDRouter

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

metadata = sqlalchemy.MetaData()
potatoes = sqlalchemy.Table(
    "potatoes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("thickness", sqlalchemy.Float),
    sqlalchemy.Column("mass", sqlalchemy.Float),
    sqlalchemy.Column("color", sqlalchemy.String),
    sqlalchemy.Column("type", sqlalchemy.String),
)
metadata.create_all(bind=engine)


class PotatoCreate(BaseModel):
    thickness: float
    mass: float
    color: str
    type: str


class Potato(PotatoCreate):
    id: int


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


router = DatabasesCRUDRouter(
    schema=Potato,
    create_schema=PotatoCreate,
    table=potatoes,
    database=database
)
app.include_router(router)
```

**code file end: docs/en/docs/backends/async.md**
-------------------------------------------


### code file start: docs/en/docs/backends/gino.md 

Asynchronous routes will be automatically generated when using the `GinoCRUDRouter`. To use it, you must pass a 
[pydantic](https://pydantic-docs.helpmanual.io/) model, your SQLAlchemy Table, and the databases database. 
This CRUDRouter is intended to be used with the python [Gino](https://python-gino.org/) library. An example
of how to use [Gino](https://python-gino.org/) with FastAPI can be found both 
[here](https://python-gino.org/docs/en/1.0/tutorials/fastapi.html) and below.

!!! warning
    To use the `GinoCRUDRouter`, Gino **and** SQLAlchemy must be first installed.

## Minimal Example
Below is a minimal example assuming that you have already imported and created 
all the required models and database connections.

```python
router = GinoCRUDRouter(
    schema=MyPydanticModel, 
    db=db,
    db_model=MyModel
)
app.include_router(router)
```


**code file end: docs/en/docs/backends/gino.md**
-------------------------------------------


### code file start: docs/en/docs/backends/memory.md 

The `MemoryCRUDRouter` is the simplest usage of the CRUDRouters.  To use it, simply pass a 
[pydantic](https://pydantic-docs.helpmanual.io/) model to it.  As a database is not required, the `MemoryCRUDRouter` is
well suited for rapid bootstrapping and prototyping.

## Usage
```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
router = MemoryCRUDRouter(schema=Potato)
app.include_router(router)
```

!!! warning
    When using the `MemoryCRUDRouter`, the schema (model) passed to it must have the `id: int` property.

!!! danger
    The storage for the `MemoryCRUDRouter` resides in memory, not a database. Hence, the data is not persistent. Be careful when using it beyond
    the rapid bootstrapping or prototyping phase.

**code file end: docs/en/docs/backends/memory.md**
-------------------------------------------


### code file start: docs/en/docs/backends/ormar.md 

When generating routes, the `OrmarCRUDRouter` will automatically tie into your database
using your [ormar](https://collerek.github.io/ormar/) models. To use it, simply pass your ormar database model as the schema.

## Simple Example

Below is an example assuming that you have already imported and created all the required
models.

```python
from fastapi_crudrouter import OrmarCRUDRouter
from fastapi import FastAPI

app = FastAPI()

router = OrmarCRUDRouter(
    schema=MyOrmarModel,
    create_schema=Optional[MyPydanticCreateModel],
    update_schema=Optional[MyPydanticUpdateModel]
)

app.include_router(router)
```

!!! note
    The `create_schema` should not include the *primary id* field as this be
    generated by the database.

## Full Example

```python
# example.py
import databases
import ormar
import sqlalchemy
import uvicorn
from fastapi import FastAPI

from fastapi_crudrouter import OrmarCRUDRouter

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


def _setup_database():
    # if you do not have the database run this once
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    return engine, database


class Potato(ormar.Model):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    thickness = ormar.Float()
    mass = ormar.Float()
    color = ormar.String(max_length=255)
    type = ormar.String(max_length=255)


app.include_router(
    OrmarCRUDRouter(
        schema=Potato,
        prefix="potato",
    )
)

if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")
```


**code file end: docs/en/docs/backends/ormar.md**
-------------------------------------------


### code file start: docs/en/docs/backends/sqlalchemy.md 

When generating routes, the `SQLAlchemyCRUDRouter` will automatically tie into 
your database using your [SQLAlchemy](https://www.sqlalchemy.org/) models. To use it, you must pass a 
[pydantic](https://pydantic-docs.helpmanual.io/) model, your SQLAlchemy model to it, and the 
database dependency.

!!! warning
    To use the `SQLAlchemyCRUDRouter`, SQLAlchemy must be first installed.

## Simple Example
Below is an example assuming that you have already imported and created all the required models.

```python
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import FastAPI

app = FastAPI()

router = SQLAlchemyCRUDRouter(
    schema=MyPydanticModel,
    create_schema=MyPydanticCreateModel, 
    db_model=MyDBModel,
    db=get_db
)

app.include_router(router)
```

!!! note
    The `create_schema` should not include the *primary id* field as this be generated by the database.

## Full Example

```python
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

app = FastAPI()
engine = create_engine(
    "sqlite:///./app.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


class PotatoCreate(BaseModel):
    thickness: float
    mass: float
    color: str
    type: str


class Potato(PotatoCreate):
    id: int

    class Config:
        orm_mode = True


class PotatoModel(Base):
    __tablename__ = 'potatoes'
    id = Column(Integer, primary_key=True, index=True)
    thickness = Column(Float)
    mass = Column(Float)
    color = Column(String)
    type = Column(String)


Base.metadata.create_all(bind=engine)

router = SQLAlchemyCRUDRouter(
    schema=Potato,
    create_schema=PotatoCreate,
    db_model=PotatoModel,
    db=get_db,
    prefix='potato'
)

app.include_router(router)
```

**code file end: docs/en/docs/backends/sqlalchemy.md**
-------------------------------------------


### code file start: docs/en/docs/backends/tortoise.md 

When generating routes, the `TortoiseCRUDRouter` will automatically tie into 
your database using your [Tortoise](https://tortoise-orm.readthedocs.io/en/latest/index.html) models. To use it, you must pass a 
[pydantic](https://pydantic-docs.helpmanual.io/) schema, your Tortoise database model to it, and register Tortoise ORM with your FastAPI App.

!!! warning
    To use the `TortoiseCRUDRouter`, [Tortoise ORM](https://pypi.org/project/tortoise-orm/) must be first installed.

!!! warning
    Tortoise ORM works on python versions 3.7 and higher, so if you want to use this backend, you would not be able to use `python 3.6`.

## Simple Example
Below is an example assuming that you have already imported and created all the required models.

```python
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from fastapi import FastAPI

app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)

router = TortoiseCRUDRouter(
    schema=MyPydanticModel, 
    db_model=MyDBModel, 
    prefix="test"
)

app.include_router(router)
```

You can provide your TORTOISE_ORM from a file or as a dictionary. If you want to provide it as a dictionary, this would be how:

```python
TORTOISE_ORM = {
    "connections": {"default": 'postgres_url_here'},
    "apps": {
        "models": {
            "models": ["example"],
            "default_connection": "default",
        },
    },
}
```

Where `"models": ["example"]` represents that `example.py` is where your Tortoise database ORM models are located. 
If you ended up having a lot of these, you might want to break it out into a `models.py` file and thus your config would change to `"models": ["models"]`. 
If you use [Aerich](https://github.com/tortoise/aerich) for database migrations, you'll need to add `"aerich.models"` to your config.

!!! note
    The `create_schema` should not include the *primary id* field as this should be generated by the database. If you don't provide a create_schema, a primary key stripped schema will be made for you. 

## Full Example

```python
# example.py

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields, Tortoise

TORTOISE_ORM = {
    "connections": {"default": 'postgres_url'},
    "apps": {
        "models": {
            "models": ["example"],
            "default_connection": "default",
        },
    },
}

# Create Database Tables
async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

app = FastAPI()
register_tortoise(app, config=TORTOISE_ORM)


# Tortoise ORM Model
class TestModel(Model):
    test = fields.IntField(null=False, description=f"Test value")
    ts = fields.IntField(null=False, description=f"Epoch time")


# Pydantic schema
TestSchema = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}Schema")
TestSchemaCreate = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}SchemaCreate", exclude_readonly=True)

# Make your FastAPI Router from your Pydantic schema and Tortoise Model
router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    db_model=TestModel,
    prefix="test"
)

# Add it to your app
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")
```

**code file end: docs/en/docs/backends/tortoise.md**
-------------------------------------------


### code file start: fastapi_crudrouter/_version.py 

```python
__version__ = "0.8.6"

```

**code file end: fastapi_crudrouter/_version.py**
-------------------------------------------


### code file start: fastapi_crudrouter/__init__.py 

```python
from .core import (
    DatabasesCRUDRouter,
    GinoCRUDRouter,
    MemoryCRUDRouter,
    OrmarCRUDRouter,
    SQLAlchemyCRUDRouter,
    TortoiseCRUDRouter,
)

from ._version import __version__  # noqa: F401

__all__ = [
    "MemoryCRUDRouter",
    "SQLAlchemyCRUDRouter",
    "DatabasesCRUDRouter",
    "TortoiseCRUDRouter",
    "OrmarCRUDRouter",
    "GinoCRUDRouter",
]

```

**code file end: fastapi_crudrouter/__init__.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/databases.py 

```python
from typing import (
    Any,
    Callable,
    List,
    Mapping,
    Type,
    Coroutine,
    Optional,
    Union,
)

from fastapi import HTTPException

from . import CRUDGenerator, NOT_FOUND
from ._types import PAGINATION, PYDANTIC_SCHEMA, DEPENDENCIES
from ._utils import AttrDict, get_pk_type

try:
    from sqlalchemy.sql.schema import Table
    from databases.core import Database
except ImportError:
    Database = None  # type: ignore
    Table = None
    databases_installed = False
else:
    databases_installed = True

Model = Mapping[Any, Any]
CALLABLE = Callable[..., Coroutine[Any, Any, Model]]
CALLABLE_LIST = Callable[..., Coroutine[Any, Any, List[Model]]]


def pydantify_record(
    models: Union[Model, List[Model]]
) -> Union[AttrDict, List[AttrDict]]:
    if type(models) is list:
        return [AttrDict(**dict(model)) for model in models]
    else:
        return AttrDict(**dict(models))  # type: ignore


class DatabasesCRUDRouter(CRUDGenerator[PYDANTIC_SCHEMA]):
    def __init__(
        self,
        schema: Type[PYDANTIC_SCHEMA],
        table: "Table",
        database: "Database",
        create_schema: Optional[Type[PYDANTIC_SCHEMA]] = None,
        update_schema: Optional[Type[PYDANTIC_SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert (
            databases_installed
        ), "Databases and SQLAlchemy must be installed to use the DatabasesCRUDRouter."

        self.table = table
        self.db = database
        self._pk = table.primary_key.columns.values()[0].name
        self._pk_col = self.table.c[self._pk]
        self._pk_type: type = get_pk_type(schema, self._pk)

        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix or table.name,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route(
            pagination: PAGINATION = self.pagination,
        ) -> List[Model]:
            skip, limit = pagination.get("skip"), pagination.get("limit")

            query = self.table.select().limit(limit).offset(skip)
            return pydantify_record(await self.db.fetch_all(query))  # type: ignore

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            query = self.table.select().where(self._pk_col == item_id)
            model = await self.db.fetch_one(query)

            if model:
                return pydantify_record(model)  # type: ignore
            else:
                raise NOT_FOUND

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            schema: self.create_schema,  # type: ignore
        ) -> Model:
            query = self.table.insert()

            try:
                rid = await self.db.execute(query=query, values=schema.dict())
                if type(rid) is not self._pk_type:
                    rid = getattr(schema, self._pk, rid)

                return await self._get_one()(rid)
            except Exception:
                raise HTTPException(422, "Key already exists") from None

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            item_id: self._pk_type, schema: self.update_schema  # type: ignore
        ) -> Model:
            query = self.table.update().where(self._pk_col == item_id)

            try:
                await self.db.fetch_one(
                    query=query, values=schema.dict(exclude={self._pk})
                )
                return await self._get_one()(item_id)
            except Exception as e:
                raise NOT_FOUND from e

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route() -> List[Model]:
            query = self.table.delete()
            await self.db.execute(query=query)

            return await self._get_all()(pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            query = self.table.delete().where(self._pk_col == item_id)

            try:
                row = await self._get_one()(item_id)
                await self.db.execute(query=query)
                return row
            except Exception as e:
                raise NOT_FOUND from e

        return route

```

**code file end: fastapi_crudrouter/core/databases.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/gino_starlette.py 

```python
from typing import Any, Callable, List, Optional, Type, Union, Coroutine

from fastapi import HTTPException

from . import NOT_FOUND, CRUDGenerator, _utils
from ._types import DEPENDENCIES, PAGINATION
from ._types import PYDANTIC_SCHEMA as SCHEMA

try:
    from asyncpg.exceptions import UniqueViolationError
    from gino import Gino
    from sqlalchemy.exc import IntegrityError
    from sqlalchemy.ext.declarative import DeclarativeMeta as Model
except ImportError:
    Model = None
    IntegrityError = None
    UniqueViolationError = None
    Gino = None
    gino_installed = False
else:
    gino_installed = True

CALLABLE = Callable[..., Coroutine[Any, Any, Model]]
CALLABLE_LIST = Callable[..., Coroutine[Any, Any, List[Model]]]


class GinoCRUDRouter(CRUDGenerator[SCHEMA]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        db_model: Model,
        db: "Gino",
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert gino_installed, "Gino must be installed to use the GinoCRUDRouter."

        self.db_model = db_model
        self.db = db
        self._pk: str = db_model.__table__.primary_key.columns.keys()[0]
        self._pk_type: type = _utils.get_pk_type(schema, self._pk)

        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix or db_model.__tablename__,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route(
            pagination: PAGINATION = self.pagination,
        ) -> List[Model]:
            skip, limit = pagination.get("skip"), pagination.get("limit")

            db_models: List[Model] = (
                await self.db_model.query.limit(limit).offset(skip).gino.all()
            )
            return db_models

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            model: Model = await self.db_model.get(item_id)

            if model:
                return model
            else:
                raise NOT_FOUND

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            model: self.create_schema,  # type: ignore
        ) -> Model:
            try:
                async with self.db.transaction():
                    db_model: Model = await self.db_model.create(**model.dict())
                    return db_model
            except (IntegrityError, UniqueViolationError):
                raise HTTPException(422, "Key already exists") from None

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            item_id: self._pk_type,  # type: ignore
            model: self.update_schema,  # type: ignore
        ) -> Model:
            try:
                db_model: Model = await self._get_one()(item_id)
                async with self.db.transaction():
                    model = model.dict(exclude={self._pk})
                    await db_model.update(**model).apply()

                return db_model
            except (IntegrityError, UniqueViolationError) as e:
                self._raise(e)

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route() -> List[Model]:
            await self.db_model.delete.gino.status()
            return await self._get_all()(pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            db_model: Model = await self._get_one()(item_id)
            await db_model.delete()

            return db_model

        return route

```

**code file end: fastapi_crudrouter/core/gino_starlette.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/mem.py 

```python
from typing import Any, Callable, List, Type, cast, Optional, Union

from . import CRUDGenerator, NOT_FOUND
from ._types import DEPENDENCIES, PAGINATION, PYDANTIC_SCHEMA as SCHEMA

CALLABLE = Callable[..., SCHEMA]
CALLABLE_LIST = Callable[..., List[SCHEMA]]


class MemoryCRUDRouter(CRUDGenerator[SCHEMA]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

        self.models: List[SCHEMA] = []
        self._id = 1

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route(pagination: PAGINATION = self.pagination) -> List[SCHEMA]:
            skip, limit = pagination.get("skip"), pagination.get("limit")
            skip = cast(int, skip)

            return (
                self.models[skip:]
                if limit is None
                else self.models[skip : skip + limit]
            )

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(item_id: int) -> SCHEMA:
            for model in self.models:
                if model.id == item_id:  # type: ignore
                    return model

            raise NOT_FOUND

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(model: self.create_schema) -> SCHEMA:  # type: ignore
            model_dict = model.dict()
            model_dict["id"] = self._get_next_id()
            ready_model = self.schema(**model_dict)
            self.models.append(ready_model)
            return ready_model

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(item_id: int, model: self.update_schema) -> SCHEMA:  # type: ignore
            for ind, model_ in enumerate(self.models):
                if model_.id == item_id:  # type: ignore
                    self.models[ind] = self.schema(
                        **model.dict(), id=model_.id  # type: ignore
                    )
                    return self.models[ind]

            raise NOT_FOUND

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route() -> List[SCHEMA]:
            self.models = []
            return self.models

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(item_id: int) -> SCHEMA:
            for ind, model in enumerate(self.models):
                if model.id == item_id:  # type: ignore
                    del self.models[ind]
                    return model

            raise NOT_FOUND

        return route

    def _get_next_id(self) -> int:
        id_ = self._id
        self._id += 1

        return id_

```

**code file end: fastapi_crudrouter/core/mem.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/ormar.py 

```python
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Type,
    cast,
    Coroutine,
    Union,
)

from fastapi import HTTPException

from . import CRUDGenerator, NOT_FOUND, _utils
from ._types import DEPENDENCIES, PAGINATION

try:
    from ormar import Model, NoMatch
except ImportError:
    Model = None  # type: ignore
    NoMatch = None  # type: ignore
    ormar_installed = False
else:
    ormar_installed = True

CALLABLE = Callable[..., Coroutine[Any, Any, Model]]
CALLABLE_LIST = Callable[..., Coroutine[Any, Any, List[Optional[Model]]]]


class OrmarCRUDRouter(CRUDGenerator[Model]):
    def __init__(
        self,
        schema: Type[Model],
        create_schema: Optional[Type[Model]] = None,
        update_schema: Optional[Type[Model]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert ormar_installed, "Ormar must be installed to use the OrmarCRUDRouter."

        self._pk: str = schema.Meta.pkname
        self._pk_type: type = _utils.get_pk_type(schema, self._pk)

        super().__init__(
            schema=schema,
            create_schema=create_schema or schema,
            update_schema=update_schema or schema,
            prefix=prefix or schema.Meta.tablename,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

        self._INTEGRITY_ERROR = self._get_integrity_error_type()

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route(
            pagination: PAGINATION = self.pagination,
        ) -> List[Optional[Model]]:
            skip, limit = pagination.get("skip"), pagination.get("limit")
            query = self.schema.objects.offset(cast(int, skip))
            if limit:
                query = query.limit(limit)
            return await query.all()  # type: ignore

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            try:
                filter_ = {self._pk: item_id}
                model = await self.schema.objects.filter(
                    _exclude=False, **filter_
                ).first()
            except NoMatch:
                raise NOT_FOUND from None
            return model

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(model: self.create_schema) -> Model:  # type: ignore
            model_dict = model.dict()
            if self.schema.Meta.model_fields[self._pk].autoincrement:
                model_dict.pop(self._pk, None)
            try:
                return await self.schema.objects.create(**model_dict)
            except self._INTEGRITY_ERROR:
                raise HTTPException(422, "Key already exists") from None

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            item_id: self._pk_type,  # type: ignore
            model: self.update_schema,  # type: ignore
        ) -> Model:
            filter_ = {self._pk: item_id}
            try:
                await self.schema.objects.filter(_exclude=False, **filter_).update(
                    **model.dict(exclude_unset=True)
                )
            except self._INTEGRITY_ERROR as e:
                self._raise(e)
            return await self._get_one()(item_id)

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route() -> List[Optional[Model]]:
            await self.schema.objects.delete(each=True)
            return await self._get_all()(pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: self._pk_type) -> Model:  # type: ignore
            model = await self._get_one()(item_id)
            await model.delete()
            return model

        return route

    def _get_integrity_error_type(self) -> Type[Exception]:
        """Imports the Integrity exception based on the used backend"""
        backend = self.schema.db_backend_name()

        try:
            if backend == "sqlite":
                from sqlite3 import IntegrityError
            elif backend == "postgresql":
                from asyncpg import (  # type: ignore
                    IntegrityConstraintViolationError as IntegrityError,
                )
            else:
                from pymysql import IntegrityError  # type: ignore
            return IntegrityError
        except ImportError:
            return Exception

```

**code file end: fastapi_crudrouter/core/ormar.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/sqlalchemy.py 

```python
from typing import Any, Callable, List, Type, Generator, Optional, Union

from fastapi import Depends, HTTPException

from . import CRUDGenerator, NOT_FOUND, _utils
from ._types import DEPENDENCIES, PAGINATION, PYDANTIC_SCHEMA as SCHEMA

try:
    from sqlalchemy.orm import Session
    from sqlalchemy.ext.declarative import DeclarativeMeta as Model
    from sqlalchemy.exc import IntegrityError
except ImportError:
    Model = None
    Session = None
    IntegrityError = None
    sqlalchemy_installed = False
else:
    sqlalchemy_installed = True
    Session = Callable[..., Generator[Session, Any, None]]

CALLABLE = Callable[..., Model]
CALLABLE_LIST = Callable[..., List[Model]]


class SQLAlchemyCRUDRouter(CRUDGenerator[SCHEMA]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        db_model: Model,
        db: "Session",
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert (
            sqlalchemy_installed
        ), "SQLAlchemy must be installed to use the SQLAlchemyCRUDRouter."

        self.db_model = db_model
        self.db_func = db
        self._pk: str = db_model.__table__.primary_key.columns.keys()[0]
        self._pk_type: type = _utils.get_pk_type(schema, self._pk)

        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix or db_model.__tablename__,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route(
            db: Session = Depends(self.db_func),
            pagination: PAGINATION = self.pagination,
        ) -> List[Model]:
            skip, limit = pagination.get("skip"), pagination.get("limit")

            db_models: List[Model] = (
                db.query(self.db_model)
                .order_by(getattr(self.db_model, self._pk))
                .limit(limit)
                .offset(skip)
                .all()
            )
            return db_models

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type, db: Session = Depends(self.db_func)  # type: ignore
        ) -> Model:
            model: Model = db.query(self.db_model).get(item_id)

            if model:
                return model
            else:
                raise NOT_FOUND from None

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            model: self.create_schema,  # type: ignore
            db: Session = Depends(self.db_func),
        ) -> Model:
            try:
                db_model: Model = self.db_model(**model.dict())
                db.add(db_model)
                db.commit()
                db.refresh(db_model)
                return db_model
            except IntegrityError:
                db.rollback()
                raise HTTPException(422, "Key already exists") from None

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type,  # type: ignore
            model: self.update_schema,  # type: ignore
            db: Session = Depends(self.db_func),
        ) -> Model:
            try:
                db_model: Model = self._get_one()(item_id, db)

                for key, value in model.dict(exclude={self._pk}).items():
                    if hasattr(db_model, key):
                        setattr(db_model, key, value)

                db.commit()
                db.refresh(db_model)

                return db_model
            except IntegrityError as e:
                db.rollback()
                self._raise(e)

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route(db: Session = Depends(self.db_func)) -> List[Model]:
            db.query(self.db_model).delete()
            db.commit()

            return self._get_all()(db=db, pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type, db: Session = Depends(self.db_func)  # type: ignore
        ) -> Model:
            db_model: Model = self._get_one()(item_id, db)
            db.delete(db_model)
            db.commit()

            return db_model

        return route

```

**code file end: fastapi_crudrouter/core/sqlalchemy.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/tortoise.py 

```python
from typing import Any, Callable, List, Type, cast, Coroutine, Optional, Union

from . import CRUDGenerator, NOT_FOUND
from ._types import DEPENDENCIES, PAGINATION, PYDANTIC_SCHEMA as SCHEMA

try:
    from tortoise.models import Model
except ImportError:
    Model = None  # type: ignore
    tortoise_installed = False
else:
    tortoise_installed = True


CALLABLE = Callable[..., Coroutine[Any, Any, Model]]
CALLABLE_LIST = Callable[..., Coroutine[Any, Any, List[Model]]]


class TortoiseCRUDRouter(CRUDGenerator[SCHEMA]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        db_model: Type[Model],
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert (
            tortoise_installed
        ), "Tortoise ORM must be installed to use the TortoiseCRUDRouter."

        self.db_model = db_model
        self._pk: str = db_model.describe()["pk_field"]["db_column"]

        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix or db_model.describe()["name"].replace("None.", ""),
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route(pagination: PAGINATION = self.pagination) -> List[Model]:
            skip, limit = pagination.get("skip"), pagination.get("limit")
            query = self.db_model.all().offset(cast(int, skip))
            if limit:
                query = query.limit(limit)
            return await query

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: int) -> Model:
            model = await self.db_model.filter(id=item_id).first()

            if model:
                return model
            else:
                raise NOT_FOUND

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(model: self.create_schema) -> Model:  # type: ignore
            db_model = self.db_model(**model.dict())
            await db_model.save()

            return db_model

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            item_id: int, model: self.update_schema  # type: ignore
        ) -> Model:
            await self.db_model.filter(id=item_id).update(
                **model.dict(exclude_unset=True)
            )
            return await self._get_one()(item_id)

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        async def route() -> List[Model]:
            await self.db_model.all().delete()
            return await self._get_all()(pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: int) -> Model:
            model: Model = await self._get_one()(item_id)
            await self.db_model.filter(id=item_id).delete()

            return model

        return route

```

**code file end: fastapi_crudrouter/core/tortoise.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/_base.py 

```python
from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, List, Optional, Type, Union

from fastapi import APIRouter, HTTPException
from fastapi.types import DecoratedCallable

from ._types import T, DEPENDENCIES
from ._utils import pagination_factory, schema_factory

NOT_FOUND = HTTPException(404, "Item not found")


class CRUDGenerator(Generic[T], APIRouter, ABC):
    schema: Type[T]
    create_schema: Type[T]
    update_schema: Type[T]
    _base_path: str = "/"

    def __init__(
        self,
        schema: Type[T],
        create_schema: Optional[Type[T]] = None,
        update_schema: Optional[Type[T]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any,
    ) -> None:

        self.schema = schema
        self.pagination = pagination_factory(max_limit=paginate)
        self._pk: str = self._pk if hasattr(self, "_pk") else "id"
        self.create_schema = (
            create_schema
            if create_schema
            else schema_factory(self.schema, pk_field_name=self._pk, name="Create")
        )
        self.update_schema = (
            update_schema
            if update_schema
            else schema_factory(self.schema, pk_field_name=self._pk, name="Update")
        )

        prefix = str(prefix if prefix else self.schema.__name__).lower()
        prefix = self._base_path + prefix.strip("/")
        tags = tags or [prefix.strip("/").capitalize()]

        super().__init__(prefix=prefix, tags=tags, **kwargs)

        if get_all_route:
            self._add_api_route(
                "",
                self._get_all(),
                methods=["GET"],
                response_model=Optional[List[self.schema]],  # type: ignore
                summary="Get All",
                dependencies=get_all_route,
            )

        if create_route:
            self._add_api_route(
                "",
                self._create(),
                methods=["POST"],
                response_model=self.schema,
                summary="Create One",
                dependencies=create_route,
            )

        if delete_all_route:
            self._add_api_route(
                "",
                self._delete_all(),
                methods=["DELETE"],
                response_model=Optional[List[self.schema]],  # type: ignore
                summary="Delete All",
                dependencies=delete_all_route,
            )

        if get_one_route:
            self._add_api_route(
                "/{item_id}",
                self._get_one(),
                methods=["GET"],
                response_model=self.schema,
                summary="Get One",
                dependencies=get_one_route,
                error_responses=[NOT_FOUND],
            )

        if update_route:
            self._add_api_route(
                "/{item_id}",
                self._update(),
                methods=["PUT"],
                response_model=self.schema,
                summary="Update One",
                dependencies=update_route,
                error_responses=[NOT_FOUND],
            )

        if delete_one_route:
            self._add_api_route(
                "/{item_id}",
                self._delete_one(),
                methods=["DELETE"],
                response_model=self.schema,
                summary="Delete One",
                dependencies=delete_one_route,
                error_responses=[NOT_FOUND],
            )

    def _add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        dependencies: Union[bool, DEPENDENCIES],
        error_responses: Optional[List[HTTPException]] = None,
        **kwargs: Any,
    ) -> None:
        dependencies = [] if isinstance(dependencies, bool) else dependencies
        responses: Any = (
            {err.status_code: {"detail": err.detail} for err in error_responses}
            if error_responses
            else None
        )

        super().add_api_route(
            path, endpoint, dependencies=dependencies, responses=responses, **kwargs
        )

    def api_route(
        self, path: str, *args: Any, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        """Overrides and exiting route if it exists"""
        methods = kwargs["methods"] if "methods" in kwargs else ["GET"]
        self.remove_api_route(path, methods)
        return super().api_route(path, *args, **kwargs)

    def get(
        self, path: str, *args: Any, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        self.remove_api_route(path, ["Get"])
        return super().get(path, *args, **kwargs)

    def post(
        self, path: str, *args: Any, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        self.remove_api_route(path, ["POST"])
        return super().post(path, *args, **kwargs)

    def put(
        self, path: str, *args: Any, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        self.remove_api_route(path, ["PUT"])
        return super().put(path, *args, **kwargs)

    def delete(
        self, path: str, *args: Any, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        self.remove_api_route(path, ["DELETE"])
        return super().delete(path, *args, **kwargs)

    def remove_api_route(self, path: str, methods: List[str]) -> None:
        methods_ = set(methods)

        for route in self.routes:
            if (
                route.path == f"{self.prefix}{path}"  # type: ignore
                and route.methods == methods_  # type: ignore
            ):
                self.routes.remove(route)

    @abstractmethod
    def _get_all(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    @abstractmethod
    def _get_one(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    @abstractmethod
    def _create(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    @abstractmethod
    def _update(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    @abstractmethod
    def _delete_one(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    @abstractmethod
    def _delete_all(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        raise NotImplementedError

    def _raise(self, e: Exception, status_code: int = 422) -> HTTPException:
        raise HTTPException(422, ", ".join(e.args)) from e

    @staticmethod
    def get_routes() -> List[str]:
        return ["get_all", "create", "delete_all", "get_one", "update", "delete_one"]

```

**code file end: fastapi_crudrouter/core/_base.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/_types.py 

```python
from typing import Dict, TypeVar, Optional, Sequence

from fastapi.params import Depends
from pydantic import BaseModel

PAGINATION = Dict[str, Optional[int]]
PYDANTIC_SCHEMA = BaseModel

T = TypeVar("T", bound=BaseModel)
DEPENDENCIES = Optional[Sequence[Depends]]

```

**code file end: fastapi_crudrouter/core/_types.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/_utils.py 

```python
from typing import Optional, Type, Any

from fastapi import Depends, HTTPException
from pydantic import create_model

from ._types import T, PAGINATION, PYDANTIC_SCHEMA


class AttrDict(dict):  # type: ignore
    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_pk_type(schema: Type[PYDANTIC_SCHEMA], pk_field: str) -> Any:
    try:
        return schema.__fields__[pk_field].type_
    except KeyError:
        return int


def schema_factory(
    schema_cls: Type[T], pk_field_name: str = "id", name: str = "Create"
) -> Type[T]:
    """
    Is used to create a CreateSchema which does not contain pk
    """

    fields = {
        f.name: (f.type_, ...)
        for f in schema_cls.__fields__.values()
        if f.name != pk_field_name
    }

    name = schema_cls.__name__ + name
    schema: Type[T] = create_model(__model_name=name, **fields)  # type: ignore
    return schema


def create_query_validation_exception(field: str, msg: str) -> HTTPException:
    return HTTPException(
        422,
        detail={
            "detail": [
                {"loc": ["query", field], "msg": msg, "type": "type_error.integer"}
            ]
        },
    )


def pagination_factory(max_limit: Optional[int] = None) -> Any:
    """
    Created the pagination dependency to be used in the router
    """

    def pagination(skip: int = 0, limit: Optional[int] = max_limit) -> PAGINATION:
        if skip < 0:
            raise create_query_validation_exception(
                field="skip",
                msg="skip query parameter must be greater or equal to zero",
            )

        if limit is not None:
            if limit <= 0:
                raise create_query_validation_exception(
                    field="limit", msg="limit query parameter must be greater then zero"
                )

            elif max_limit and max_limit < limit:
                raise create_query_validation_exception(
                    field="limit",
                    msg=f"limit query parameter must be less then {max_limit}",
                )

        return {"skip": skip, "limit": limit}

    return Depends(pagination)

```

**code file end: fastapi_crudrouter/core/_utils.py**
-------------------------------------------


### code file start: fastapi_crudrouter/core/__init__.py 

```python
from . import _utils
from ._base import NOT_FOUND, CRUDGenerator
from .databases import DatabasesCRUDRouter
from .gino_starlette import GinoCRUDRouter
from .mem import MemoryCRUDRouter
from .ormar import OrmarCRUDRouter
from .sqlalchemy import SQLAlchemyCRUDRouter
from .tortoise import TortoiseCRUDRouter

__all__ = [
    "_utils",
    "CRUDGenerator",
    "NOT_FOUND",
    "MemoryCRUDRouter",
    "SQLAlchemyCRUDRouter",
    "DatabasesCRUDRouter",
    "TortoiseCRUDRouter",
    "OrmarCRUDRouter",
    "GinoCRUDRouter",
]

```

**code file end: fastapi_crudrouter/core/__init__.py**
-------------------------------------------


### code file start: tests/conftest.py 

```python
import pytest
from fastapi.testclient import TestClient

from .implementations import *


def yield_test_client(app, impl):
    if impl.__name__ == "tortoise_implementation":
        from tortoise.contrib.test import initializer, finalizer

        initializer(["tests.implementations.tortoise_"])
        with TestClient(app) as c:
            yield c
        finalizer()

    else:
        with TestClient(app) as c:
            yield c


def label_func(*args):
    func, dsn = args[0]
    dsn = dsn.split(":")[0].split("+")[0]
    return f"{func.__name__}-{dsn}"


@pytest.fixture(params=implementations, ids=label_func, scope="class")
def client(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    [app.include_router(router(**kwargs)) for kwargs in settings]
    yield from yield_test_client(app, impl)


@pytest.fixture(
    params=[
        sqlalchemy_implementation_custom_ids,
        databases_implementation_custom_ids,
        ormar_implementation_custom_ids,
        gino_implementation_custom_ids,
    ]
)
def custom_id_client(request):
    yield from yield_test_client(request.param(), request.param)


@pytest.fixture(
    params=[
        sqlalchemy_implementation_string_pk,
        databases_implementation_string_pk,
        ormar_implementation_string_pk,
        gino_implementation_string_pk,
    ],
    scope="function",
)
def string_pk_client(request):
    yield from yield_test_client(request.param(), request.param)


@pytest.fixture(
    params=[
        sqlalchemy_implementation_integrity_errors,
        ormar_implementation_integrity_errors,
        gino_implementation_integrity_errors,
    ],
    scope="function",
)
def integrity_errors_client(request):
    yield from yield_test_client(request.param(), request.param)

```

**code file end: tests/conftest.py**
-------------------------------------------


### code file start: tests/test_base.py 

```python
from abc import ABC
from typing import Type

import pytest
from fastapi import APIRouter, FastAPI

from fastapi_crudrouter import (
    GinoCRUDRouter,
    MemoryCRUDRouter,
    OrmarCRUDRouter,
    SQLAlchemyCRUDRouter,
    DatabasesCRUDRouter,
)

# noinspection PyProtectedMember
from fastapi_crudrouter.core._base import CRUDGenerator
from tests import Potato


@pytest.fixture(
    params=[
        GinoCRUDRouter,
        SQLAlchemyCRUDRouter,
        MemoryCRUDRouter,
        OrmarCRUDRouter,
        GinoCRUDRouter,
        DatabasesCRUDRouter,
    ]
)
def subclass(request) -> Type[CRUDGenerator]:
    return request.param


def test_router_is_subclass_of_crud_generator(subclass):
    assert issubclass(subclass, CRUDGenerator)


def test_router_is_subclass_of_api_router(subclass):
    assert issubclass(subclass, APIRouter)


def test_base_class_is_abstract():
    assert issubclass(CRUDGenerator, ABC)


def test_raise_not_implemented():
    app = FastAPI()

    def foo(*args, **kwargs):
        def bar():
            pass

        return bar

    methods = CRUDGenerator.get_routes()

    for m in methods:
        with pytest.raises(TypeError):
            app.include_router(CRUDGenerator(schema=Potato))

        setattr(CRUDGenerator, f"_{m}", foo)

```

**code file end: tests/test_base.py**
-------------------------------------------


### code file start: tests/test_custom_ids.py 

```python
import pytest

from . import test_router

basic_potato = dict(potato_id=1, thickness=0.24, mass=1.2, color="Brown", type="Russet")

PotatoUrl = "/potatoes"


def test_get(custom_id_client):
    test_router.test_get(custom_id_client, PotatoUrl)


def test_post(custom_id_client):
    test_router.test_post(custom_id_client, PotatoUrl, basic_potato)


def test_get_one(custom_id_client):
    test_router.test_get_one(
        custom_id_client, PotatoUrl, basic_potato, id_key="potato_id"
    )


def test_update(custom_id_client):
    test_router.test_update(
        custom_id_client, PotatoUrl, basic_potato, id_key="potato_id"
    )


def test_delete_one(custom_id_client):
    test_router.test_delete_one(
        custom_id_client, PotatoUrl, basic_potato, id_key="potato_id"
    )


def test_delete_all(custom_id_client):
    test_router.test_delete_all(custom_id_client, PotatoUrl, basic_potato)


@pytest.mark.parametrize("id_", [-1, 0, 4, "14"])
def test_not_found(custom_id_client, id_):
    test_router.test_not_found(custom_id_client, id_, PotatoUrl, basic_potato)

```

**code file end: tests/test_custom_ids.py**
-------------------------------------------


### code file start: tests/test_exclude.py 

```python
import random
import pytest

from fastapi import FastAPI, testclient
from fastapi_crudrouter import MemoryCRUDRouter

from tests import Potato

URL = "/potato"


def get_client(**kwargs):
    app = FastAPI()
    app.include_router(MemoryCRUDRouter(schema=Potato, prefix=URL, **kwargs))

    return testclient.TestClient(app)


@pytest.mark.parametrize("i", list(range(1, len(MemoryCRUDRouter.get_routes()) + 1)))
def test_exclude_internal(i):
    keys = random.sample(MemoryCRUDRouter.get_routes(), k=i)
    kwargs = {r + "_route": False for r in keys}

    router = MemoryCRUDRouter(schema=Potato, prefix=URL, **kwargs)
    assert len(router.routes) == len(MemoryCRUDRouter.get_routes()) - i


def test_exclude_delete_all():
    client = get_client(delete_all_route=False)
    assert client.delete(URL).status_code == 405
    assert client.get(URL).status_code == 200


def test_exclude_all():
    routes = MemoryCRUDRouter.get_routes()
    kwargs = {r + "_route": False for r in routes}
    client = get_client(**kwargs)

    assert client.delete(URL).status_code == 404
    assert client.get(URL).status_code == 404
    assert client.post(URL).status_code == 404
    assert client.put(URL).status_code == 404

    for id_ in [-1, 1, 0, 14]:
        assert client.get(f"{URL}/{id_}").status_code == 404
        assert client.post(f"{URL}/{id_}").status_code == 404
        assert client.put(f"{URL}/{id_}").status_code == 404
        assert client.delete(f"{URL}/{id_}").status_code == 404

```

**code file end: tests/test_exclude.py**
-------------------------------------------


### code file start: tests/test_integrity_errors.py 

```python
import pytest

from tests import test_router

POTATO_URL = "/potatoes"


def test_integrity_error_create(integrity_errors_client):
    client = integrity_errors_client
    potato = dict(id=1, thickness=2, mass=5, color="red", type="russet")

    args = client, POTATO_URL, potato
    test_router.test_post(*args)
    with pytest.raises(AssertionError):
        test_router.test_post(*args)

    # No integrity error here because of the create_schema
    args = client, "/carrots", dict(id=1, length=2, color="red")
    test_router.test_post(*args)
    test_router.test_post(*args, expected_length=2)


def test_integrity_error_update(integrity_errors_client):
    client = integrity_errors_client
    potato1 = dict(id=1, thickness=2, mass=5, color="red", type="russet")

    potato2 = dict(id=2, thickness=9, mass=5, color="yellow", type="mini")

    args = client, POTATO_URL
    test_router.test_post(*args, potato1, expected_length=1)
    test_router.test_post(*args, potato2, expected_length=2)

    potato2["color"] = potato1["color"]
    res = client.put(f'{POTATO_URL}/{potato2["id"]}', json=potato2)
    assert res.status_code == 422, res.json()

    potato2["color"] = "green"
    res = client.put(f'{POTATO_URL}/{potato2["id"]}', json=potato2)
    assert res.status_code == 200, res.json()

```

**code file end: tests/test_integrity_errors.py**
-------------------------------------------


### code file start: tests/test_openapi_schema.py 

```python
from pytest import mark

from tests import CUSTOM_TAGS

POTATO_TAGS = ["Potato"]
PATHS = ["/potato", "/carrot"]
PATH_TAGS = {
    "/potato": POTATO_TAGS,
    "/potato/{item_id}": POTATO_TAGS,
    "/carrot": CUSTOM_TAGS,
    "/carrot/{item_id}": CUSTOM_TAGS,
}


class TestOpenAPISpec:
    def test_schema_exists(self, client):
        res = client.get("/openapi.json")
        assert res.status_code == 200

        return res

    def test_schema_tags(self, client):
        schema = self.test_schema_exists(client).json()
        paths = schema["paths"]

        assert len(paths) == len(PATH_TAGS)
        for path, method in paths.items():
            assert len(method) == 3

            for m in method:
                assert method[m]["tags"] == PATH_TAGS[path]

    @mark.parametrize("path", PATHS)
    def test_response_types(self, client, path):
        schema = self.test_schema_exists(client).json()
        paths = schema["paths"]

        for method in ["get", "post", "delete"]:
            assert "200" in paths[path][method]["responses"]

        assert "422" in paths[path]["post"]["responses"]

        item_path = path + "/{item_id}"
        for method in ["get", "put", "delete"]:
            assert "200" in paths[item_path][method]["responses"]
            assert "404" in paths[item_path][method]["responses"]
            assert "422" in paths[item_path][method]["responses"]

```

**code file end: tests/test_openapi_schema.py**
-------------------------------------------


### code file start: tests/test_overloads.py 

```python
import pytest
from fastapi import APIRouter

from .implementations import implementations
from .conftest import yield_test_client


URLs = ["/potato", "/carrot"]
PARAMS = [-1, 0, 1, 14, "ten"]

GET_ALL = "Overloaded Get All"
GET_ONE = "Overloaded Get One"
CREATE_ONE = "Overloaded Post One"
UPDATE_ONE = "Overloaded Update One"
DELETE_ONE = "Overloaded Delete One"
DELETE_ALL = "Overloaded Delete All"
CUSTOM_ROUTE = "Custom Route"


@pytest.fixture(params=implementations, scope="class")
def overloaded_client(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    routers = [router(**s) for s in settings]

    for r in routers:
        r: APIRouter

        @r.api_route("", methods=["GET"])
        def overloaded_get_all():
            return GET_ALL

        @r.get("/{item_id}")
        def overloaded_get_one():
            return GET_ONE

        @r.post("")
        def overloaded_get():
            return CREATE_ONE

        @r.put("/{item_id}")
        def overloaded_update():
            return UPDATE_ONE

        @r.delete("/{item_id}")
        def overloaded_delete():
            return DELETE_ONE

        @r.api_route("", methods=["DELETE"])
        def overloaded_delete():
            return DELETE_ALL

        @r.post("/custom")
        def custom_route():
            return CUSTOM_ROUTE

        app.include_router(r)

    yield from yield_test_client(app, impl)


@pytest.fixture(params=URLs)
def url(request):
    yield request.param


class TestOverloads:
    @staticmethod
    def check_response(res, expected):
        assert res.status_code == 200
        assert expected in res.text

    def test_get_all(self, overloaded_client, url):
        return self.check_response(overloaded_client.get(url), GET_ALL)

    @pytest.mark.parametrize("id_", PARAMS)
    def test_get_one(self, overloaded_client, url, id_):
        self.check_response(overloaded_client.get(f"{url}/{id_}"), GET_ONE)

    def test_create(self, overloaded_client, url):
        self.check_response(overloaded_client.post(url), CREATE_ONE)

    @pytest.mark.parametrize("id_", PARAMS)
    def test_update(self, overloaded_client, url, id_):
        self.check_response(overloaded_client.put(f"{url}/{id_}"), UPDATE_ONE)

    @pytest.mark.parametrize("id_", PARAMS)
    def test_delete(self, overloaded_client, url, id_):
        self.check_response(overloaded_client.delete(f"{url}/{id_}"), DELETE_ONE)

    def test_delete_all(self, overloaded_client, url):
        self.check_response(overloaded_client.delete(url), DELETE_ALL)

    def test_custom_route(self, overloaded_client, url):
        self.check_response(overloaded_client.post(f"{url}/custom"), CUSTOM_ROUTE)

```

**code file end: tests/test_overloads.py**
-------------------------------------------


### code file start: tests/test_pagination.py 

```python
import typing

import pytest

from . import PAGINATION_SIZE, test_router

PotatoUrl = "/potato"
CarrotUrl = "/carrot"
basic_carrot = dict(length=1.2, color="Orange")
basic_potato = dict(thickness=0.24, mass=1.2, color="Brown", type="Russet")

INSERT_COUNT = 20


@pytest.fixture(scope="class")
def insert_items(
    client,
    url: str = PotatoUrl,
    model: typing.Dict = None,
    count: int = INSERT_COUNT,
):
    model = model or basic_potato
    for i in range(count):
        test_router.test_post(
            client,
            url=url,
            model=model,
            expected_length=i + 1 if i + 1 < PAGINATION_SIZE else PAGINATION_SIZE,
        )


@pytest.fixture(scope="class")
def insert_carrots(client):
    for i in range(INSERT_COUNT):
        test_router.test_post(client, CarrotUrl, basic_carrot, expected_length=i + 1)


@pytest.fixture(scope="class")
def cleanup(client):
    yield
    client.delete(CarrotUrl)
    client.delete(PotatoUrl)


def get_expected_length(limit, offset, count: int = INSERT_COUNT):
    expected_length = limit
    if offset >= count:
        expected_length = 0

    elif offset + limit >= INSERT_COUNT:
        expected_length = INSERT_COUNT - offset

    return expected_length


@pytest.mark.usefixtures("insert_carrots", "insert_items", "cleanup")
class TestPagination:
    @pytest.mark.parametrize("offset", [0, 1, 5, 10, 20, 40])
    @pytest.mark.parametrize("limit", [1, 5, 10])
    def test_pagination(self, client, limit, offset):
        test_router.test_get(
            client=client,
            url=PotatoUrl,
            params={"limit": limit, "skip": offset},
            expected_length=get_expected_length(limit, offset),
        )

    @pytest.mark.parametrize("offset", [-1, "asdas", 3.23])
    def test_invalid_offset(self, client, offset):
        res = client.get(PotatoUrl, params={"skip": offset})
        assert res.status_code == 422

    @pytest.mark.parametrize("limit", [-1, 0, "asdas", 3.23, 21])
    def test_invalid_limit(self, client, limit):
        res = client.get(PotatoUrl, params={"limit": limit})
        assert res.status_code == 422

    def test_pagination_disabled(self, client):
        test_router.test_get(client, CarrotUrl, expected_length=INSERT_COUNT)

    @pytest.mark.parametrize("limit", [2, 5, 10])
    def test_paging(self, client, limit):
        ids = set()
        skip = 0
        while skip < INSERT_COUNT:
            data = test_router.test_get(
                client,
                PotatoUrl,
                params={"limit": limit, "skip": skip},
                expected_length=get_expected_length(limit, skip),
            )

            for item in data:
                assert item["id"] not in ids
                ids.add(item["id"])

            skip += limit

        assert len(ids) == INSERT_COUNT

    @pytest.mark.parametrize("limit", [2, 5, 10])
    def test_paging_no_limit(self, client, limit):
        client.delete(CarrotUrl)
        for i in range(limit):
            res = client.post(url=CarrotUrl, json=basic_carrot)
            assert res.status_code == 200, res.json()

        res = client.get(CarrotUrl)
        assert res.status_code == 200, res.json()
        assert len(res.json()) == limit

        res = client.get(CarrotUrl, params={"limit": limit})
        assert res.status_code == 200, res.json()
        assert len(res.json()) == limit

        limit = int(limit / 2)
        res = client.get(CarrotUrl, params={"limit": limit})
        assert res.status_code == 200, res.json()
        assert len(res.json()) == limit

```

**code file end: tests/test_pagination.py**
-------------------------------------------


### code file start: tests/test_pks.py 

```python
from . import test_router

potato_type = dict(name="russet", origin="Canada")
URL = "/potato_type"


def test_get(string_pk_client):
    test_router.test_get(string_pk_client, URL)


def test_post(string_pk_client):
    test_router.test_post(string_pk_client, URL, potato_type)


def test_get_one(string_pk_client):
    test_router.test_get_one(
        string_pk_client, URL, dict(name="kenebec", origin="Ireland"), "name"
    )


def test_delete_one(string_pk_client):
    test_router.test_delete_one(
        string_pk_client, URL, dict(name="golden", origin="Ireland"), "name"
    )


def test_delete_all(string_pk_client):
    test_router.test_delete_all(
        string_pk_client,
        URL,
        dict(name="red", origin="Ireland"),
        dict(name="brown", origin="Ireland"),
    )

```

**code file end: tests/test_pks.py**
-------------------------------------------


### code file start: tests/test_prefix.py 

```python
import pytest

from tests.implementations import implementations


@pytest.fixture(params=implementations)
def router(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    kwargs = {**settings[0], **dict(prefix=None)}
    router = router(**kwargs)

    yield router


def test_prefix_lowercase(router):
    assert type(router.prefix) is str
    assert router.prefix != ""
    assert router.prefix == router.prefix.lower()

```

**code file end: tests/test_prefix.py**
-------------------------------------------


### code file start: tests/test_router.py 

```python
from typing import Dict

import pytest

from .utils import compare_dict

basic_potato = dict(thickness=0.24, mass=1.2, color="Brown", type="Russet")
URL = "/potato"


def test_get(client, url: str = URL, params: dict = None, expected_length: int = 0):
    res = client.get(url, params=params)
    data = res.json()

    assert res.status_code == 200, data
    assert type(data) == list and len(data) == expected_length

    return data


def test_post(
    client, url: str = URL, model: Dict = None, expected_length: int = 1
) -> dict:
    model = model or basic_potato
    res = client.post(url, json=model)
    assert res.status_code == 200, res.json()

    data = client.get(url).json()
    assert len(data) == expected_length

    return res.json()


def test_get_one(client, url: str = URL, model: Dict = None, id_key: str = "id"):
    model = model or basic_potato
    res = client.post(url, json=model)
    assert res.status_code == 200
    id_ = res.json()[id_key]

    data = client.get(url).json()
    assert len(data)

    res = client.get(f"{url}/{id_}")
    assert res.status_code == 200

    assert compare_dict(res.json(), model, exclude=[id_key])


def test_update(client, url: str = URL, model: Dict = None, id_key: str = "id"):
    test_get(client, url, expected_length=0)

    model = model or basic_potato
    res = client.post(url, json=model)
    data = res.json()
    assert res.status_code == 200

    test_get(client, url, expected_length=1)

    tuber = {k: v for k, v in model.items()}
    tuber["color"] = "yellow"

    res = client.put(f"{url}/{data[id_key]}", json=tuber)
    assert res.status_code == 200
    assert compare_dict(res.json(), tuber, exclude=[id_key])
    assert not compare_dict(res.json(), model, exclude=[id_key])

    res = client.get(f"{url}/{data[id_key]}")
    assert res.status_code == 200
    assert compare_dict(res.json(), tuber, exclude=[id_key])
    assert not compare_dict(res.json(), model, exclude=[id_key])


def test_delete_one(client, url: str = URL, model: Dict = None, id_key: str = "id"):
    model = model or basic_potato
    res = client.post(url, json=model)
    data = res.json()
    assert res.status_code == 200

    res = client.get(f"{url}/{data[id_key]}")
    assert res.status_code == 200
    assert compare_dict(res.json(), model, exclude=[id_key])

    length_before = len(client.get(url).json())

    res = client.delete(f"{url}/{data[id_key]}")
    assert res.status_code == 200
    assert compare_dict(res.json(), model, exclude=[id_key])

    res = client.get(url)
    assert res.status_code == 200
    assert len(res.json()) < length_before


def test_delete_all(
    client,
    url: str = URL,
    model: Dict = None,
    model2: Dict = None,
):
    model = model or basic_potato
    model2 = model2 or basic_potato

    res = client.post(url, json=model)
    assert res.status_code == 200

    res = client.post(url, json=model2)
    assert res.status_code == 200

    assert len(client.get(url).json()) >= 2

    res = client.delete(url)
    assert res.status_code == 200
    assert len(res.json()) == 0

    assert len(client.get(url).json()) == 0


@pytest.mark.parametrize("id_", [-1, 0, 4, "14"])
def test_not_found(client, id_, url: str = URL, model: Dict = None):
    url = f"{url}/{id_}"
    model = model or basic_potato
    assert client.get(url).status_code == 404
    assert client.put(url, json=model).status_code == 404
    assert client.delete(url).status_code == 404


def test_dne(client):
    res = client.get("/")
    assert res.status_code == 404

    res = client.get(f"/tomatoes")
    assert res.status_code == 404

```

**code file end: tests/test_router.py**
-------------------------------------------


### code file start: tests/test_sqlalchemy_nested_.py 

```python
from typing import List

from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from tests import ORMModel, test_router
from tests.implementations.sqlalchemy_ import _setup_base_app

CHILD_URL = "/child"
PARENT_URL = "/parent"


class ChildSchema(ORMModel):
    parent_id: int


class ParentSchema(ORMModel):
    children: List[ChildSchema] = []


class ParentCreate(BaseModel):
    pass


def create_app():
    app, engine, Base, session = _setup_base_app()

    class Child(Base):
        __tablename__ = "child"
        id = Column(Integer, primary_key=True, index=True)
        parent_id = Column(Integer, ForeignKey("parent.id"))

    class Parent(Base):
        __tablename__ = "parent"
        id = Column(Integer, primary_key=True, index=True)

        children = relationship(Child, backref="parent", lazy="joined")

    Base.metadata.create_all(bind=engine)
    parent_router = SQLAlchemyCRUDRouter(
        schema=ParentSchema,
        create_schema=ParentCreate,
        db_model=Parent,
        db=session,
        prefix=PARENT_URL,
    )
    child_router = SQLAlchemyCRUDRouter(
        schema=ChildSchema, db_model=Child, db=session, prefix=CHILD_URL
    )
    app.include_router(parent_router)
    app.include_router(child_router)

    return app


def test_nested_models():
    client = TestClient(create_app())

    parent = test_router.test_post(client, PARENT_URL, dict())
    test_router.test_post(client, CHILD_URL, dict(id=0, parent_id=parent["id"]))

    res = client.get(f'{PARENT_URL}/{parent["id"]}')
    assert res.status_code == 200, res.json()

    data = res.json()
    assert type(data["children"]) is list and data["children"], data

```

**code file end: tests/test_sqlalchemy_nested_.py**
-------------------------------------------


### code file start: tests/test_two_routers.py 

```python
import pytest

from . import test_router
from .utils import compare_dict

basic_potato = dict(thickness=0.24, mass=1.2, color="Brown", type="Russet")
basic_carrot = dict(length=1.2, color="Orange")

PotatoUrl = "/potato"
CarrotUrl = "/carrot"


def test_get(client):
    test_router.test_get(client, PotatoUrl)
    test_router.test_get(client, CarrotUrl)


def test_post(client):
    test_router.test_post(client, PotatoUrl, basic_potato)
    test_router.test_post(client, CarrotUrl, basic_carrot)


def test_get_one(client):
    test_router.test_get_one(client, PotatoUrl, basic_potato)
    test_router.test_get_one(client, CarrotUrl, basic_carrot)


def test_update(client):
    test_router.test_update(client, PotatoUrl, basic_potato)

    with pytest.raises(AssertionError):
        test_router.test_update(client, CarrotUrl, basic_carrot)

    res = client.post(CarrotUrl, json=basic_carrot)
    data = res.json()
    assert res.status_code == 200

    carrot = {k: v for k, v in basic_carrot.items()}
    carrot["color"] = "Red"
    carrot["length"] = 54.0

    res = client.put(f'{CarrotUrl}/{data["id"]}', json=carrot)
    assert res.status_code == 200
    assert not compare_dict(res.json(), carrot, exclude=["id"])
    assert not compare_dict(res.json(), basic_carrot, exclude=["id"])
    assert compare_dict(res.json(), carrot, exclude=["id", "color"])

    res = client.get(f'{CarrotUrl}/{data["id"]}')
    assert res.status_code == 200
    assert not compare_dict(res.json(), carrot, exclude=["id"])
    assert not compare_dict(res.json(), basic_carrot, exclude=["id"])
    assert compare_dict(res.json(), carrot, exclude=["id", "color"])


def test_delete_one(client):
    test_router.test_delete_one(client, PotatoUrl, basic_potato)
    test_router.test_delete_one(client, CarrotUrl, basic_carrot)


def test_delete_all(client):
    test_router.test_delete_all(client, PotatoUrl, basic_potato)
    test_router.test_delete_all(client, CarrotUrl, basic_carrot, basic_carrot)


@pytest.mark.parametrize("id_", [-1, 0, 4, "14"])
def test_not_found(client, id_):
    test_router.test_not_found(client, id_, PotatoUrl, basic_potato)
    test_router.test_not_found(client, id_, CarrotUrl, basic_carrot)

```

**code file end: tests/test_two_routers.py**
-------------------------------------------


### code file start: tests/test_version.py 

```python
def test_version():
    import fastapi_crudrouter

    assert type(fastapi_crudrouter.__version__) is str


def test_version_file():
    from fastapi_crudrouter import _version

    assert type(_version.__version__) is str

```

**code file end: tests/test_version.py**
-------------------------------------------


### code file start: tests/utils.py 

```python
def compare_dict(d1, d2, exclude: list) -> bool:
    exclude = exclude or ["id"]
    d1 = {k: v for k, v in d1.items() if k not in exclude}
    d2 = {k: v for k, v in d2.items() if k not in exclude}
    return d1 == d2

```

**code file end: tests/utils.py**
-------------------------------------------


### code file start: tests/__init__.py 

```python
from pydantic import BaseModel

from .conf import config

PAGINATION_SIZE = 10
CUSTOM_TAGS = ["Tag1", "Tag2"]


class ORMModel(BaseModel):
    id: int

    class Config:
        orm_mode = True


class PotatoCreate(BaseModel):
    thickness: float
    mass: float
    color: str
    type: str


class Potato(PotatoCreate, ORMModel):
    pass


class CustomPotato(PotatoCreate):
    potato_id: int

    class Config:
        orm_mode = True


class CarrotCreate(BaseModel):
    length: float
    color: str = "Orange"


class CarrotUpdate(BaseModel):
    length: float


class Carrot(CarrotCreate, ORMModel):
    pass


class PotatoType(BaseModel):
    name: str
    origin: str

    class Config:
        orm_mode = True

```

**code file end: tests/__init__.py**
-------------------------------------------


### code file start: tests/conf/config.py 

```python
import os
import pathlib


ENV_FILE_PATH = pathlib.Path(__file__).parent / "dev.env"
assert ENV_FILE_PATH.exists()


class BaseConfig:
    POSTGRES_HOST = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    POSTGRES_DB = ""
    POSTGRES_PORT = ""

    MSSQL_PORT = ""
    SA_PASSWORD = ""

    def __init__(self):
        self._apply_dot_env()
        self._apply_env_vars()
        self.POSTGRES_URI = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        self.MSSQL_URI = f"mssql+pyodbc://sa:{self.SA_PASSWORD}@{self.POSTGRES_HOST}:{self.MSSQL_PORT}/test?driver=SQL+Server"

    def _apply_dot_env(self):
        with open(ENV_FILE_PATH) as fp:
            for line in fp.readlines():
                line = line.strip(" \n")

                if line and not line.startswith("#"):
                    k, v = line.split("=", 1)

                    if hasattr(self, k) and not getattr(self, k):
                        setattr(self, k, v)

    def _apply_env_vars(self):
        for k, v in os.environ.items():
            if hasattr(self, k):
                setattr(self, k, v)

```

**code file end: tests/conf/config.py**
-------------------------------------------


### code file start: tests/conf/__init__.py 

```python
from .config import BaseConfig

config = BaseConfig()

```

**code file end: tests/conf/__init__.py**
-------------------------------------------


### code file start: tests/implementations/databases_.py 

```python
import databases
from fastapi import FastAPI
from sqlalchemy import Column, Float, Integer, MetaData, String, Table, create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database

from fastapi_crudrouter import DatabasesCRUDRouter
from tests import (
    Carrot,
    CarrotCreate,
    CarrotUpdate,
    CustomPotato,
    PAGINATION_SIZE,
    Potato,
    PotatoType,
    CUSTOM_TAGS,
    config,
)

DSN_LIST = [
    "sqlite:///./test.db?check_same_thread=false",
    # config.MSSQL_URI,
    config.POSTGRES_URI,
]


def _setup_database(db_uri: str = DSN_LIST[0]):
    if database_exists(db_uri):
        drop_database(db_uri)

    create_database(db_uri)
    database = databases.Database(db_uri)
    engine = create_engine(db_uri)

    return engine, database


def databases_implementation(db_uri: str):
    engine, database = _setup_database(db_uri)

    metadata = MetaData()
    potatoes = Table(
        "potatoes",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("thickness", Float),
        Column("mass", Float),
        Column("color", String),
        Column("type", String),
    )
    carrots = Table(
        "carrots",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("length", Float),
        Column("color", String),
    )
    metadata.create_all(bind=engine)

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    router_settings = [
        dict(
            database=database,
            table=potatoes,
            schema=Potato,
            prefix="potato",
            paginate=PAGINATION_SIZE,
        ),
        dict(
            database=database,
            table=carrots,
            schema=Carrot,
            create_schema=CarrotCreate,
            update_schema=CarrotUpdate,
            prefix="carrot",
            tags=CUSTOM_TAGS,
        ),
    ]

    return app, DatabasesCRUDRouter, router_settings


def databases_implementation_custom_ids():
    engine, database = _setup_database()

    metadata = MetaData()
    potatoes = Table(
        "potatoes",
        metadata,
        Column("potato_id", Integer, primary_key=True),
        Column("thickness", Float),
        Column("mass", Float),
        Column("color", String),
        Column("type", String),
    )

    metadata.create_all(bind=engine)

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    potato_router = DatabasesCRUDRouter(
        database=database, table=potatoes, schema=CustomPotato
    )
    app.include_router(potato_router)

    return app


def databases_implementation_string_pk():
    engine, database = _setup_database()

    metadata = MetaData()
    potato_types = Table(
        "potato_type",
        metadata,
        Column("name", String, primary_key=True),
        Column("origin", String),
    )

    metadata.create_all(bind=engine)

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    potato_router = DatabasesCRUDRouter(
        database=database,
        table=potato_types,
        schema=PotatoType,
        create_schema=PotatoType,
    )
    app.include_router(potato_router)

    return app

```

**code file end: tests/implementations/databases_.py**
-------------------------------------------


### code file start: tests/implementations/gino_.py 

```python
import asyncio
from fastapi import FastAPI
from fastapi_crudrouter import GinoCRUDRouter
from gino.ext.starlette import Gino
from sqlalchemy_utils import create_database, database_exists, drop_database
from tests import (
    CUSTOM_TAGS,
    PAGINATION_SIZE,
    Carrot,
    CarrotCreate,
    CarrotUpdate,
    CustomPotato,
    Potato,
    PotatoType,
    config,
)


GINO_DATABASE_URL = config.POSTGRES_URI.replace("postgresql", "asyncpg")


async def migrate(db):
    async with db.with_bind(GINO_DATABASE_URL):
        await db.gino.create_all()


def _setup_base_app():
    if database_exists(config.POSTGRES_URI):
        drop_database(config.POSTGRES_URI)

    create_database(config.POSTGRES_URI)

    app = FastAPI()
    db = Gino(dsn=GINO_DATABASE_URL)
    db.init_app(app)
    return db, app


def gino_implementation(**kwargs):
    db, app = _setup_base_app()

    class PotatoModel(db.Model):
        __tablename__ = "potatoes"
        id = db.Column(db.Integer, primary_key=True, index=True)
        thickness = db.Column(db.Float)
        mass = db.Column(db.Float)
        color = db.Column(db.String)
        type = db.Column(db.String)

    class CarrotModel(db.Model):
        __tablename__ = "carrots"
        id = db.Column(db.Integer, primary_key=True, index=True)
        length = db.Column(db.Float)
        color = db.Column(db.String)

    asyncio.get_event_loop().run_until_complete(migrate(db))

    router_settings = [
        dict(
            schema=Potato,
            db_model=PotatoModel,
            db=db,
            prefix="potato",
            paginate=PAGINATION_SIZE,
        ),
        dict(
            schema=Carrot,
            db_model=CarrotModel,
            db=db,
            create_schema=CarrotCreate,
            update_schema=CarrotUpdate,
            prefix="carrot",
            tags=CUSTOM_TAGS,
        ),
    ]

    return app, GinoCRUDRouter, router_settings


# noinspection DuplicatedCode
def gino_implementation_custom_ids():
    db, app = _setup_base_app()

    class PotatoModel(db.Model):
        __tablename__ = "potatoes"
        potato_id = db.Column(db.Integer, primary_key=True, index=True)
        thickness = db.Column(db.Float)
        mass = db.Column(db.Float)
        color = db.Column(db.String)
        type = db.Column(db.String)

    asyncio.get_event_loop().run_until_complete(migrate(db))

    app.include_router(GinoCRUDRouter(schema=CustomPotato, db_model=PotatoModel, db=db))

    return app


def gino_implementation_string_pk():
    db, app = _setup_base_app()

    class PotatoTypeModel(db.Model):
        __tablename__ = "potato_type"
        name = db.Column(db.String, primary_key=True, index=True)
        origin = db.Column(db.String)

    asyncio.get_event_loop().run_until_complete(migrate(db))

    app.include_router(
        GinoCRUDRouter(
            schema=PotatoType,
            create_schema=PotatoType,
            db_model=PotatoTypeModel,
            db=db,
            prefix="potato_type",
        )
    )

    return app


def gino_implementation_integrity_errors():
    db, app = _setup_base_app()

    class PotatoModel(db.Model):
        __tablename__ = "potatoes"
        id = db.Column(db.Integer, primary_key=True, index=True)
        thickness = db.Column(db.Float)
        mass = db.Column(db.Float)
        color = db.Column(db.String, unique=True)
        type = db.Column(db.String)

    class CarrotModel(db.Model):
        __tablename__ = "carrots"
        id = db.Column(db.Integer, primary_key=True, index=True)
        length = db.Column(db.Float)
        color = db.Column(db.String)

    asyncio.get_event_loop().run_until_complete(migrate(db))

    app.include_router(
        GinoCRUDRouter(
            schema=Potato,
            db_model=PotatoModel,
            db=db,
            create_schema=Potato,
            prefix="potatoes",
        )
    )
    app.include_router(
        GinoCRUDRouter(
            schema=Carrot,
            db_model=CarrotModel,
            db=db,
            update_schema=CarrotUpdate,
            prefix="carrots",
        )
    )

    return app

```

**code file end: tests/implementations/gino_.py**
-------------------------------------------


### code file start: tests/implementations/memory.py 

```python
from fastapi import FastAPI

from fastapi_crudrouter import MemoryCRUDRouter
from tests import Potato, Carrot, CarrotUpdate, PAGINATION_SIZE, CUSTOM_TAGS


def memory_implementation(**kwargs):
    app = FastAPI()
    router_settings = [
        dict(schema=Potato, paginate=PAGINATION_SIZE),
        dict(schema=Carrot, update_schema=CarrotUpdate, tags=CUSTOM_TAGS),
    ]

    return app, MemoryCRUDRouter, router_settings


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(memory_implementation(), port=5000)

```

**code file end: tests/implementations/memory.py**
-------------------------------------------


### code file start: tests/implementations/ormar_.py 

```python
import os

import databases
import ormar
import pytest
import sqlalchemy
from fastapi import FastAPI

from fastapi_crudrouter import OrmarCRUDRouter
from tests import CarrotCreate, CarrotUpdate, PAGINATION_SIZE, CUSTOM_TAGS

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


@pytest.fixture(scope="function", autouse=True)
async def cleanup():
    async with database:
        await PotatoModel.objects.delete(each=True)
        await CarrotModel.objects.delete(each=True)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


def _setup_database():
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    return engine, database


class PotatoModel(ormar.Model):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    thickness = ormar.Float()
    mass = ormar.Float()
    color = ormar.String(max_length=255)
    type = ormar.String(max_length=255)


class CarrotModel(ormar.Model):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    length = ormar.Float()
    color = ormar.String(max_length=255)


class PotatoTypeModel(ormar.Model):
    class Meta(BaseMeta):
        tablename = "potato_type"

    name = ormar.String(primary_key=True, max_length=300)
    origin = ormar.String(max_length=300)


class CustomPotatoModel(ormar.Model):
    class Meta(BaseMeta):
        tablename = "custom_potatoes"

    potato_id = ormar.Integer(primary_key=True)
    thickness = ormar.Float()
    mass = ormar.Float()
    color = ormar.String(max_length=255)
    type = ormar.String(max_length=255)


class UniquePotatoModel(ormar.Model):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    thickness = ormar.Float()
    mass = ormar.Float()
    color = ormar.String(max_length=255, unique=True)
    type = ormar.String(max_length=255)


def get_app():
    [
        os.remove(f"./db.sqlite3{s}")
        for s in ["", "-wal", "-shm"]
        if os.path.exists(f"./db.sqlite3{s}")
    ]

    _setup_database()

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app


def ormar_implementation(**kwargs):
    app = get_app()

    router_settings = [
        dict(
            schema=PotatoModel,
            prefix="potato",
            paginate=PAGINATION_SIZE,
        ),
        dict(
            schema=CarrotModel,
            update_schema=CarrotUpdate,
            prefix="carrot",
            tags=CUSTOM_TAGS,
        ),
    ]

    return (
        app,
        OrmarCRUDRouter,
        router_settings,
    )


# noinspection DuplicatedCode
def ormar_implementation_custom_ids():
    app = get_app()

    app.include_router(
        OrmarCRUDRouter(
            schema=CustomPotatoModel,
            prefix="potatoes",
            paginate=PAGINATION_SIZE,
        )
    )

    return app


def ormar_implementation_string_pk():
    app = get_app()

    app.include_router(
        OrmarCRUDRouter(
            schema=PotatoTypeModel,
            prefix="potato_type",
        )
    )

    return app


def ormar_implementation_integrity_errors():
    app = get_app()

    app.include_router(
        OrmarCRUDRouter(
            schema=UniquePotatoModel,
            prefix="potatoes",
            paginate=PAGINATION_SIZE,
        )
    )
    app.include_router(
        OrmarCRUDRouter(
            schema=CarrotModel,
            create_schema=CarrotCreate,
            update_schema=CarrotUpdate,
            prefix="carrots",
        )
    )

    return app

```

**code file end: tests/implementations/ormar_.py**
-------------------------------------------


### code file start: tests/implementations/sqlalchemy_.py 

```python
from fastapi import FastAPI
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from tests import (
    Carrot,
    CarrotCreate,
    CarrotUpdate,
    CustomPotato,
    PAGINATION_SIZE,
    Potato,
    PotatoType,
    CUSTOM_TAGS,
    config,
)

DSN_LIST = [
    "sqlite:///./test.db?check_same_thread=false",
    # config.MSSQL_URI,
    config.POSTGRES_URI,
]


def _setup_base_app(db_uri: str = DSN_LIST[0]):
    if database_exists(db_uri):
        drop_database(db_uri)

    create_database(db_uri)

    app = FastAPI()

    engine = create_engine(db_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    def session():
        session = SessionLocal()
        try:
            yield session
            session.commit()
        finally:
            session.close()

    return app, engine, Base, session


def sqlalchemy_implementation(db_uri: str):
    app, engine, Base, session = _setup_base_app(db_uri)

    class PotatoModel(Base):
        __tablename__ = "potatoes"
        id = Column(Integer, primary_key=True, index=True)
        thickness = Column(Float)
        mass = Column(Float)
        color = Column(String)
        type = Column(String)

    class CarrotModel(Base):
        __tablename__ = "carrots"
        id = Column(Integer, primary_key=True, index=True)
        length = Column(Float)
        color = Column(String)

    Base.metadata.create_all(bind=engine)
    router_settings = [
        dict(
            schema=Potato,
            db_model=PotatoModel,
            db=session,
            prefix="potato",
            paginate=PAGINATION_SIZE,
        ),
        dict(
            schema=Carrot,
            db_model=CarrotModel,
            db=session,
            create_schema=CarrotCreate,
            update_schema=CarrotUpdate,
            prefix="carrot",
            tags=CUSTOM_TAGS,
        ),
    ]

    return app, SQLAlchemyCRUDRouter, router_settings


# noinspection DuplicatedCode
def sqlalchemy_implementation_custom_ids():
    app, engine, Base, session = _setup_base_app()

    class PotatoModel(Base):
        __tablename__ = "potatoes"
        potato_id = Column(Integer, primary_key=True, index=True)
        thickness = Column(Float)
        mass = Column(Float)
        color = Column(String)
        type = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(
        SQLAlchemyCRUDRouter(schema=CustomPotato, db_model=PotatoModel, db=session)
    )

    return app


def sqlalchemy_implementation_string_pk():
    app, engine, Base, session = _setup_base_app()

    class PotatoTypeModel(Base):
        __tablename__ = "potato_type"
        name = Column(String, primary_key=True, index=True)
        origin = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(
        SQLAlchemyCRUDRouter(
            schema=PotatoType,
            create_schema=PotatoType,
            db_model=PotatoTypeModel,
            db=session,
            prefix="potato_type",
        )
    )

    return app


def sqlalchemy_implementation_integrity_errors():
    app, engine, Base, session = _setup_base_app()

    class PotatoModel(Base):
        __tablename__ = "potatoes"
        id = Column(Integer, primary_key=True, index=True)
        thickness = Column(Float)
        mass = Column(Float)
        color = Column(String, unique=True)
        type = Column(String)

    class CarrotModel(Base):
        __tablename__ = "carrots"
        id = Column(Integer, primary_key=True, index=True)
        length = Column(Float)
        color = Column(String)

    Base.metadata.create_all(bind=engine)
    app.include_router(
        SQLAlchemyCRUDRouter(
            schema=Potato,
            db_model=PotatoModel,
            db=session,
            create_schema=Potato,
            prefix="potatoes",
        )
    )
    app.include_router(
        SQLAlchemyCRUDRouter(
            schema=Carrot,
            db_model=CarrotModel,
            db=session,
            update_schema=CarrotUpdate,
            prefix="carrots",
        )
    )

    return app

```

**code file end: tests/implementations/sqlalchemy_.py**
-------------------------------------------


### code file start: tests/implementations/tortoise_.py 

```python
import os

from fastapi import FastAPI
from tortoise import Model, Tortoise, fields

from fastapi_crudrouter import TortoiseCRUDRouter
from tests import (
    Carrot,
    CarrotCreate,
    CarrotUpdate,
    PAGINATION_SIZE,
    Potato,
    CUSTOM_TAGS,
)


class PotatoModel(Model):
    thickness = fields.FloatField()
    mass = fields.FloatField()
    color = fields.CharField(max_length=255)
    type = fields.CharField(max_length=255)


class CarrotModel(Model):
    length = fields.FloatField()
    color = fields.CharField(max_length=255)


TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["tests.implementations.tortoise_"],
            "default_connection": "default",
        },
    },
}


async def on_shutdown():
    await Tortoise.close_connections()


def tortoise_implementation(**kwargs):
    [
        os.remove(f"./db.sqlite3{s}")
        for s in ["", "-wal", "-shm"]
        if os.path.exists(f"./db.sqlite3{s}")
    ]

    app = FastAPI(on_shutdown=[on_shutdown])

    Tortoise.init(config=TORTOISE_ORM)
    Tortoise.generate_schemas()

    router_settings = [
        dict(
            schema=Potato,
            db_model=PotatoModel,
            prefix="potato",
            paginate=PAGINATION_SIZE,
        ),
        dict(
            schema=Carrot,
            db_model=CarrotModel,
            create_schema=CarrotCreate,
            update_schema=CarrotUpdate,
            prefix="carrot",
            tags=CUSTOM_TAGS,
        ),
    ]

    return app, TortoiseCRUDRouter, router_settings

```

**code file end: tests/implementations/tortoise_.py**
-------------------------------------------


### code file start: tests/implementations/__init__.py 

```python
import sys

from .databases_ import (
    databases_implementation,
    databases_implementation_custom_ids,
    databases_implementation_string_pk,
)
from .gino_ import (
    gino_implementation,
    gino_implementation_custom_ids,
    gino_implementation_integrity_errors,
    gino_implementation_string_pk,
)
from .memory import memory_implementation
from .ormar_ import (
    ormar_implementation,
    ormar_implementation_custom_ids,
    ormar_implementation_integrity_errors,
    ormar_implementation_string_pk,
)
from .sqlalchemy_ import (
    sqlalchemy_implementation,
    sqlalchemy_implementation_custom_ids,
    sqlalchemy_implementation_integrity_errors,
    sqlalchemy_implementation_string_pk,
    DSN_LIST,
)
from .tortoise_ import tortoise_implementation

implementations = [
    (memory_implementation, ""),
    (ormar_implementation, ""),
    (gino_implementation, ""),
]

implementations.extend([(sqlalchemy_implementation, dsn) for dsn in DSN_LIST])
implementations.extend([(databases_implementation, dsn) for dsn in DSN_LIST])


if sys.version_info >= (3, 8):
    implementations.append((tortoise_implementation, ""))

```

**code file end: tests/implementations/__init__.py**
-------------------------------------------


### code file start: tests/test_dependencies/test_disable.py 

```python
import pytest

from fastapi_crudrouter.core import CRUDGenerator

from tests.implementations import implementations
from tests.conftest import yield_test_client, label_func
from tests import test_router


URLS = ["/potato", "/carrot"]
AUTH = {"Authorization": "Bearer my_token"}
KEY_WORDS = {f"{r}_route" for r in CRUDGenerator.get_routes()}
DISABLE_KWARGS = {k: False for k in KEY_WORDS}


@pytest.fixture(params=implementations, ids=label_func, scope="class")
def client(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    [app.include_router(router(**s, **DISABLE_KWARGS)) for s in settings]

    yield from yield_test_client(app, impl)


@pytest.fixture(params=implementations, ids=label_func, scope="class")
def delete_all_client(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    [
        app.include_router(router(**s, delete_all_route=False, update_route=False))
        for s in settings
    ]

    yield from yield_test_client(app, impl)


@pytest.mark.parametrize("url", URLS)
def test_route_disable(client, url):
    assert client.get(url).status_code == 404
    assert client.get(url).status_code == 404
    assert client.post(url).status_code == 404

    for id_ in [-1, 1, 0, 14]:
        assert client.get(f"{url}/{id_}").status_code == 404
        assert client.put(f"{url}/{id_}").status_code == 404
        assert client.delete(f"{url}/{id_}").status_code == 404


def test_route_disable_single(delete_all_client):
    url = "/potato"

    assert delete_all_client.delete(url).status_code == 405

    test_router.test_post(delete_all_client, url)
    assert delete_all_client.put(f"{url}/{1}").status_code == 405
    assert delete_all_client.delete(f"{url}/{1}").status_code == 200

```

**code file end: tests/test_dependencies/test_disable.py**
-------------------------------------------


### code file start: tests/test_dependencies/test_per_route.py 

```python
import pytest
from fastapi import Depends, HTTPException

from tests.conftest import yield_test_client
from tests.implementations import implementations

URLS = ["/potato", "/carrot"]
AUTH = {"Authorization": "Bearer my_token"}


class RaisesException:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def __call__(self):
        raise HTTPException(self.status_code)


class NullDependency:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def __call__(self):
        pass


DEPENDS_KWARGS = dict(
    get_all_route=[Depends(NullDependency), Depends(RaisesException(401))],
    get_one_route=[Depends(NullDependency), Depends(RaisesException(402))],
    create_route=[Depends(NullDependency), Depends(RaisesException(403))],
    update_route=[Depends(NullDependency), Depends(RaisesException(404))],
    delete_all_route=[Depends(NullDependency), Depends(RaisesException(405))],
    delete_one_route=[Depends(NullDependency), Depends(RaisesException(406))],
)


@pytest.fixture(params=implementations)
def client(request):
    impl, dsn = request.param

    app, router, settings = impl(db_uri=dsn)
    [app.include_router(router(**s, **DEPENDS_KWARGS)) for s in settings]

    yield from yield_test_client(app, impl)


@pytest.mark.parametrize("url", URLS)
def test_route_disable(client, url):
    item_url = f"{url}/1"
    actions = [
        (client.get, url),
        (client.get, item_url),
        (client.post, url),
        (client.put, item_url),
        (client.delete, url),
        (client.delete, item_url),
    ]

    err_codes = set()
    for method, url in actions:
        print(method, url, err_codes)
        status_code = method(url).status_code

        assert status_code != 200
        assert 400 <= status_code <= 406
        assert status_code not in err_codes

        err_codes.add(status_code)

    assert len(err_codes) == len(actions)

```

**code file end: tests/test_dependencies/test_per_route.py**
-------------------------------------------


### code file start: tests/test_dependencies/test_top_level.py 

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

import pytest

from tests.implementations import implementations
from tests.conftest import yield_test_client

URLS = ["/potato", "/carrot"]
AUTH = {"Authorization": "Bearer my_token"}


@pytest.fixture(params=implementations, scope="class")
def client(request):
    impl, dsn = request.param

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

    def token_auth(token: str = Depends(oauth2_scheme)):
        if not token:
            raise HTTPException(401, "Invalid token")

    app, router, settings = impl(db_uri=dsn)
    [
        app.include_router(router(**s, dependencies=[Depends(token_auth)]))
        for s in settings
    ]

    yield from yield_test_client(app, impl)


@pytest.fixture(params=URLS)
def url(request):
    yield request.param


class TestTopLevelDependencies:
    @staticmethod
    def test_authorization(client, url):
        assert client.get(url, headers=AUTH).status_code == 200
        assert client.post(url, headers=AUTH).status_code != 401
        assert client.delete(url, headers=AUTH).status_code == 200

        for id_ in [-1, 1, 0, 14]:
            assert client.get(f"{url}/{id_}", headers=AUTH).status_code != 401
            assert client.put(f"{url}/{id_}", headers=AUTH).status_code != 401
            assert client.delete(f"{url}/{id_}", headers=AUTH).status_code != 401

    @staticmethod
    def test_authorization_fail(client, url):
        assert client.get(url).status_code == 401
        assert client.get(url).status_code == 401
        assert client.post(url).status_code == 401

        for id_ in [-1, 1, 0, 14]:
            assert client.get(f"{url}/{id_}").status_code == 401
            assert client.put(f"{url}/{id_}").status_code == 401
            assert client.delete(f"{url}/{id_}").status_code == 401

```

**code file end: tests/test_dependencies/test_top_level.py**
-------------------------------------------


### code file start: tests/test_integration/test_backend_not_installed.py 

```python
import pathlib


def test_virtualenv(virtualenv):
    file = pathlib.Path(__file__)
    package = file.parent.parent.parent
    assert (package / "fastapi_crudrouter").exists()

    virtualenv.run(f"pip install -e {package}")
    virtualenv.run(f"python {file}")


if __name__ == "__main__":
    from fastapi_crudrouter import (
        DatabasesCRUDRouter,
        GinoCRUDRouter,
        OrmarCRUDRouter,
        SQLAlchemyCRUDRouter,
        TortoiseCRUDRouter,
    )

    routers = [
        SQLAlchemyCRUDRouter,
        DatabasesCRUDRouter,
        OrmarCRUDRouter,
        TortoiseCRUDRouter,
        GinoCRUDRouter,
    ]

    for crud_router in routers:
        try:
            # noinspection PyTypeChecker
            crud_router(..., ..., ..., ...)
        except AssertionError:
            pass
        except Exception:
            raise AssertionError(
                f"Not checking that all requirements are installed when initializing the {crud_router.__name__}"
            )

```

**code file end: tests/test_integration/test_backend_not_installed.py**
-------------------------------------------


### code file start: tests/test_integration/test_typing.py 

```python
import pathlib

file = pathlib.Path(__file__)
root_dir = file.parent.parent.parent
package_src = root_dir / "fastapi_crudrouter"


def test_py_typed_file_exists():
    assert (package_src / "py.typed").exists()
    assert (package_src / "py.typed").is_file()


def test_virtualenv(virtualenv):
    assert (root_dir).exists()
    assert (root_dir / "setup.py").exists()

    virtualenv.run(f"pip install -e {root_dir}")
    virtualenv.run(f"pip install mypy")
    virtualenv.run(f"mypy {file}")


if __name__ == "__main__":
    from pydantic import BaseModel
    from fastapi import FastAPI

    import fastapi_crudrouter

    class User(BaseModel):
        id: int
        name: str
        email: str

    router = fastapi_crudrouter.MemoryCRUDRouter(schema=User)
    app = FastAPI()
    app.include_router(router)

```

**code file end: tests/test_integration/test_typing.py**
-------------------------------------------


### code file start: tests/test_integration/__init__.py 

```python

```

**code file end: tests/test_integration/__init__.py**
-------------------------------------------

