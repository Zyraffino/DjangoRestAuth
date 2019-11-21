from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetView, UserView

arg_list_view = {
    'post': 'create',
    'get': 'list'
}

arg_detail_view = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

snippet_list = SnippetView.as_view(arg_list_view)
snippet_detail = SnippetView.as_view(arg_detail_view)

user_list = UserView.as_view(arg_list_view)
user_detail = UserView.as_view(arg_detail_view)


# URL Patterns
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),

    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
])