# PokeApi
## Technical Test - MO

Runtime
`Python 3.8.5`

.env dev environment
`
export SQL_ENGINE=django.db.backends.postgresql 

export SQL_DATABASE=database_dev 
export SQL_USER=postgres 
export SQL_PASSWORD=postgres
export SQL_HOST=db
export SQL_PORT=5432
`

Run!
`docker-compose -f docker-compose.dev.yml up`

The solution loads the evolution-chain 1 by default 

http://localhost:8000/api/pokemon?name=ivysaur

