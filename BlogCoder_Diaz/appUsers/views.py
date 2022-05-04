from django.shortcuts import render, redirect

#appUsers imports-->
from appUsers.models import Avatar, UserAbout, Chat
from appUsers.forms import UserRegister_form, UserEdit_form, AboutUser_form, Avatar_form, Chat_form, ChangePassword_form

#django.contrib.auth imports-->
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Users views-->

def login_request(request):

    if request.method == "POST":

        loginform = AuthenticationForm(request, data=request.POST)

        if loginform.is_valid():
            data = loginform.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)

                avatar = Avatar.objects.filter(user=request.user)
                if len(avatar) > 0:
                    img = avatar[0].imagen.url

                else:

                    img = None

                return render(request, 'appBlog/index.html', {'user': usuario, 'img':img})

            else:
                return render(request, 'appUsers/login.html', {"errors": ['El usuario no existe.']})

        else:

            loginform= AuthenticationForm()
            return render(request, 'appUsers/login.html', {"loginform": loginform, "errors": ['Usuario o contraseña incorrectos']})

    else:
        
        loginform = AuthenticationForm()

        return render(request, 'appUsers/login.html', {"loginform": loginform})

def register_request(request):
    
    if request.method == "POST":

        registerform = UserRegister_form(request.POST)

        if registerform.is_valid():

            registerform.save()
            user = registerform.cleaned_data.get("username")

            return redirect('Login')

        else:

            registerform= UserRegister_form()
            return render(request, 'appUsers/register.html', {"registerform": registerform, "errors": ['Datos de registro inválidos.']})

    else:

        registerform = UserRegister_form()
        return render(request, 'appUsers/register.html', {"registerform": registerform})

@login_required
def edituser_request(request):

    usuario = request.user

    avatar = Avatar.objects.filter(user=usuario)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img= None

    if request.method == 'POST':
         
        edituserform = UserEdit_form(request.POST)
        aboutuserform = AboutUser_form(request.POST)

        if edituserform.is_valid() and aboutuserform.is_valid():

            data = edituserform.cleaned_data

            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()

            usuario_k = UserAbout.objects.filter(user=usuario)
            data1 = aboutuserform.cleaned_data

            if len(usuario_k) > 0:

                usuario_k = usuario_k[0]

                usuario_k.bio = data1['bio']
                usuario_k.instagram = data1['instagram']
                usuario_k.facebook = data1['facebook']
                usuario_k.twitter = data1['twitter']

                usuario_k.save()

            else:

                usuario_k = UserAbout(user= usuario, bio=data1['bio'], instagram=data1['instagram'], facebook=data1['facebook'], twitter=data1['twitter'])
                usuario_k.save()

            return redirect('inicio')

        else:

            edituserform = UserEdit_form()
            aboutuserform = AboutUser_form()

            return render(request, 'appUsers/edituser.html', {"edituserform": edituserform, "aboutuserform":aboutuserform, "errors": ['Datos ingresados inválidos.'], 'img':img})

    else: 

        edituserform = UserEdit_form(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        aboutuserform = AboutUser_form()

        return render(request, 'appUsers/edituser.html', {"aboutuserform":aboutuserform, "edituserform": edituserform, 'img':img})

@login_required
def add_avatar(request):

    if request.method == 'POST':

        miAvatar = Avatar_form(request.POST, request.FILES)

        if miAvatar.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            file = miAvatar.cleaned_data

            if len(avatar) > 0:

                avatar = avatar[0]
                avatar.imagen = file['img']
                avatar.save()

                avatar = Avatar.objects.filter(user=request.user)

                img = avatar[0].imagen.url

            else:

                avatar = Avatar(user=usuario, imagen=miAvatar.cleaned_data['img'])
                avatar.save()

                img = None

        return render(request, 'appBlog/index.html', {'img':img})

    else:

        miAvatar = Avatar_form()

        img = None
        
        return render(request, 'appUsers/addavatar.html', {'miAvatar': miAvatar, 'img': img})

@login_required
def open_profile(request):
    
    user = request.user

    avatar = Avatar.objects.filter(user=request.user)

    aboutuser = UserAbout.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

        if len(aboutuser) > 0:
            bio = aboutuser[0].bio
            instagram = aboutuser[0].instagram
            facebook = aboutuser[0].facebook
            twitter = aboutuser[0].twitter

        else:
    
            bio = 'Información no disponible aún.'
            instagram = None
            facebook = None
            twitter = None

    else:

        img = None

        bio = 'Información no disponible aún.'
        instagram = None
        facebook = None
        twitter = None

    return render(request, 'appUsers/profile.html', {'user':user, 'imgprofile':img, 'img': img, 'bio':bio, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter})

def open_user_profile(request, usuario):

    user = User.objects.get(username=usuario)

    usuario1= user.id

    avatar = Avatar.objects.filter(user=usuario1)

    aboutuser = UserAbout.objects.filter(user=usuario1)

    if len(avatar) > 0:

        imgprofile = avatar[0].imagen.url

        if len(aboutuser) > 0:
            bio = aboutuser[0].bio
            instagram = aboutuser[0].instagram
            facebook = aboutuser[0].facebook
            twitter = aboutuser[0].twitter

        else:
    
            bio = 'Información no disponible aún.'
            instagram = None
            facebook = None
            twitter = None

    else:

        imgprofile = None

        bio = 'Información no disponible aún.'
        instagram = None
        facebook = None
        twitter = None

    if request.user.username:

        avatar1 = Avatar.objects.filter(user=request.user)

        if len(avatar1) > 0:

            img = avatar1[0].imagen.url

        else:

            img = None
    
    else:

        img = None

    return render(request, 'appUsers/profile.html', {'img': img, 'user': user, 'imgprofile': imgprofile, 'bio':bio, 'instagram':instagram, 'facebook':facebook, 'twitter':twitter})

@login_required
def chatting(request, usuario):

    receiver = User.objects.get(username=usuario)

    avatar = Avatar.objects.filter(user=request.user)

    messages = Chat.objects.all()

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method == 'POST':

        miMessage = Chat_form(request.POST)

        if miMessage.is_valid():

            message = Chat(writer=request.user, body=miMessage.cleaned_data['body'], recipient=receiver)

            message.save()

            miMessage = Chat_form()

            return render(request, 'appUsers/chat.html', {'img': img, 'user':request.user, 'receiver': receiver, 'messages':messages, 'miMessage': miMessage})

    else:

        miMessage = Chat_form()

    return render(request, 'appUsers/chat.html', {'img': img, 'user':request.user, 'receiver': receiver, 'messages':messages, 'miMessage': miMessage})

@login_required
def open_inbox(request):

    activechats = Chat.objects.all()

    listchats = []

    for chat in activechats:

        if chat.recipient != request.user or chat.recipient == request.user:


            if chat.recipient == request.user and chat.writer not in listchats:

                listchats.append(chat.writer)
            
            elif chat.recipient != request.user and chat.recipient.username not in listchats:

                listchats.append(chat.recipient.username)


    return render(request, 'appUsers/inbox.html', {'listchats':listchats, 'activechats':activechats})

