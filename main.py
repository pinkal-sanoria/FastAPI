from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World Pinkal here"}

@app.get("/about")
def about():
    return {'data':{'about page'}}