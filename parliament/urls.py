from django.urls import path
from .views import (
    ContactsListView,
    ContactsCreateView,
    ContactDetailView,
    UpdatesListView,
    UpdatesCreateView,
    UpdateUpvoteView,
    UpdateDownvoteView,
    UpdateDetailView,
    SuggestionsListView,
    SuggestionsCreateView,
    SuggestionUpvoteView,
    SuggestionDownvoteView,
    SuggestionDetailView,
)

urlpatterns = [
    path("parliamentContact/", ContactsListView.as_view()),
    path("parliamentContact/create/", ContactsCreateView.as_view()),
    path("parliamentContact/<int:pk>/", ContactDetailView.as_view()),
    path("parliamentUpdates/", UpdatesListView.as_view()),
    path("parliamentUpdates/create/", UpdatesCreateView.as_view()),
    path("parliamentUpdates/<int:pk>/", UpdateDetailView.as_view()),
    path("parliamentUpdates/<int:pk>/upvote/", UpdateUpvoteView.as_view()),
    path("parliamentUpdates/<int:pk>/downvote/", UpdateDownvoteView.as_view()),
    path("parliamentSuggestions/", SuggestionsListView.as_view()),
    path("parliamentSuggestions/create/", SuggestionsCreateView.as_view()),
    path("parliamentSuggestions/<int:pk>/", SuggestionDetailView.as_view()),
    path("parliamentSuggestions/<int:pk>/upvote/", SuggestionUpvoteView.as_view()),
    path("parliamentSuggestions/<int:pk>/downvote/", SuggestionDownvoteView.as_view()),
]
