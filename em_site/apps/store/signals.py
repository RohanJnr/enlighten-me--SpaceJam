import os

from PIL import Image


def delete_book_image(sender, instance, **kwargs):
    image_path = instance.image.path
    os.remove(image_path)


def resize_book_image(sender, instance, **kwargs):
    image_path = instance.image.path
    image = Image.open(image_path)
    output_size = (500, 500)
    image.thumbnail(output_size)
    image.save(image_path)
