import datetime
import logging
from django.shortcuts import render, redirect
from Download_file.models import Image_resize
from rest_framework.response import Response
from rest_framework.views import APIView
from Download_file.serializers import ImageSerializer

logger = logging.getLogger('log')

def mainSite(request):
    return render(request, 'Main/main.html')

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['photo']
        width, height = request.POST['width'], request.POST['height']
        print(file, width, height)
        a = Image_resize(width=int(width), height=int(height), file=file)
        a1 = a.save()
        a2 = Image_resize.objects.filter(file=a1).first()
        if a2:
            id = a2.id
            info = {'info':'Идетификационный код: %s'%id,
                    'primer':'Что бы узнать состояние запроса введите:',
                    'link':' http://127.0.0.1:8000/api/%s'%id}
        else:
            logger.error('%s: %s' % (datetime.date.today(), 'Неверный идентификатор'))
            return redirect('../')
        return  render(request,'Main/info.html', context=info)

def rdrct(request):
    return redirect('../')

class ImageView(APIView):
    def get(self, request, pk):
        image = Image_resize.objects.filter(id=pk)
        if image:
            serializer = ImageSerializer(image, many=True)
            logger.info('%s: %s' % (datetime.date.today(), 'REST успешно создан'))
            return Response({'result': serializer.data})
        else:
            return render(request,'Main/errorid.html')