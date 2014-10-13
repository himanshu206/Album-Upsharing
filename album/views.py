from django.shortcuts import render_to_response
from .models import saveRegister
from .models import AlbumPhotos
from .models import AlbumInfo
import json
import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.core import serializers

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


#module to register user

def registerUser(request):
    f_name = request.POST.get('f_name', '')
    l_name = request.POST.get('l_name', '')
    email = request.POST.get('regEmail', '')
    password = request.POST.get('regPasswd', '')
    try:
        check = saveRegister.objects.get(email__icontains=email)
    except saveRegister.DoesNotExist:
        check = None

    response_data = {}
    if check is None:
        b = saveRegister(f_name=f_name, l_name=l_name, email=email, password=password)
        b.save()
        response_data['message'] = 1;
        response_data['username'] = f_name;

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data['message'] = 2
        response_data['email'] = email
        return HttpResponse(json.dumps(response_data), content_type="application/json")

#module for login user

def loginUser(request):

    login_email = request.POST.get('loginEmail', '')
    login_password = request.POST.get('loginPasswd', '')

    try:
        checkLogin = saveRegister.objects.get(email__icontains=login_email, password__contains=login_password)
    except saveRegister.DoesNotExist:
        checkLogin = None

    response_data = {}
    request.session['member_id'] = {}
    if checkLogin is None:
        response_data['message'] = 0;
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        request.session['member_id'] = checkLogin.id
        request.session['firstname'] = checkLogin.f_name
        request.session['lastname'] = checkLogin.l_name
        request.session['email'] = checkLogin.email
        response_data['message'] = 1;
        response_data['User_id'] = checkLogin.id;
        return HttpResponse(json.dumps(response_data), content_type="application/json")

#module for user profile

def profile(request):
    try:
        if request.session['member_id'] is not None:
            user_email = request.session['email']
            first_name = request.session['firstname']
            last_name = request.session['lastname']
            user_data = {'user_email':user_email,'first_name':first_name,'last_name':last_name}
            json_data = json.dumps(user_data)
            return render_to_response('profile.html', {"user_data": json_data})
    except KeyError:
        pass
    return redirect('/')

#module for getting all albums just login
@csrf_exempt
def getAllAlbums(request):
    try:
        if request.session['member_id'] is not None:
            dataStore = {}
            i=0
            allAlbums = AlbumInfo.objects.filter(user_id=request.session['member_id']).order_by('-pk')
            allAlbms = serializers.serialize('json', allAlbums)
            all = json.loads(allAlbms)
            for Album in allAlbums:
                getPhotoData = serializers.serialize('json', AlbumPhotos.objects.filter(albumPhoto_id=Album.id))
                photo_list = json.loads( getPhotoData )
                dataStore[i] = photo_list
                i=i+1

            print(json.dumps({'photo_data':dataStore}))
            return HttpResponse(json.dumps({'album_info':all,'photo_data':dataStore}), content_type='application/json')
    except KeyError:
        pass
    return redirect('/')


#module for saving album info post login
@csrf_exempt
def saveAlbumInfo(request):

    try:
        if request.session['member_id'] is not None:
            album_name = request.POST.get('album_name','')

            date = datetime.date.today()
            saveAlbumInfo = AlbumInfo(albumName=album_name, date=date, user_id=request.session['member_id'])
            saveAlbumInfo.save()
            albumId = AlbumInfo.objects.latest('id')
            empty_album_data = {'album_id':albumId.id, 'album_name':album_name,'album_photos_count':albumId.count, 'album_created_date':str(date)}
            json_data = json.dumps(empty_album_data)
            return HttpResponse(json_data, content_type="application/json")
    except KeyError:
        pass
    return redirect('/')

#module for uploading images
@csrf_exempt
def uploadImages(request):
    try:
        if request.session['member_id'] is not None:
            if request.method == "POST":

                album_Id = request.POST.get('album_Id','')
                files = request.FILES.getlist('file')
                for filename in files:
                    save_image = AlbumPhotos(photo=filename, albumPhoto_id=album_Id)
                    save_image.save()

                data = {'status':'true'}
                return HttpResponse(json.dumps(data), content_type="application/json")

    except KeyError:
        pass
    return redirect('/')


#module for counting photos in current album
@csrf_exempt
def getPhotoCount(request):

        if request.session['member_id'] is not None:
            if request.method == "POST":
                response = {}
                album_Id = request.POST.get('album_Id_1','')
                countPhotos = AlbumPhotos.objects.filter(albumPhoto_id=album_Id).count()
                print("_______",countPhotos)
                response['count'] = countPhotos
                return HttpResponse(json.dumps(response), content_type="application/json")

    #except KeyError:
     #   pass
    #return redirect('/')


#module to logout user

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('/')
