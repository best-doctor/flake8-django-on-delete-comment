import ast
import typing
import tokenize

NOQA_FOR_CASCADE_ON_DELETE = '# allowed_cascade'


def get_field_lines_with_on_delete_cascade(ast_tree: ast.AST) -> typing.Set:
    field_lines_with_cascade_on_delete = set()
    lines_with_cascade_attr = set()
    for node in ast.walk(ast_tree):
        if not isinstance(node, ast.Call):
            continue
        for keyword in node.keywords:
            if keyword.arg == 'on_delete' and (
                    hasattr(keyword.value, 'value') and keyword.value.attr == 'CASCADE'):  # type: ignore
                field_lines_with_cascade_on_delete.add(node.lineno)
                lines_with_cascade_attr.add(keyword.value.lineno)
                break

        for child_node in ast.iter_child_nodes(node):
            if isinstance(child_node, ast.Attribute) and (child_node.attr == 'CASCADE') and (
                    node.lineno not in lines_with_cascade_attr):
                field_lines_with_cascade_on_delete.add(node.lineno)
    return field_lines_with_cascade_on_delete


def get_lines_with_cascade_noqa(filepath: str) -> typing.Set:
    with tokenize.open(filepath) as f:
        line_numbers_with_noqa = set()
        for line in tokenize.generate_tokens(f.readline):
            if (tokenize.COMMENT in line) and (NOQA_FOR_CASCADE_ON_DELETE in line.string):
                line_numbers_with_noqa.add(line.start[0])
    return line_numbers_with_noqa


def get_cascade_lines_without_noqa(filepath: str, ast_tree: ast.AST) -> typing.Set:
    line_numbers_with_noqa = get_lines_with_cascade_noqa(filepath)
    lines_with_cascade_attr = get_field_lines_with_on_delete_cascade(ast_tree)

    return lines_with_cascade_attr.difference(line_numbers_with_noqa)
