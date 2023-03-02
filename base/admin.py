from django.contrib import admin

# Register your models here.
from .models import Article, Banner, Oraltalks
from .models import Data_analysis, Software, Instrument
from .models import check_bib_file
from django.http import HttpResponseRedirect

class ArticleAdmin(admin.ModelAdmin):
    save_on_top = True
    change_form_template = 'admin/custom_change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if "_process-bibtex" in request.POST:
            data = check_bib_file(request.FILES['_import-bibtex'])
            request = self.custom_action(request, data)
            print(request.POST['title'])
            #print(obj.id)
            #self.change_view(request, str(obj.id))
            return HttpResponseRedirect('.')

        return super(ArticleAdmin, self).change_view(request, object_id, form_url, extra_context)

    def custom_action(self, request, data):
        new_POST = request.POST.copy()
        new_POST['title'] = data
        request.POST = new_POST

        return request
    
    custom_action.allow_tags = True

admin.site.register(Article, ArticleAdmin)
admin.site.register(Banner)
admin.site.register(Oraltalks)

admin.site.register(Data_analysis)
admin.site.register(Software)
admin.site.register(Instrument)