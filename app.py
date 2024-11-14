from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
import uvicorn
from resolvers import resolve_welcome, resolve_libroID, resolve_libro_autor, resolve_libro_genero, resolve_ListaLibros

type_defs = load_schema_from_path("esquema.graphql")

query = QueryType()

query.set_field("welcome", resolve_welcome)
query.set_field("libro_ID",resolve_libroID)
query.set_field("libro_autor", resolve_libro_autor)
query.set_field("libro_genero", resolve_libro_genero)
query.set_field("ListarLibros", resolve_ListaLibros)

#esquema ejecutable
esquema = make_executable_schema(type_defs, query)

app = GraphQL(esquema)

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
