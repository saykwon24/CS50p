"""
PEP 8: Style Guide for Python Code (for readability)
    >>> https://peps.python.org/pep-0008/

1. Indentation: 4 spaces or Tabs
2 Maximum Line Length: 79 characters
3. Blank Lines: Use blank lines to separate functions and classes
4. Imports: Imports should be on separate lines
5. Whitespace: Avoid extra spaces in expressions and statements
6. Naming Conventions: Use lowercase with underscores for functions and variables, CamelCase for classes
7. Comments: Use comments to explain code, and use docstrings for functions and classes
8. Docstrings: Use triple quotes for docstrings, and include a summary and parameters
9. Exceptions: Use specific exceptions, and avoid bare except clauses
10. Code Layout: Use consistent formatting, and keep related code together
...


pylint: 코드에 실수가 있는지, 스타일이 일관되는지 검사하는 도구
pycodestyle: PEP 8 스타일 가이드에 따라 코드를 작성, pylint보다는 덜 엄격하고 가벼운 도구
black: 코드 포매팅 도구, PEP 8 스타일 가이드를 따르며 자동으로 코드를 정리해줌
       terminal 창에 'black fileName' 입력하여 실행
"""


students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin", "Padma": "Ravenclaw",}
for student in students:
  print(student)
