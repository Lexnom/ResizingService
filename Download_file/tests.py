from django.test import TestCase,Client
from Download_file.func import resizing

class Size(TestCase):

    def InvalidID(self):
        c = Client()
        response = c.post('/api/23211')
        print(response.status_code)

    def CorrectResizing(self):
        file = 'anime_anime_girls_splatter_mask_gas_masks_paint_splatter-1466561.jpgd.png'
        self.assertEqual(resizing(file,30,30), (20, 20))
