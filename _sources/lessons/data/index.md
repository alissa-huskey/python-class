Data
====

% TODO
% [ ] intro
%     [ ] relational databases
%     [ ] server, client
%     [ ] database, tables, rows, columns
% [ ] SQL
%     [ ] `psql`
%         [ ] invocation: `--help`,  `--file=FILENAME`, `--list`, `-1`, `--command`
%         [ ] create database `createdb`, `dropdb`
%         [ ] create user
%         [ ] create role
%         [ ] create database
%         [ ] connect to database
%         [ ] importing
%     [ ] comments: `-- ...`, `/* ... */`
%     [ ] `CREATE TABLE`, `INSERT`, `SELECT`, `DROP`, `UPDATE`, `ALTER TABLE`
%     [ ] querying
%         [ ] `VALUES`, `AS`, `DISTINCT`
%         [ ] `LIMIT`, `OFFSET`, `ORDER BY`, `DESC`
%         [ ] `JOIN`, `UNION`, `INTERSECT`, `EXCEPT`, subqueries
%         [ ] `WITH`, `HAVING`
%         [ ] `BETWEEN`, `LIKE`, `LIKE`, `ILIKE`, `SIMILAR`
%         [ ] `IS`, `ISNULL`, `NOTNULL`
%         [ ] `NOT`, `AND`, `OR`
%         [ ] `CASE`
%     [ ] inserting and updating: `RETURNING`
%     [ ] CLI: `\h`, `\l`, `\d`, `\d+`, `\dt`, `\du`, `\q`, `\i`, `\x`
%     [ ] primary keys, foreign keys, constraints, triggers
%     [ ] aggregate functions: `max`, `min`, `sum`, `avg`, `count`, `GROUP BY`
%     [ ] transactions: `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`
%     [ ] views
%     [ ] indexes: unique
%     [ ] `current_date`
% [ ] Python connect to database
% [ ] `~/.pgpass`, `~/.psqlrc`
%     [ ] 
% PGDATABASE, PGUSER
% logs:
% /usr/local/var/postgres/server.log
% pgcli: https://www.pgcli.com/

% brew install postgresql
% brew postgresql-upgrade-database
% brew services start postgresql
% rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres -E utf8
% pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
% rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres --locale=C -E UTF-8

Troubleshooting
---------------

Mac

```
FATAL:  database files are incompatible with server
DETAIL:  The data directory was initialized by PostgreSQL version 9.2, which is not compatible with this version 9.0.4.
```

```bash
rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres --locale=C -E UTF-8
```

Reference
---------

### Postgres

* [PostgreSQL.org Tutorial](https://www.postgresql.org/docs/current/tutorial.html)
* [postgresqltutorial.com > Getting Started](https://www.postgresqltutorial.com/postgresql-getting-started/)
* [postgresqltutorial.com > Sample Database](https://www.postgresqltutorial.com/postgresql-sample-database/)
* [psql command line tutorial and cheat sheet](https://tomcam.github.io/postgres/)
* [Beginner's Guide to PostgreSQL](https://www.datacamp.com/community/tutorials/beginners-introduction-postgresql)
* [PostgreSQL tutorial](https://www.codertutor.com/postgresql-tutorial.html)
* [A Getting Started PostgreSQL Tutorial](https://www.sqlservercentral.com/articles/a-getting-started-postgresql-tutorial)

### Python

* [Using PostgreSQL in Python](https://www.datacamp.com/community/tutorials/tutorial-postgresql-python)

### Tools

* [Heroku Postgres](https://devcenter.heroku.com/categories/heroku-postgres)
* [ElephantSQL](https://www.elephantsql.com/)
*
