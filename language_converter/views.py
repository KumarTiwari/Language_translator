from django.shortcuts import render
from googletrans import Translator
from django.http import JsonResponse

def Converter(request):
    if request.method=="POST" and request.is_ajax():
        new_language=request.POST['language']
        data_main=request.POST['data_main']
        trans=Translator()
        req_language=trans.translate(data_main,dest=new_language)
        data={
             'req_language': req_language.text ,
        }
        return JsonResponse(data)
    else:
        return render(request,'converter.html',{})