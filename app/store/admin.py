from django.contrib import admin

from .models import Discarts, Notifications, TrashStations


class DiscartsInline(admin.StackedInline):
    model = Discarts
    extra = 0
    fields = (
        "user",
        "quantity"
    )


class NotificationsInline(admin.StackedInline):
    model = Notifications
    extra = 0
    readonly_fields = (
        "checker",
        "status"
    )


@admin.register(TrashStations)
class TrashStationsAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "deleted_at"]
    search_fields = ["title",]
    list_filter = ["created_at", "updated_at", "deleted_at"]
    fieldsets = [
        (
            "",
            {
                "fields": [
                    "title",
                ]
            },
        ),
        (
            "Datas",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "deleted_at"
                ]
            },
        )
    ]
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    inlines = [DiscartsInline, NotificationsInline]


@admin.register(Discarts)
class DiscartsAdmin(admin.ModelAdmin):
    list_display = ["station", "user", "quantity"]
    search_fields = ["station__title",]
    list_filter = ["created_at", "updated_at", "deleted_at"]
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    fieldsets = [
        (
            "",
            {
                "fields": [
                    "station",
                    "user",
                    "quantity",
                ]
            },
        ),
        (
            "Datas",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "deleted_at"
                ]
            },
        )
    ]


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ["station", "checker", "status"]
    search_fields = ["station__title",]
    list_filter = ["status", "created_at", "updated_at", "deleted_at"]
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    fieldsets = [
        (
            "",
            {
                "fields": [
                    "station",
                    "checker",
                    "status",
                ]
            },
        ),
        (
            "Datas",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "deleted_at"
                ]
            },
        )
    ]
