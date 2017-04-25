from django.conf.urls import url

from screens import views

urlpatterns = [
    url(r"^$", views.index,
        name="index"),
    url(r"^create$", views.create,
        name="create"),
    url(r"^update$", views.update,
        name="update"),
    url(r"^updateLayout", views.update_layout,
        name="update_layout"),
    url(r"^delete/(?P<screen_id>[0-9]+)/$", views.delete,
        name="delete"),
    url(r"^edit/(?P<screen_id>[0-9]+)/$", views.edit,
        name="edit"),
    url(r"^(?P<screen_id>[0-9]+)$", views.detail,
        name="detail"),
    url(r"^new$", views.new,
        name="new"),
    url(r"^load_widget_config$", views.load_widget_config,
        name="load_widget_config"),
    url(r"^load_widget$", views.load_widget,
        name="load_widget"),
    url(r"^createWidgetData$", views.create_widget_data,
        name="create_widget_data"),
    url(r"^updateWidgetData$", views.update_widget_data,
        name="update_widget_data"),
    url(r"^getWidgetData$", views.get_widget_data,
        name="get_widget_data"),
    url(r"^listWidgetData$", views.list_widget_data,
        name="list_widget_data"),
    url(r"^deleteWidgetData$", views.delete_widget_data,
        name="delete_widget_data"),
]
