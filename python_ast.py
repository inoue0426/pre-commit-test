import ast
import sys


def check_python_ast(filename):
    with open(filename, "r") as file:
        content = file.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Syntax error in {filename} at line {e.lineno}, column {e.offset}")
        print(f"Error details: {e}")
        return False

    unused_vars = set()
    defined_vars = set()
    used_vars = set()

    class VarVisitor(ast.NodeVisitor):
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):
                defined_vars.add(node.id)
            elif isinstance(node.ctx, ast.Load):
                used_vars.add(node.id)

    VarVisitor().visit(tree)
    unused_vars = defined_vars - used_vars

    if unused_vars:
        print(f"Unused variables found in {filename}: {', '.join(unused_vars)}")

    class FuncVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            if len(node.body) > 10:
                print(
                    f"Complex function found in {filename}: {node.name} ({len(node.body)} lines)"
                )

    FuncVisitor().visit(tree)

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    print(f"Imports in {filename}: {', '.join(imports)}")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_python_ast.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if check_python_ast(filename):
        print(f"AST check completed for {filename}")
    else:
        print(f"AST check failed for {filename}")
