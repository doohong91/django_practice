from django.db import models


class Posting(models.Model):
    content = models.TextField(default='')
    icon = models.CharField(max_length=20)
    # upload URL(Uniform Resource Locator) => /media/posting/origin/20190312/
    image = models.ImageField(blank=True, upload_to='posting/origin/%Y%m%d')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.id}: {self.content[:20]}>'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print()
        print(f'=== Saved Posting with id: {self.id}')
        print(f'    content: {self.content}')
        if self.image:
            print(f'    image_size: {self.image.width}px * {self.image.height}px: {round(self.image.size / 1024)}kb')
        print('==========================================')
        print()
