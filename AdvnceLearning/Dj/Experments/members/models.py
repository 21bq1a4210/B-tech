from django.db import models

class MyModel(models.Model):
    # CharField
    char_field = models.CharField(max_length=255, null=True, blank=True)

    # IntegerField
    int_field = models.IntegerField(null=True, blank=True)

    # FloatField
    float_field = models.FloatField(null=True, blank=True)

    # DecimalField
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # DateField
    date_field = models.DateField(null=True, blank=True)

    # TimeField
    time_field = models.TimeField(null=True, blank=True)

    # DateTimeField
    datetime_field = models.DateTimeField(null=True, blank=True)

    # BooleanField
    boolean_field = models.BooleanField(default=True)

    # EmailField
    email_field = models.EmailField(max_length=255, null=True, blank=True)

    # URLField
    url_field = models.URLField(max_length=255, null=True, blank=True)

    # ImageField
    image_field = models.ImageField(upload_to='images/', null=True, blank=True)

    # FileField
    file_field = models.FileField(upload_to='files/', null=True, blank=True)

    # TextField
    text_field = models.TextField(null=True, blank=True)

    # SlugField
    slug_field = models.SlugField(max_length=255, null=True, blank=True)

    # BinaryField
    binary_field = models.BinaryField(null=True, blank=True)

    # UUIDField
    uuid_field = models.UUIDField(null=True, blank=True)

    my_name = models.CharField(max_length=255, null=True, blank=True)

    # ForeignKey
    # (Example: If you have another model named 'RelatedModel')
    # related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE, null=True, blank=True)

    # OneToOneField
    # (Example: If you have another model named 'OneToOneRelatedModel')
    # one_to_one_related_model = models.OneToOneField(OneToOneRelatedModel, on_delete=models.CASCADE, null=True, blank=True)

    # ManyToManyField
    # (Example: If you have another model named 'ManyToManyRelatedModel')
    # many_to_many_related_models = models.ManyToManyField(ManyToManyRelatedModel, blank=True)

    def __str__(self):
        return f"MyModel #{self.pk}"
