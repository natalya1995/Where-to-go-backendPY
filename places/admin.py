from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django_summernote.admin import SummernoteModelAdmin
from .models import Place, PlaceImage

class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ('image', 'preview')          
    readonly_fields = ('preview',)

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="height:70px;border-radius:8px"/>', obj.image.url)
        return "—"

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, SummernoteModelAdmin):
    list_display = ('title', 'is_published', 'latitude', 'longitude', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'short_description', 'long_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PlaceImageInline]
    summernote_fields = ('long_description',) 

@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position', 'thumb')
    list_editable = ('position',)

    @admin.display(description="Превью")
    def thumb(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="height:50px;border-radius:6px"/>', obj.image.url)
        return "—"
