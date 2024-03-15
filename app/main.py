import os

import shutil

import time
from typing import Union

import json

from anyio import Path

from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from fastapi import FastAPI, Request, File, UploadFile

from typing import Annotated

from db import Db_start

from a_image import Image_start


app = FastAPI()

base_dir = os.path.dirname(os.path.abspath(__file__))

# app.mount("/upload/", StaticFiles(directory="upload/"), name="upload")

# app.mount("/", StaticFiles(directory="upload"), name="upload")
# app.mount("/", StaticFiles(directory="new_img"), name="new_img")


db_object = Db_start({ 'id', 1})
img_object = Image_start()

class Task(BaseModel):
    name: str
    # description: Optional[str] = none

@app.get("/")
async def read_root():

    return {"data": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
@app.get("/import_put/{import_put}")
async def import_put(import_put: int, q: Union[str, None] = None):
    return {"import_put": import_put, "q": q}


#*** product ***
@app.get("/products")
async def order(q: Union[str, None] = None):
    return {"q": q}

@app.post("/product/update/{id}")
async def order(id: int, q: Union[str, None] = None):
    return {"id": id, "q": q}
 
@app.get("/product/remove/{id}")
async def order(id: int, q: Union[str, None] = None):
    return {"id": id, "q": q}
    
@app.post("/product/create")
async def order(q: Union[str, None] = None):
    return {"q": 'product create'}
    
@app.get("/product/view/{id}")
async def order(id: int, q: Union[str, None] = None):
    return {"id": id, "q": q}
    
@app.get("/files/")
async def list_files():
    
    data = {}
    
    dir_file = os.path.join(os.path.dirname(__file__), 'upload')
    files = os.listdir(path=dir_file)
    new_str = ', '.join(files)
    return {"files": files }


@app.post("/upload/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    status = False
    dir_file = os.path.join(os.path.dirname(__file__), 'upload')
    save_file = os.path.join(dir_file, file.filename)
    
    with open(save_file, "wb") as f:
        shutil.copyfileobj(file.file, f)
        img_object.image_edit(save_file)
        status = True
    
    
    
    host = request.client.host
    
    port = str(request.client.port)

    return { "filename":host+':'+port+"/upload/"+file.filename, "new_filename":host+':'+port+"/new_img/"+file.filename, "upload_status":status }


@app.post("/remove_file/")
async def order(file_name: Union[str, None] = None):
    
    file = db_object.mainfile(file_name, 'upload')
    
    if os.path.isfile(file):
        os.remove(file)
        q = "done"
    else:
        q = "file not found"    
    
    return {"file": file_name, "status": q}