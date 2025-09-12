# Fast API project setup and tutorial

## Using Alembic for migrations

1. Create migrations directory
```
alembic init [name of directory containing migrations] # general template
alembic init -t async [name of directory containing migrations] # for async support
```
2. Configure .mako and env.py files with necessary imports and other setups
3. Generate migration based on db changes
```
alembic revision --autogenerate -m <message within "">
```
4. Fix any migration file issues and push migration to db
```
alembic upgrade [head/revision_id] # head for latest migration or revision ID from migration file
```
For downgrade, you can use: `alembic downgrade -1`