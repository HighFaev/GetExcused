from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
import src.models.model as model
import src.services.huggingface_api as huggingface_api

router = APIRouter()

#Root page
@router.get("/", response_class=HTMLResponse)
async def root():
    return "Hello from getExcused server!"

#Change excuses rank
@router.post("/change-excuse-rank",)
async def change_excuse_rank(text: str, deltaRank = 1):
    model.change_rank(text, deltaRank)

#Get some excuses in sorted order (by rank)
@router.get("/get-excuses", response_class=JSONResponse)
async def get_excuses(numberOfExcuses = 0, needAll: bool = False):
    return model.get_excuses(numberOfExcuses, needAll)

#Get a new joke
@router.get("/generate-joke", response_class=JSONResponse)
async def generate_joke():
    joke = huggingface_api.generate_excuse()
    model.add_excuse(joke)
    return joke