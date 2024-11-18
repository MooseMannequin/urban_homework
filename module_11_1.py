import requests
from PIL import Image
from PIL import ImageFilter
from io import BytesIO

r = requests.get('https://cdna.artstation.com/p/assets/images/images/051/393/996/large/moosemannequin-eugene-ustyuzhanin-frogonly2.jpg?1657183746')
i = Image.open(BytesIO(r.content))
print(i.format, i.size, i.mode)

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = im1.size[1] + im2.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im2.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
    im.paste(im1.transpose(Image.Transpose.FLIP_TOP_BOTTOM), (im1.size[0], 0))
    im.paste(im2.filter((ImageFilter.CONTOUR)), (1920, 1920))
    im.paste(im1.filter(ImageFilter.EMBOSS), (0, 1920))


    return im.show()

merge(i, i.transpose(Image.Transpose.FLIP_LEFT_RIGHT))