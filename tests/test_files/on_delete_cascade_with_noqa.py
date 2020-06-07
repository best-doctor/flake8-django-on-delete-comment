from django.db import models


test_field = models.ForeignKey(  # allowed_cascade
    'TestModel',
    on_delete=models.CASCADE,
)

other_test_field = models.ForeignKey(  # allowed_cascade
    'OtherTestModel',
    models.CASCADE,
)
