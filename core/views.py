from django.shortcuts import render
from django.http import StreamingHttpResponse
from core.utils.videoReconocer import   generate_frames
from core.utils.videoCapturar import capture_plate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Vista para la página principal
def home(request):
    return render(request, 'home.html')

def reconocedor(request):
    return render(request, 'reconocedor.html')

def captura(request):
    return render(request, 'captura.html')

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def login_view(request):

    if request.method == 'GET':
        return render(request, 'login_2.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario Creado') 
           except:
               return HttpResponse('Usuario ya existe')
           
        return HttpResponse('Password no coincide') 
    

# Vista para el feed de video
def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_capture(request):
    return StreamingHttpResponse(capture_plate(), content_type='multipart/x-mixed-replace; boundary=frame')