import datetime
import logging
from Download_file.func import resizing
from django.db import models
from  ResizeService import settings
# Create your models here.

logger = logging.getLogger('log')

class Image_resize(models.Model):
    file = models.ImageField()
    height = models.IntegerField()
    width = models.IntegerField()
    oldSize = models.CharField(max_length=12, null=0)


    def save(self):
        super(Image_resize, self).save()
        size =  resizing(self.file, self.width, self.height)
        self.oldSize = size
        super(Image_resize, self).save()
        logger.info('%s: %s' % (datetime.date.today(), 'Успешно сохранено'))
        return self.file
        