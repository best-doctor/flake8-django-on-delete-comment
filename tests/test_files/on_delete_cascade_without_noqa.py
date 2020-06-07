from django.db import models

test_field = models.ForeignKey(
    'TestModel',
    on_delete=models.CASCADE,
)
