from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getmethod():
    return {"status":True,"message":"Hey"}