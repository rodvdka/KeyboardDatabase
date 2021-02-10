import base64
from PIL import Image
from io import BytesIO

def to_img64(file):
    #Create image and resize to smaller size if over the threshold
    image = Image.open(file)
    if image.size[0] > 200 and image.size[1] > 200:
        image.thumbnail((200, 200), Image.ANTIALIAS)

    #Create memory buffer to store the image binary data
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)

    #Convery bytes to base64
    img64 = base64.b64encode(buf.read())
    return img64.decode("ascii")