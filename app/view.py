from fastapi.templating import Jinja2Templates
from fastapi import Request

#For working with templates
templates = Jinja2Templates(directory="../templates")

def render_home_page(request: Request):
    return templates.TemplateResponse("HelloPage.html", {"request": request})
