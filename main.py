from fastapi import FastAPI

# instanciamos FastAPI
# en Js sería: const app = new FastAPI();
app = FastAPI()

# definimos una ruta para le método GET
# estamos usando el decorador @app.get("/") para asociar la función read_root() con la ruta /.
# los decoradores son como funciones que envuelven otras funciones
# en Js sería: app.get("/", (req, res) => res.send({ Hello: "World" }));

@app.get("/")
def read_root():
    return {"Hello": "World"}

# vamos a crear un array vacio para poder tener algún sitio donde postear algo ya que aún no tenemos la base de datos
items = [] 

# definimos una ruta con un método POST
@app.post("/items")
def create_items(item: str):
    # añadimos el item al array
    items.append(item)
    return items

# definimos una ruta con un método GET por Id
@app.get("/items/{item_id}")
def read_item(item_id: int) -> str:
    return items[item_id]