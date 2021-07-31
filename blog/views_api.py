from django.db.models import query
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from json import JSONEncoder

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__ 


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    
    def post(self, request):
        response={}
        response['status']=500
        response['message']='Something went wrong'
        try:
            data=request.data
            if data.get('username') is None:
                response['message']='key username is not found'
                raise Exception('key username is not found')
            if data.get('password') is None:
                response['message']='key password is not found'
                raise Exception('key password is not found')
            
            check_user=User.objects.filter(username=data.get('username')).first()
            
            if check_user is None:
                response['message']='username is not found'
                raise Exception('username is not found')

            check_obj=authenticate(username=data.get('username'),password=data.get('password'))

            if check_obj:
                login(request,check_obj)
                response['status']=200
                response['message']='welcome'
            else:
                response['message']='invalid password'
                raise Exception('invaild password')

        except Exception as e:
            print(e)
            return Response(response)
        return Response(response)
LoginView=LoginView.as_view()



class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()



    def post(self, request):
        response={}
        response['status']=500
        response['message']='Something went wrong'
        try:
            data=request.data
            if data.get('username') is None:
                response['message']='key username is not found'
                raise Exception('key username is not found')
            if data.get('password') is None:
                response['message']='key password is not found'
                raise Exception('key password is not found')
            if data.get('password')!=data.get('password1'):
                response['message']='password is not match'
                raise Exception('password is not matched')
            
            check_user=User.objects.filter(username=data.get('username')).first()
            if check_user:
                response['message']='username is already taken'
                raise Exception('username is already taken')
            
            check_user=User.objects.filter(email=data.get('email')).first()
            if check_user:
                response['message']='email is already taken'
                raise Exception('email is already taken')

            check_obj=User.objects.create(username=data.get('username'),email=data.get('email'))
            check_obj.set_password(data.get('password'))
            check_obj.is_admin=True
            check_obj.save()
            response['message']='user is created'
            response['status']=200

        except Exception as e:
            print(e)
            return Response(response)
        return Response(response)
RegisterView=RegisterView.as_view()

