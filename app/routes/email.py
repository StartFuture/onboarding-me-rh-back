from fastapi import APIRouter, BackgroundTasks
from app.schemas import email as schemas_email
from app.dao import dao_email as daoEmail
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType


router = APIRouter(
    prefix="/email",
    tags=[
        "email"
    ]
)

@router.post("/email")
async def simple_send(email: schemas_email.EmailSchema) -> JSONResponse:
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(daoEmail.conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

@router.post("/emailbackground")
async def send_in_background(
    background_tasks: BackgroundTasks,
    email: schemas_email.EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.dict().get("email"),
        body="Simple background task",
        subtype=MessageType.plain)

    fm = FastMail(daoEmail.conf)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})