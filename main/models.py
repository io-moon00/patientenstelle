from django.db import models
# Create your models here.

class Page(models.Model):
    PAGE = [
        ('home', 'Home'),
        ('news', 'News'),
        ('offer', 'Angebot'),
        ('about', 'About'),
        ('membership', 'Mitgliedschaft'),
        ('contact', 'Contact'),
        ('links', 'Links')
    ]
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    page = models.CharField(max_length=10, choices=PAGE, default='home')

    class Meta:
        verbose_name = "Seite"
        verbose_name_plural = "Seiten"
        
    def __str__(self):
        return self.page


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')
    image_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoren"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default='#FFFFFF')

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    lead = models.TextField()
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Blog Eintrag"
        verbose_name_plural = "Blog Einträge"

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    TEAM = [
    ('vorstand', 'Vorstand'),
    ('advice', 'Beratung'),
]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=8, choices=TEAM, default='vorstand')

    class Meta:
        verbose_name = "Team Mitglied"
        verbose_name_plural = "Team Mitglieder"

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    frontpage = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"
    
    def __str__(self):
        return self.title