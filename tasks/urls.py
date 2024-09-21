from django.urls import path

from tasks.views import (
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    TaskCreateView,
    TaskDetailView, toggle_task_completion, TaskUpdateView, TaskDeleteView,
)

app_name = "tasks"

urlpatterns = [
    # Projects
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path(
        "projects/<slug:slug>/update/",
        ProjectUpdateView.as_view(),
        name="project-update",
    ),
    path(
        "projects/<slug:slug>/delete/",
        ProjectDeleteView.as_view(),
        name="project-delete",
    ),

    # Tasks
    path(
        "tasks/create/<slug:project_slug>/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path("tasks/<slug:slug>", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<slug:slug>/toggle-completion/", toggle_task_completion, name="toggle-completion"),
    path("tasks/<slug:slug>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<slug:slug>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]
