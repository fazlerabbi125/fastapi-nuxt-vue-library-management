Generic single-database configuration.

1. Create migrations directory
```
alembic init migrations
```
2. Generate migration based on db changes
```
alembic revision --autogenerate -m "Initial migration"
```
3. Push migration to db
```
alembic upgrade [head] # head for latest migration
```