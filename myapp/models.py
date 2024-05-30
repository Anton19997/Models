from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, through='Borrow')

    def __str__(self):
        return self.user.username

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower.user.username} borrowed {self.book.title}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"

class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True, blank=True, related_name='likes_dislikes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, related_name='likes_dislikes', on_delete=models.CASCADE)
    is_like = models.BooleanField()

    class Meta:
        unique_together = ('user', 'article', 'comment')

    def __str__(self):
        target = self.article if self.article else self.comment
        return f"{self.user.username} {'liked' if self.is_like else 'disliked'} {target}"
