from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

# instanciamos FastAPI
# en Js sería: const app = new FastAPI();
app = FastAPI()

# creamos el Modelo a partir de BaseModel de Pydantic
# En Js sería: Item extends BaseModel {}

class Item(BaseModel):
    text: str = None
    is_done: bool = False

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
def create_items(item: Item):
    # añadimos el item al array
    items.append(item)
    return items

# definimos una ruta con un método GET esta vez si para nuestra API
# response_model es un argumento que se utiliza para indicar el modelo de respuesta que se espera.
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

# definimos una ruta con un método GET por Id
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) :
    # si el item existe lo devolvemos
    if item_id < len(items):
        return items[item_id]
    # si el item no existe lanzamos un error
    else:
        # raise se utiliza para lanzar una excepción de forma explícita en Python.
        # En js sería: throw new Error()
        # f"{}" es un string literal en Python" 
        #En js sería: `${}`
        raise HTTPException(status_code=404, detail= f"Item {item_id} not found")