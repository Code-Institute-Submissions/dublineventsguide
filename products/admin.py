from django.contrib import admin
from .models import Original, Product, Vote

admin.site.register(Vote)


@admin.register(Original)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'make',
        'model',
        'votes',
    )
    list_filter = (
        'status',
        'make',
        'model',
        'date',
        'votes'
    )
    search_fields = (
        'status',
        'make',
        'model',
        'date'
    )
    actions = ['highlight', 'activate', 'deactivate']

    def highlight(self, request, queryset):
        queryset.update(status='h')

    def activate(self, request, queryset):
        queryset.update(status='a')

    def deactivate(self, request, queryset):
        queryset.update(status='i')


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'in_stock',
        'make',
        'model',
        'date',
        'manufacturer',
        'color'
    )
    list_filter = (
        'status',
        'make',
        'model',
        'date',
        'manufacturer',
        'color'
    )
    search_fields = (
        'status',
        'make',
        'model',
        'date',
        'manufacturer',
        'color'
    )
    actions = ['promote', 'soldout', 'out_of_stock', 'on_sales']

    def promote(self, request, queryset):
        queryset.update(status='p')

    def soldout(self, request, queryset):
        queryset.update(status='s')

    def put_of_stock(self, request, queryset):
        queryset.update(status='o')

    def on_sales(self, request, queryset):
        queryset.update(status='y')
