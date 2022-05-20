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

Run the db container first!
`docker-compose -f docker-compose.dev.yml up db`
and then the django web container!
`docker-compose -f docker-compose.dev.yml up web`

The solution loads the evolution-chain 1 by default 
So you can see data just by calling the next url in your browser
`http://localhost:8000/api/pokemon?name=ivysaur`

To add more data you may use the container CLI and type
`python manage.py add_pokemons ${id}`

Where `add_pokemons` is the command created for this exercise and
`id` is the id for the evolution-chain to add

