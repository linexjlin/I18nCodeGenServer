
from core import Core
from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import tempfile

class UpdateData(BaseModel):
    data: dict

app = FastAPI()

projects = {}

def get_project(id):
    if id in projects:
        return projects[id]
    else:
        pj = Core(id=id)
        projects[id] = pj
        return pj

@app.get("/{id}")
def export(id: str, file: str, notes: str = "", languages: str = "", template: str = ""):
    langs = languages.split(",")
    pj = get_project(id)
    
    suffix = os.path.splitext(file)[1]
    if not suffix:
        raise HTTPException(status_code=400, detail="Unable to detect file type")
    
    pj.set_translate_notes(notes=notes)
    fileContent = pj.export_code_lang(langs,suffix,template)
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
        temp_file.write(fileContent.encode())
        return FileResponse(temp_file.name, filename=file)
    
@app.post("/{id}")
def update_data(id: str, update_data: UpdateData):
    pj = get_project(id)
    pj.update(update_data.data)
    return {"message": "Data updated successfully"}

@app.delete("/{id}/key")
def delete_data(id: str, k: str):
    pj = get_project(id)
    pj.delete(k)
    return {"message": f"Key '{k}' deleted successfully"}

@app.put("/{id}/key")
def add_data(id: str, k: str):
    pj = get_project(id)
    pj.add(k)
    return {"message": f"Key '{k}' added successfully"}

@app.put("/{id}/translate")
def add_data(id: str, k: str, l: str, v: str):
    pj = get_project(id)
    ret = pj.add_translate(k,l,v)
    return {"message": f"'{k} '{l}' '{v}' added, with return {ret}"}

@app.get("/{id}/key")
def get_data(id: str, k: str, l: str):
    pj = get_project(id)
    value = pj.get(k, l)
    return {"result":value}

