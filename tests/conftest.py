import os
import ast

from flake8_django_on_delete_comment.checker import DjangoOnDeleteCommentChecker


def run_validator_for_test_files(filename: str):
    test_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_files',
        filename,
    )
    with open(test_file_path, 'r') as file_handler:
        raw_content = file_handler.read()
    tree = ast.parse(raw_content)
    checker = DjangoOnDeleteCommentChecker(tree=tree, filename=test_file_path)

    return list(checker.run())
