from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employee import router as router_employee
from app.routes.company import router as router_company
from app.routes.email import router as router_email
from app.routes.welcome_kit import router as router_welcome_kit
from app.routes.welcome_kit_item import router as router_welcome_kit_item
from app.routes.welcome_kit_wk_item import router as router_welcome_kit_wk_item
from app.routes.address import router as router_address
from app.routes.tracking import router as router_tracking


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3306",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=router_employee)
app.include_router(router=router_company)
app.include_router(router=router_email)
app.include_router(router=router_welcome_kit)
app.include_router(router=router_welcome_kit_item)
app.include_router(router=router_welcome_kit_wk_item)
app.include_router(router=router_address)
app.include_router(router=router_tracking)