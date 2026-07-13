import jdatetime
from django.contrib import admin
from .models import Tazkera, Service
from django.urls import reverse
from django.utils.html import format_html



# admin.site.register(Service)

@admin.register(Tazkera)
class TazkeraAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "father_name",
        "phone",
        "id_type",
        "issue_date_shamsi",
        "print_form",
    )

    search_fields = (
        "full_name",
        "father_name",
        "grandfather_name",
        "phone",
        "id_number",
        "tazkera_id",
    )

    list_filter = (
        "id_type",
        "issue_date",
    )

    ordering = ("-issue_date",)


    @admin.display(description="تاریخ ثبت")
    def issue_date_shamsi(self, obj):
        return jdatetime.date.fromgregorian(date=obj.issue_date).strftime("%Y/%m/%d")
    

    def print_form(self, obj):
        url = reverse("print_tazkera", args=[obj.pk])
        return format_html(
            '<a class="button" target="_blank" href="{}">🖨 چاپ</a>',
            url
        )
    print_form.short_description = "چاپ"


