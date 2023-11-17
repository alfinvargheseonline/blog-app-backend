import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from blog_app_backend.serializer import PostSerializer,BlogSerializer
from  blog_app_backend.models import PostModel,SignupModel
from django.db.models import Q
# Create your views here.
@csrf_exempt
def ViewAll(request):
    if request.method=='POST':
        postList=PostModel.objects.all()
        serialize_data=PostSerializer(postList,many=True)
        
        return HttpResponse(json.dumps(serialize_data.data))
    
@csrf_exempt
def AddPost(request):
    if request.method=='POST':
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=PostSerializer(data=recieved_data)
        if serializer_check.is_valid():
           serializer_check.save()
        
           return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"FAILD"}))



@csrf_exempt
def searchView(request):
    if request.method=="POST":
        recived_data=json.loads(request.body)
        getname=recived_data["title"]
        data=list(PostModel.objects.filter(Q(title__icontains=getname)).values())
        return HttpResponse(json.dumps(data))

@csrf_exempt  
def deleteView(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({
            "status":"Post Delete"
        }))
    


@csrf_exempt      
def Signup(request):
    if request.method=='POST':
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=BlogSerializer(data=recieved_data)
        if serializer_check.is_valid():
           serializer_check.save()
        
           return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"FAILD"}))