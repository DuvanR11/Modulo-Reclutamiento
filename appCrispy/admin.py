from django.contrib import admin
from appCrispy.models import Engineer
from appCrispy.forms import EngineerForm
from django.utils.html import format_html

class EngineerAdmin (admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    # form = EngineerForm
    
    # readonly_fields = ['firstname', 'lastname', 'email', 'phone', 'job', 'age','message','birthday','personality',
    #                    'salary','gender','experience','file','image','smoker','situation','created_at',
                       
    #                    'frameworks','languages', 'databases', 'libraries', 'mobile', 'other',
    #                    'university','faculty' ,'institution', 'course' ,'start_course' ,'end_course', 'about_course', 'status_course',
    #                    'company', 'position', 'start_work', 'end_work', 'about_work', 'employed' ,'travel' ,'remote',
    #                    ]
    
    fieldsets= [
        (" Personal Information", {'fields': ['firstname',  'lastname', 'situation', 'email', 'phone',  'job', 'age','message','birthday','personality','salary','gender','smoker','experience','file','image']}),
        (" Skills", {'fields': ['frameworks', 'languages', 'databases', 'libraries', 'mobile', 'other']}),
        (" Educational Information", {'fields': ['university', 'faculty', 'institution', 'course', 'start_course', 'end_course', 'about_course', 'status_course']}),
        (" Work Information", {'fields': ['company', 'position', 'start_work', 'end_work', 'about_work', 'employed', 'travel', 'remote']}),
    ]
    
    list_filter=['situation']
    list_display = ['firstname', 'lastname', 'email', 'message', 'job', 'age','status', '_']
    search_fields = ['firstname', 'lastname', 'email', 'message', 'job', 'situation','age']
    list_per_page = 10
    
    #Functions to change the icons
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    
    def status (self, obj):
        if obj.situation == 'Approved':
            color ='#28a745'
        elif obj.situation == 'Pending':
            color ='#fea95e'
        else:
            color ='red'
        return format_html ('<strong><p style="color: {}">{}</p></strong>'. format(color, obj.situation))
    status.allow_tags = True
        
admin.site.register(Engineer, EngineerAdmin)