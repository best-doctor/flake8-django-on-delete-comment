import typing

from setuptools import setup, find_packages


package_name = 'flake8_django_on_delete_comment'


def get_version() -> typing.Optional[str]:
    with open('flake8_django_on_delete_comment/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='A flake8 extension to validate django models ForeignKey fields on on_delete CASCADE comment',
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    keywords='flake8 on_delete',
    version=get_version(),
    author='BestDoctor',
    author_email='khkaterine@gmail.com',
    install_requires=['flake8'],
    entry_points={
        'flake8.extension': [
            'CD001 = flake8_django_on_delete_comment.checker:DjangoOnDeleteCommentChecker',
        ],
    },
    url='https://github.com/best-doctor/flake8-django-on-delete-comment',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
