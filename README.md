# flake8-django-on-delete-comment

[![Build Status](https://travis-ci.org/best-doctor/flake8-django-on-delete-comment.svg?branch=master)](https://travis-ci.org/best-doctor/flake8-django-on-delete-comment)
[![Maintainability](https://api.codeclimate.com/v1/badges/3518733cdde9eede8959/maintainability)](https://codeclimate.com/github/best-doctor/flake8-django-on-delete-comment/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3518733cdde9eede8959/test_coverage)](https://codeclimate.com/github/best-doctor/flake8-django-on-delete-comment/test_coverage)

A flake8 extension to validate django models ForeignKey fields
on on_delete CASCADE comment.

```python
test_field = models.ForeignKey(  # allowed_cascade
    'TestModel',
    on_delete=models.CASCADE,
)
```

CASCADE can be not safe to choose, so such fields should be marked by comment.

## Installation

```terminal
pip install flake8-django-on-delete-comment
```

## Example

Sample file:

```python
# test.py

first_field = models.ForeignKey(  # allowed_cascade
    'FirstModel',
    on_delete=models.CASCADE,
)

second_field = models.ForeignKey(
    'SecondModel',
    on_delete=models.CASCADE,
)

third_field = models.ForeignKey(
    'ThirdModel',
    on_delete=models.PROTECT,
)
```

Usage:

```terminal
$ flake8 test.py
test.py:6:1: CD001 field needs a valid comment for on_delete
```

## Contributing

We would love you to contribute to our project. It's simple:

1. Create an issue with bug you found or proposal you have.
   Wait for approve from maintainer.
1. Create a pull request. Make sure all checks are green.
1. Fix review comments if any.
1. Be awesome.

Here are useful tips:

- You can run all checks and tests with `make check`.
  Please do it before TravisCI does.
- We use [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/en/python_styleguide.md).
- We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
