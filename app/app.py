from app.routes.employee import router as router_employee
from app.routes.routes import router as router_routes
from app.routes.route_get import route_get as router_get
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
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
app.include_router(router=router_routes)
app.include_router(router=router_get)