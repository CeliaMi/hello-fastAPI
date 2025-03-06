from fastapi import FastAPI

# instanciamos FastAPI
# en Js sería: const app = new FastAPI();
app = FastAPI()

# definimos una ruta
# estamos usando el decorador @app.get("/") para asociar la función read_root() con la ruta /.
# los decoradores es que son funciones que envuelven otras funciones
# en Js sería: app.get("/", (req, res) => res.send({ Hello: "World" }));
@app.get("/")
def read_root():
    return {"Hello": "World"}