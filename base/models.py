from django.db import models
import re

def check_bib_file(file_name):
    BIB_TYPES = ['ARTICLE', 'BOOK']
    #with open(file_name, 'r', encoding='utf-8') as file:
    bdata = file_name.read()
    data = bdata.decode('utf-8')

    entries = [1 if re.search(entry_type, data, re.IGNORECASE) is not None else 0 for entry_type in BIB_TYPES]
    print(entries)
    if sum(entries) != 1:
        raise Exception('Not a proper bibtex file. Please upload a single bibtex (.tex) entry.')
    else:
        entry_type = BIB_TYPES[entries.index(1)]
        #parameters = get_params(entry_type)
    return entry_type

##### PUBLICATIONS ######
class Publication(models.Model):
    #Required Fields
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    year = models.PositiveSmallIntegerField()
    cover_image = models.ImageField(upload_to='images/')
    link_url = models.URLField()
    #Opitional Fields
    month = models.PositiveSmallIntegerField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["year"]

class Article(Publication):
    #Required Fields
    journal_name = models.CharField(max_length=100)
    #Opitional Fields
    journal_abbr = models.CharField(max_length=50, null=True, blank=True)
    doi = models.CharField(max_length=50, null=True, blank=True)
    volume = models.PositiveSmallIntegerField(null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    issue = models.PositiveSmallIntegerField(null=True, blank=True)
    starting_page = models.PositiveSmallIntegerField(null=True, blank=True)
    ending_page = models.PositiveSmallIntegerField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    #keywords

class Banner(Publication):
    #Required Fields
    event_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    #Opitional Fields
    event_abbr = models.CharField(max_length=50, null=True, blank=True)
    presentation_date = models.DateField(null=True, blank=True)
    abstract = models.TextField(max_length=500, null=True, blank=True)
    link_abstract = models.URLField(null=True, blank=True)

class Oraltalks(Publication):
    #Required Fields
    event_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    #Opitional Fields
    event_abbr = models.CharField(max_length=50, null=True, blank=True)
    presentation_date = models.DateField(null=True, blank=True)
    abstract = models.TextField(max_length=500, null=True, blank=True)
    link_abstract = models.URLField(null=True, blank=True)
    link_video = models.URLField(null=True, blank=True)


##### PORTFOLIO ######
class Data_analysis(Publication):
    link_project = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=500)

class Software(Publication):
    link_project = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=500)

class Instrument(Publication):
    link_project = models.URLField()
    link_github = models.URLField()
    description = models.TextField(max_length=500)
