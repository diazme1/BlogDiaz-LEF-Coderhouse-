import email
from django.shortcuts import redirect, render

#AppBlog forms--->
from appBlog.forms import MakePost_form, LeaveComment_form
#AppBlog models--->
from appBlog.models import Post, Comment
#AppUsers models-->
from appUsers.models import Avatar
#Django login resources--->
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def inicio(request):

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, 'appBlog/index.html', {'user': usuario, 'img':img})

def pages(request):

    postslist = Post.objects.all().order_by('-fecha')

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        usuario = request.user

        if len(avatar) > 0:

            img = avatar[0].imagen.url

        else:

            img = None

    else:

        img = None

        usuario = None

    return render(request, 'appBlog/pages.html', {'postlist':postslist, 'img':img, 'user':usuario})

def abrir_post(request, titulo):

        readPost = Post.objects.get(titulo=titulo)

        try:
            commentsPost = Comment.objects.filter(post=titulo)

            if request.user.username:

                avatar = Avatar.objects.filter(user=request.user)

                if len(avatar) > 0:

                    img = avatar[0].imagen.url
                
                else:

                    img= None
        
            else:

                img = None

        except:

            commentsPost= None

            if request.user.username:

                avatar = Avatar.objects.filter(user=request.user)

                if len(avatar) > 0:

                    img = avatar[0].imagen.url

                else:
                    img=None
            else:
                img=None

        return render(request, 'appBlog/post.html', {'post': readPost, 'img': img, 'comentarios': commentsPost})

@login_required
def makepost(request):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method =='POST':

        miPost = MakePost_form(request.POST)

        if miPost.is_valid():

            content = miPost.cleaned_data

            post = Post(owner=request.user, 
                        autor=content['autor'],
                        email=content['email'], 
                        titulo=content['titulo'], 
                        cuerpo=content['cuerpo'], 
                        subtitulo=content['subtitulo'], 
                        imagen=content['imagen'])

            post.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, 'appBlog/pages.html', {'postlist': postslist, 'img': img})
    
    else:

        miPost = MakePost_form(initial={'owner':request.user, 'email':request.user.email})

    return render(request, 'appBlog/makepost.html', {'miPost': miPost, 'img': img})

@login_required
def leavecomment(request, titulo):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method =='POST':

        miComment = LeaveComment_form(request.POST)

        if miComment.is_valid():

            content = miComment.cleaned_data

            post = Post.objects.filter(titulo=titulo)

            post = post[0].titulo

            comment = Comment(usuario=content['usuario'], body=content['body'], post = post)

            comment.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, 'appBlog/pages.html', {'postlist': postslist, 'img': img})
    
    else:

        post = Post.objects.filter(titulo=titulo)

        post = post[0].titulo

        miComment = LeaveComment_form(initial={'usuario':request.user, 'post':post})

    return render(request, 'appBlog/leavecomment.html', {'miComment': miComment, 'img': img})

def search_post(request):

    data = request.GET.get('titulo', "")
    error = ""

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:

            img = avatar[0].imagen.url
        else:
            img = None
    else:
        img = None

    if data:
        try:

            post = Post.objects.get(titulo=data)

            return render(request, 'appBlog/searchpost.html', {"post": post, "titulo": data, 'img': img})

        except Exception as exc:

            error = "No se han encontrado posts con el título indicado."

    return render(request, 'appBlog/searchpost.html', {"error": error, 'img': img})

@login_required
def deletepost(request, post_titulo):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    try:
        post = Post.objects.get(titulo=post_titulo)
        post.delete()

    except:

        postslist = Post.objects.all().order_by('-fecha')

        return render(request, 'appBlog/index.html', {'postlist': postslist, 'img': img})
    
    else:

        miPost = MakePost_form()

        postslist = Post.objects.all().order_by('-fecha')

        return render(request, 'appBlog/index.html', {'postlist': postslist, 'miPost': miPost, 'img': img})

@login_required
def updatepost(request, post_titulo):

    post = Post.objects.get(titulo=post_titulo)

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:

        img = avatar[0].imagen.url

    else:

        img = None

    if request.method == "POST":

        formulario = MakePost_form(request.POST)
        
        if formulario.is_valid():

            informacion = formulario.cleaned_data

            post.cuerpo = informacion["cuerpo"]
            post.subtitulo = informacion["subtitulo"]
            post.imagen = informacion["imagen"]

            post.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, "appBlog/index.html", {'postlist': postslist, 'img': img})

        else:

            formulario = MakePost_form()

            return render(request, "appBlog/updatepost.html", {"formulario": formulario, "post_titulo":post_titulo, 'img': img, "errors": ['Datos ingresados inválidos.']})

    else:

        formulario = MakePost_form(initial={"titulo": post.titulo, "autor": post.autor, 'cuerpo': post.cuerpo, 'email':post.email, 'owner': post.owner})

        return render(request, "appBlog/updatepost.html", {"formulario": formulario, "post_titulo":post_titulo, 'img': img})

def aboutLEF(request):

    if request.user.username:

        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:

            img = avatar[0].imagen.url
        
        else:

            img = None
    
    else: 

        img = None

    return render(request, 'appBlog/about.html', {'img':img})
    

    
 