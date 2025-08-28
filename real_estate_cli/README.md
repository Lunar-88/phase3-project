
# Real Estate CLI

A Python CLI project for managing **properties, clients, and transactions** using SQLAlchemy ORM and Click.

## Features
- Manage properties (add, list).
- Manage clients (add, list).
- Record transactions (sales, rentals).
- Automatic property status updates (Available → Sold/Rented).

## Tech Stack
- Python 3.11
- SQLAlchemy (ORM)
- Alembic (migrations)
- Click (CLI framework)
- SQLite (database)

## Setup
```bash
pipenv install
pipenv shell
alembic init alembic
python seed.py
