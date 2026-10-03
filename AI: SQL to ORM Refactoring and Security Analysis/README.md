# AI: SQL to ORM Refactoring and Security Analysis

## Overview
This task uses an AI assistant (Google Gemini) to refactor a procedural Python script that manages a `users` table through `mysql.connector` and raw SQL strings into an object-oriented version built on the SQLAlchemy ORM. The AI was also asked to explain why the ORM version is more secure and more professional.

## Files
- `initial_raw_sql.py`: the original script. A `get_connection()` helper plus `create_user`, `get_user_by_username`, `update_user_email`, `delete_user` and `list_users`, all written with hand-written SQL strings and `%s` parameterized queries.
- `refactored_orm.py`: the AI-generated SQLAlchemy ORM version. A declarative `User` model, table creation through `Base.metadata.create_all`, and the same five operations rewritten to use an ORM `Session`.

## The prompt
The single prompt required the AI to: define `User` as a declarative model with a unique, non-null username; show table creation, adding a user and querying it through a `Session` with commit and rollback handling; refactor all five original functions; and explain in detail why the ORM is more professional and secure than raw SQL with string formatting.

## How to run
```bash
pip install sqlalchemy
python refactored_orm.py
```
The script uses a local SQLite file so it runs anywhere. To target MySQL, install `mysql-connector-python` and change the engine URL to `mysql+mysqlconnector://root:yourpassword@localhost/example_db`. The model and the CRUD functions stay the same.

## What changed
| Raw SQL version | ORM version |
|---|---|
| SQL lives inside Python strings | The table is a Python class (`User`) |
| Rows come back as tuples (`row[1]`) | Rows come back as `User` objects (`user.email`) |
| Manual cursor and connection handling | A `Session` manages the unit of work |
| Schema created separately with DDL | `Base.metadata.create_all(engine)` builds it from the model |
| Tied to MySQL | Change the engine URL to change database |

## Key takeaways from the AI analysis
- **Injection safety:** the ORM binds parameters on every query, so there is no spot where user input can be concatenated into SQL by mistake.
- **Portability:** the dialect is chosen by the connection URL, so model and queries do not change between databases.
- **Maintainability:** columns and constraints (`unique`, `nullable=False`) are declared once in the model.
- **Transactions:** each write is wrapped in try/except with `session.rollback()` so a failed operation does not leave the session in a broken state.

## Verification
I ran `refactored_orm.py` locally. The table is created, `alice` is inserted and fetched back as a `User` object. Running it a second time shows the unique constraint rejecting the duplicate username and the session rolling back cleanly.

## Notes
- The `email` column is not unique in this version. That is a design choice worth revisiting for a real app.
- `session.query(...)` is the classic Query API. It still works in SQLAlchemy 2.x, though the newer style uses `select()`.
