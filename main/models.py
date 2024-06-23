from django.db import models
# Create your models here.

class Page(models.Model):
    PAGE = [
        ('home', 'Home'),
        ('about', 'About'),
        ('news', 'News'),
        ('contact', 'Contact'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    page = models.CharField(max_length=8, choices=PAGE, default='home')
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

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default='#FFFFFF')
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    lead = models.TextField()
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/')

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

    def __str__(self):
        return self.name



