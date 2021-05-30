<p align="center">
  <img src="https://i.imgur.com/s9Gvwsg.png">
</p>

[![Tacklebox](https://img.shields.io/badge/tacklebox-case%20study-blue)](https://tacklebox-webhooks.github.io)

## Overview

These are the instructions to install and use the Python client library for Tacklebox.
Tacklebox is an open-source serverless framework that offers webhooks as a service.

It includes:
- a [CLI tool](https://github.com/tacklebox-webhooks/cli) to deploy and manage AWS infrastructure
- 4 client libraries ([JavaScript](https://github.com/tacklebox-webhooks/javascript),
    [Ruby](https://github.com/tacklebox-webhooks/ruby),
    [Python](https://github.com/tacklebox-webhooks/python),
    and [Go](https://github.com/tacklebox-webhooks/golang))
- a RESTful API with docs
- a management UI

You can read more about our case study [here](https://tacklebox-webhooks.github.io"),
and you can also watch our presentation [here](https://www.youtube.com/watch?v=QEFFlWNNwk8&t=1s).

## The Team

**Juan Palma** *Software Engineer* Phoenix, AZ

**Kevin Counihan** *Software Engineer* Seattle, WA

**Armando Mota** *Software Engineer* Los Angeles, CA

**Kayl Thomas** *Software Engineer* Atlanta, GA

## Getting Started

### Install the Python library

To install the Python library for Tacklebox, run:

```bash
pip install tacklebox-webhooks
```

### Use the Python library

Once you install the Python library for Tacklebox, you can start using it like so:

```python
from tacklebox_webhooks import Tacklebox

# Initialize a Tacklebox object using the API Key and API Host
# obtained after running 'tacklebox deploy'
tacklebox = Tacklebox(API_KEY, API_HOST)
```

Once you include the package and initialize a Tacklebox object, you can do
many things. For example, you can create a service like so:

```python
tacklebox.service.create({ "name": "service1" })
```

Once you create services, event types, users and subscriptions,
you can create a new event like so:

```python
service_id = "d90af763-5839-4a90-834c-5512980984f5"
user_id = "cabea1b5-b485-41b7-8146-72ece22dc458"

event_data = {
    "event_type": "greet",
    "payload": {
        "message": "Hello from the Python wrapper!"
    },
    "idempotency_key": "1"
}

tacklebox.event.create(service_id, user_id, event_data)
```

If you want to see the message log for a specific user and service:

```python
service_id = "d90af763-5839-4a90-834c-5512980984f5"
user_id = "cabea1b5-b485-41b7-8146-72ece22dc458"

tacklebox.message.list(service_id, user_id)
```
