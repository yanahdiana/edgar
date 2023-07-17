from django.contrib import admin

from .models import Question, Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5



class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
     #   (None, {"fields": ["question_text"]}),
      #  ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    #]
     inlines = [ChoiceInline]
     list_display = ["question_text", "pub_date", "was_published_recently"]
     list_filter = ["pub_date"] #adds "Filter" sidebar thats lets you filter the change list by the pub_date field.
     search_fields = ["question_text"] # adds a search box at the top of the change list.
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
