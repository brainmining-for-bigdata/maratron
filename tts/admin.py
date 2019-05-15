from django.contrib import admin
from .models import Maratron

# Register your models here.

# admin.site.register(Maratron)

@admin.register(Maratron)
class MaratronAdmin(admin.ModelAdmin):
    list_display = ['index', 'category', 'title', 'author'] # 보여줄 칼럼
    list_display_links = ['index', 'category', 'title', 'author'] # 상세보기 링크 설정
    list_filter = ["index"] # filter 기준 칼럼
    search_fields = ["category", 'author'] # 검색 컬럼