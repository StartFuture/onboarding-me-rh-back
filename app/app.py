from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employee import router as router_employee
from app.routes.admin import router as router_admin
from app.routes.company import router as router_company
from app.routes.email import router as router_email


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3306"
    # "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=router_employee)
app.include_router(router=router_admin)
app.include_router(router=router_company)
app.include_router(router=router_email)