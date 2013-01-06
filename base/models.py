from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Talent(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50,null=True,blank=True)
    is_premium = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Style(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Format(models.Model):
    name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    talent = models.ManyToManyField('Talent',related_name="formattalent")
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.real_name

class Frequency(models.Model):
    name = models.CharField(max_length=20)
    filename = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Station(models.Model):
    name = models.CharField(max_length=50)
    words = models.IntegerField()
    formats = models.ManyToManyField('Format',related_name='stationformat')
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Slogan(models.Model):
    name = models.CharField(max_length=300)
    words = models.IntegerField()
    formats = models.ManyToManyField('Format',related_name='sloganformat')
    is_promo_only = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Template_type(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class Template(models.Model):
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=80)
    length = models.DecimalField(max_digits=4,decimal_places=2)
    producer = models.ForeignKey('Producer')
    formats = models.ManyToManyField('Format',related_name='templateformat')
    price = models.DecimalField(max_digits=4,decimal_places=2)
    type = models.ForeignKey('Template_type')
    #Slogan Details
    slogan_words = models.IntegerField()
    slogan_cue = models.DecimalField(max_digits=4,decimal_places=2)
    slogan_talents = models.ManyToManyField('Talent',related_name='template_slogantalent')
    slogan_style = models.ForeignKey('Style',related_name='template_sloganstyle')
    #Station Details
    station_words = models.IntegerField()
    station_cue = models.DecimalField(max_digits=4,decimal_places=2)
    station_talents = models.ManyToManyField('Talent',related_name='template_stationtalent')
    station_style = models.ForeignKey('Style',related_name='template_stationstyle')   
    #frequency details
    frequency_cue = models.DecimalField(max_digits=4,decimal_places=2)
    frequency_talents = models.ManyToManyField('Talent',related_name='template_frequencytalent')
    frequency_style = models.ForeignKey('Style',related_name='template_frequencystyle')   
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
class PieceLength(models.Model):
    name = models.CharField(max_length=300)
    length = models.DecimalField(max_digits=4,decimal_places=2)
    

 