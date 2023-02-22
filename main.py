from fastapi import FastAPI
#    uvicorn
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),
          name="static")
@app.get("/htmlfile")
def f2():
    return FileResponse("index.html")
# http://127.0.0.1/static/index.html
@app.get("/html", response_class=HTMLResponse)
def f1():
    a="Hi all"
    return f"""
    <html>
    <head>
    <title>${a}</title>
    </head>
    <body><h1>Кчау</h1>
    <img src="...">
    </body>
    </html>
    """

@app.get("/")
def root():
    return {"info": "Some info"}
# http://168.0.0.1:8000/

@app.get("/index")
def root():
    return {"info": "info"}
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# http://168.0.0.1:8000/index
@app.get("/{pk}")
def root(pk:int,st:str = None):
    return {"parametr": pk,"st":st}
# http://168.0.0.1:8000/989?st="abc"
