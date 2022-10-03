from application import *
from application.config.database import meta, engine
from application.controllers import (
    actors,
    categories,
    companies_movies,
    companies,
    countries,
    credit,
    department,
    languages,
    movies_categories,
    movies,
    releases,
    transaction_detail,
    transactions,
    users
)

meta.create_all()

app.include_router(actors.router)
app.include_router(categories.router)
app.include_router(companies_movies.router)
app.include_router(companies.router)
app.include_router(countries.router)
app.include_router(credit.router)
app.include_router(department.router)
app.include_router(languages.router)
app.include_router(movies_categories.router)
app.include_router(movies.router)
app.include_router(releases.router)
app.include_router(transaction_detail.router)
app.include_router(transactions.router)
app.include_router(users.router)
