from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Quote(models.Model):
    quote_text = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = str(author)

    def __str__(self):
        return self.quote_text