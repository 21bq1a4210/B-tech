# from django.db import models
#
# class UploadedImage(models.Model):
#     CATEGORY_CHOICES = [
#         ('watch', 'Watch'),
#         ('laptop', 'Laptop'),
#         ('mobile', 'Mobile'),
#         ('gold_ornament', 'Gold Ornament'),
#         ('bag', 'Bag'),
#         ('earbuds', 'Earbuds'),
#         ('others', 'Others'),
#     ]
#
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     image = models.ImageField(upload_to='uploaded_images/')
