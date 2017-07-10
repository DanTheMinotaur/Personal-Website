from django.db import models


class HomepageLink(models.Model):
    link_name = models.CharField(max_length=50)
    link_description = models.CharField(max_length=255, blank=True)
    link_url = models.URLField()
    link_image = models.ImageField(upload_to='site_images/homepage/')  # Check where this will save files to
    optional_class = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.link_name

