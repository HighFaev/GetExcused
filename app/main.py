from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

import uvicorn

import controller
import model
import view

#Start FastAPI app
app = FastAPI()

#Root page
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return await controller.root_controller(request)

@app.post("/change-excuse-rank",)
async def change_excuse_rank(text: str, deltaRank = 1):
    await controller.change_excuse_rank(text, deltaRank)

@app.get("/get-excuses", response_class=JSONResponse)
async def get_excuses(numberOfExcuses = 0, needAll = False):
    return await controller.get_excuses(numberOfExcuses, needAll)    

#Run file if runfile named "main.py"
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)