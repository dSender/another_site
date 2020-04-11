from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .views import CreateUser, PostList, logout_, AccountSettings, CreatePostView


urlpatterns = [
    path('reglog/', CreateUser.as_view()),
    path('', PostList.as_view()),
    path('confirm/', TemplateView.as_view(template_name='email_confirm.html')),
    path('logout/', logout_),
    path('accountsettings/', AccountSettings.as_view()),
    path('post-create/', CreatePostView.as_view())
]


