from PIL import Image

from ResizeService import settings


def resizing(file, width, height):
    original_image = Image.open('%s/%s' % (settings.MEDIA_ROOT, file))
    resizing_image = original_image.resize((width, height))
    resizing_image.save('%s/%s' % (settings.MEDIA_ROOT, file))
    return original_image.size