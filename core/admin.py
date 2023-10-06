from django.contrib import admin
from .models import QuizCategory,QuizQuestions,UserSubmitAnswer,CertifiedAlready
from .models import UserTotalScore

class UserSubmittedAdmin(admin.ModelAdmin):
    list_display=('id','right_answer','question','user','category')

class UserTotalScoreAdmin(admin.ModelAdmin):
    list_display=('user','Score','percentage','Total')

admin.site.register(QuizCategory)
admin.site.register(QuizQuestions)
admin.site.register(UserSubmitAnswer,UserSubmittedAdmin)
admin.site.register(UserTotalScore,UserTotalScoreAdmin)
admin.site.register(CertifiedAlready)

# Register your models here.
