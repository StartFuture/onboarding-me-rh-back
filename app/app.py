from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employee import router as router_employee
from app.routes.route_get import route_get as router_get
from app.routes.route_create import route_create as router_create
from app.routes.route_update import route_update as router_update
from app.routes.route_delete import route_delete as router_delete

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
app.include_router(router=router_get)
app.include_router(router=router_create)
app.include_router(router=router_update)
app.include_router(router=router_delete)