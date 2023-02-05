from django.db import models

import author.models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey("author.Profile", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=303)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tags')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AdditionalText(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class AdditionalPicture(models.Model):
    article_text = models.ForeignKey(AdditionalText, on_delete=models.CASCADE)
    image = models.ImageField()
    is_vite = models.BooleanField(default=True)


class Comment(models.Model):
    author = models.ForeignKey("author.Profile", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField(max_length=303, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     # return self.article
    #     if self.author.user.get_full_name():
    #         return f"{self.author.user.get_full_name()}'s comment"
    #     return self.author.user.username
