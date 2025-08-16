# Fast API project setup and tutorial

Generic single-database configuration.

1. Create migrations directory
```
alembic init [name of directory containing migrations]
```
2. Generate migration based on db changes
```
alembic revision --autogenerate -m <message within "">
```
3. Push migration to db
```
alembic upgrade [head/revision_id] # head for latest migration or revision ID from migration file
```
For downgrade, you can use: `alembic downgrade -1`