from app.schema import Query
import strawberry

schema = strawberry.Schema(query=Query)

