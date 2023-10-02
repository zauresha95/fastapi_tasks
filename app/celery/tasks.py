import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
#from app.logger import logger
from app.celery.celery import celery_app
# from app.tasks.email_templates import create_booking_confirmation_template


@celery_app.task
def process_pic(
    path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    for width, height in [
        (1000, 500),
        (200, 100)
    ]:
        resized_img = im.resize(size=(width, height))
        resized_img.save(f"app/static/images/resized_{width}_{height}_{im_path.name}")

