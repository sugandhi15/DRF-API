from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST','PATCH'])
def homepage(request):
    if request.method=="GET":
        return Response({
            'status':200,
            'message':'Yes ! Django rest framework is working...',
            'method':'It is a GET request',
        })
    elif request.method=="POST":
        return Response({
            'status':200,
            'message':'Yes ! Django rest framework is working...',
            'method':'It is a GET request',
        })
    elif request.method=="PATCH":
        return Response({
            'status':200,
            'message':'Yes ! Django rest framework is working...',
            'method':'It is a PATCH request',
        })
    else:
        return Response({
            'status':400,
            'message':'Yes ! Django rest framework is working...',
            'method':'called invalid Method',
        })
    

@api_view(['GET'])
def get_todo(request):
    try:
        data=Todo.objects.all()
        serializer =  TodoSerializer(data,many= True)
        return Response({
            'status':200,
            'data':serializer.data
        })
    except Exception as e:
        return Response({
            'status':500,
            'message':e
        })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data 
        serializer =  TodoSerializer(data = data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status':True,
                'message':'Success Data',
                'data':serializer.data
            })
        
        return Response({
            'status':False,
            'message':'Failed to fetch Data 1',
            'data':serializer.data
        })
    except Exception as e:
        return Response({
            'status':False,
             'message': 'An error occurred: {}'.format(str(e)), 
        })
    

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status' : False,
                'message':'uid is required',
                'data':{}
            })
        
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj , data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':'Success Data',
                'data':serializer.data
            })
        
        return Response({
            'status':False,
            'message':'Failed to fetch Data 1',
            'data':serializer.data
        })
    
    except Exception as e:
        return Response({
            'status':False,
            'message':'Failed to fetch Data 1',
            'data':serializer.data
        })
    

class TodoView(APIView):

    def get(self,request):
        return Response({
            'status':True,
            'msg':'This is a todo list',
            'method-called':'You called a get method'
        })
    
    
    def post(self,request):
        return Response({
            'status':True,
            'msg':'This is a todo list',
            'method-called':'You called post request'
        })
    

    def patch(self,request):
        return Response({
            'status':True,
            'msg':'This is a todo list',
            'method-called':'You called Patch request'
        })
    

    def delete(self,request):
        return Response({
            'status':True,
            'msg':'This is a todo list',
            'method-called':'You called delete request'
        })