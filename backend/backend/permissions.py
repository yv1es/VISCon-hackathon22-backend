from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from events.models import BlogPost
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required



user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

def testPermissions(user, model):
    user.has_perm('<app label>.add_model')
    user.has_perm('<app label>.change_model')
    user.has_perm('<app label>.delete_model')
    user.has_perm('<app label>.view_model')

def createPermission(user):
    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
    )
    # somehow add permission to user_permissions

def changeEvent(user, event):
    if user.is_authenticated:
        if user.has_perm('application.change_event'):
            event.name = "changed"

def users_list_view(request):
    request.user.has_perm(...)

@permission_required('auth.view_user')
def users_list_view(request):
    pass

# only superuser can create tags/categories
#  