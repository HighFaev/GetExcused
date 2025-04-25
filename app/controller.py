from fastapi import Request
import model
import view

async def root_controller(request: Request):
    return view.render_home_page(request)

async def change_excuse_rank(text: str):
    model.change_rank(text, 1)