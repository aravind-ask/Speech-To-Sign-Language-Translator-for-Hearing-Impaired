from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

class Translation(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.ForeignKey(Language, related_name='translations_from', on_delete=models.CASCADE)
    target_language = models.ForeignKey(Language, related_name='translations_to', on_delete=models.CASCADE)
