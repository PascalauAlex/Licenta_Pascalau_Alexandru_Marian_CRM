from django.contrib import admin
from lead.models import Lead, LostReason
# Register your models here.


admin.site.register(Lead)

@admin.register(LostReason)
class LostReasonAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_active','display_order')
    list_filter = ('category','is_active')
    search_fields = ('name','description')
    list_editable = ('is_active','display_order')
    prepopulated_fields = {'slug':('name',)}
    readonly_fields = ('created_at',)


    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request,obj,form,change)





