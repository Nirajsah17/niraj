---
author: nirajkumar
title: FastAPI
description: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
tags: python, fastapi, web, api
---

# FastAPI


FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

FastAPI is a modern Python web framework that leverage the latest Python features to provide you with a simple way to build APIs. It is based on standard Python type hints and is designed to be easy to use and learn. FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts.

## Quick Understanding

- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- **Fast to code**: Increase the speed to develop features by about 200% to 300%. 
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
- **Easy**: Designed to be easy to use and learn. Less time reading docs.
- **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- **Robust**: Get production-ready code. With automatic interactive documentation.
- **Standards-based**: Based on standard Python type hints. It is fully type-checkable.
- **Fully asynchronous**: Supports type hints natively. Performant execution. 
- **Automatic interactive API documentation**: Swagger UI, ReDoc, and OpenAPI.

## Installation

You can install FastAPI using pip:

```bash
pip install fastapi
```

## Hello world

Here is a simple example of a FastAPI application:

<!--codeinclude-->
[hello world](../../src/fastapi/hello.py) 
`hello.py`
<!--/codeinclude-->

```bash
  # To run the app use following command where hello is the name of the file specify port using --port
  uvicorn hello:app --reload --port 8000

```

## URL Path 


<!--codeinclude-->
[url path](../../src/fastapi/path.py)
`url_path.py`
<!--/codeinclude-->



## Query Parameters

<!--codeinclude-->
[URI parameter](../../src/fastapi/query_params.py) 
`params.py`
<!--/codeinclude-->

## Request Body

<!--codeinclude-->
[request body](../../src/fastapi/data_model_validation.py)
`request_body.py`
<!--/codeinclude-->

## FormData and File Uploads

<!--codeinclude-->
[form data](../../src/fastapi/formdata.py)
`form_data.py`
<!--/codeinclude-->

## Authentication

<!--codeinclude-->
[authentication](../../src/fastapi/oauth2.py)
`authentication.py`
<!--/codeinclude-->



