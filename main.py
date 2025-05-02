from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path



import src.controllers.controller as controller

#Start FastAPI app
app = FastAPI()
app.include_router(controller.router)

#Setup CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


#Run file if runfile named "main.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)