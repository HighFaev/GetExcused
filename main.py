from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.presenters.presenter as controller

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