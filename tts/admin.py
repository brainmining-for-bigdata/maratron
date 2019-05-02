from django.contrib import admin
from .models import Maratron

# Register your models here.

# admin.site.register(Maratron)

@admin.register(Maratron)
class MaratronAdmin(admin.ModelAdmin):
    list_display = ['index', 'category', 'title', 'name'] # 보여줄 칼럼
    list_display_links = ['index', 'category', 'title', 'name'] # 상세보기 링크 설정
    list_filter = ["index"] # filter 기준 칼럼
    search_fields = ["category", 'name'] # 검색 컬럼