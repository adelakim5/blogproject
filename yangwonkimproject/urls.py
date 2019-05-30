
from django.contrib import admin
from django.urls import path
import food.views as post
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post.home, name='home'),
    path("create/", post.create, name="create"),
    path("read/<int:post_id>/", post.read, name="read"),
    path("food/<int:post_id>/update/", post.update, name="update" ),
    path("food/<int:post_id>/renew/", post.renew, name="renew"),
    path("food/<int:post_id>/delete", post.delete, name="delete"),
    path("list/", post.list, name="list"),
    path("write/", post.write, name="write"),
    path("<int:post_id>/comment/create", post.create_c, name="comment"),
    path("accounts/signup/", accounts.signup, name="signup"),
    path("accounts/login/", accounts.login, name="login"),
    path("accounts/logout/", accounts.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
