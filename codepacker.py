class CodeMeta():
    def __init__(self, name, var, scopes):
        self.name = name
        self.var = var
        self.scopes = scopes

def get_meta(name, code_paragraph):
    lines = __code_to_lines(code_paragraph)
    varlist = __get_variables(lines)
    scopes = __get_scopes(lines)
    return CodeMeta(name, varlist, scopes)

def __code_to_lines(code_paragraph):
    lines, j = [], 0
    if code_paragraph == None or code_paragraph == "":
        return lines
    code_paragraph = code_paragraph.strip()
    for i in range(0, len(code_paragraph)):
        if code_paragraph[i] == "\n":
            lines.append(code_paragraph[j:i])
            j = i
    if len(lines) == 0:
        lines.append(code_paragraph)
    return lines

def __get_variables(code_lines):
    var = {}
    for l in code_lines:
        idx = l.find("=")
        if idx < 0:
            continue
        if l[idx+1] == "=":
            continue
        s = l.replace(" ", "").split("=")        
        left, right = s[0].split(","), s[1].split(",")
        for i in range(0, len(left)):
            if left[i] in var:
                continue
            var[left[i]] = __infer_inittype(right[i])
    return var
    
def __get_scopes(code_lines):
    scopes = {}
    scopes["root"] = (0, len(code_lines))
    depth, stack = 0, []
    for i in range(0, len(code_lines)):
        if code_lines[i][-1] == ":":
            depth = depth + 1
            stack.append((depth, i))
            continue
        indents = __count_indents(code_lines[i])
        if indents == 4*(depth-1) or (i == len(code_lines) and indents > 0):
            last = stack.pop()
            scopes[f'scope-{len(scopes)}'] = (last[1], i)
            depth = depth - 1
    return scopes

def __infer_inittype(value):
    if type(value) is not str:
        return (type(value), value)
    if value.isnumeric():
        return (type(1), int(value))

def __count_indents(code_line):
    for i in range(0, len(code_line)):
        if code_line[i] != " ": return i+1
    return 0