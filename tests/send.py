import aiofiles
import base64
from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from sanic.response import json
from sanic_mail import Sanic_Mail
import aiosmtplib
app = Sanic(__name__)
jinja = SanicJinja2(app)
Sanic_Mail.SetConfig(
    app,
    MAIL_SENDER='toantd1202@gmail.com',
    MAIL_SENDER_PASSWORD='pass',
    MAIL_SEND_HOST='smtp.gmail.com',
    MAIL_SEND_PORT='465',
    MAIL_TLS='TLS'
)
sender = Sanic_Mail(app)


@app.get('/send')
async def send(request):
    attachments = {}
    async with aiofiles.open("path/file.txt", "rb") as f:
        attachments["toan.txt"] = await f.read()
    async with aiofiles.open('path/image.jpg', "rb") as f:
        attachments['cười.jpg'] = await f.read()
    await app.send_email(
        targetlist="toantd1202@gmail.com",
        subject="thư nè",
        content="mở ra đi",
        attachments=attachments
    )
    return json({"result": "ok"})
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
