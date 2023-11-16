glossary = {
    'variables': 'Data "held" in "containers" This data is then stored in these containers for future use.',
    'syntax': 'A set of rules that define particular layouts of letters and symbols.',
    'tools': 'A piece of software that helps programmers write code much faster.',
    'repository': 'A folder that houses all the projects source files and it is kept in a place you can access to view those files.',
    'loops': 'It runs a code block after checking a condition. Until a certain condition is met, the loop will keep checking and running.',
    'operator': 'A term used to denote the object which can manipulate different operands.',
    'expression': 'A legal grouping of letters, symbols, and numbers being used to represent the value of one or more variables.',
    'bug': 'A general term used to denote an unexpected error or defect in hardware or software, which causes it to malfunction',
    'objects': 'A combination of related variables, constants and other data structures which can be selected and manipulated together.',
    'keywords': 'Words that are reserved by a programming language or a program as they have special meaning,',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")