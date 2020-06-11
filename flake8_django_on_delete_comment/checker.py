import ast
import typing
from flake8_django_on_delete_comment import __version__ as version

from flake8_django_on_delete_comment.ast_helpers import get_cascade_lines_without_noqa

ErrorType = typing.Tuple[int, int, str, type]


class DjangoOnDeleteCommentChecker:
    name = 'flake8-django-on-delete-comment'
    version = version

    def __init__(self, tree: ast.AST, filename: str):
        self.filename = filename
        self.tree = tree

    def run(self) -> typing.Generator[ErrorType, None, None]:
        if 'migrations' not in self.filename:
            cascade_lines_without_noqa = get_cascade_lines_without_noqa(self.filename, self.tree)
            errors = self.get_on_delete_comment_errors(cascade_lines_without_noqa)
            for error in errors:
                yield (*error, type(self))

    def get_on_delete_comment_errors(
        self,
        cascade_lines_without_noqa: typing.Set[int],
    ) -> typing.List[typing.Tuple[int, int, str]]:
        errors: typing.List[typing.Tuple[int, int, str]] = []
        if cascade_lines_without_noqa:
            for line in cascade_lines_without_noqa:
                errors.append((
                    line,
                    0,
                    'CD001 field needs a valid comment for on_delete',
                ))

        return errors
