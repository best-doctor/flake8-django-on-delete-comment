check:
	flake8 .
	mypy flake8_django_on_delete_comment
	python -m pytest --cov=flake8_django_on_delete_comment --cov-report=xml
	mdl README.md
	safety check -r requirements.txt
