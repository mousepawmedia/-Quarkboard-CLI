# Development Guide

## Setup

We **strongly** advise using Linux, macOS, or Windows Subsystem for Linux. All
instructions herein will assume you've done so; if you are using Windows anyway,
you will need to adapt commands to your system.

We use Python 3.11, so you will need to install that. On Ubuntu 22.04, you can install that via the following:

```bash
sudo apt install -y python3.11 python3.11-venv
```

Then, run the following (under Mac/Linux):

```bash
python3.11 -m venv venv
venv/bin/pip install .[dev]
```

Please enable the commit hooks to help ensure code quality:

```bash
git config --local core.hooksPath .githooks/