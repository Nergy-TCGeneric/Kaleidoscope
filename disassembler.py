#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Disassembler accepts only list of strings, i.e. a line of codes.

# assumptions can be formularized by like this :
# variable -> operator, value, scope.
# = Variable restraint is effective on A to B.

class Assumption:
    def __init__(var, op, val, scope):
        self.var = var
        self.op = op
        self.val = val
        self.scope = scope
    
    def operate():
        pass

OPERATORS = [">", "<", "==", ">=", "<=", "!=", "*", "+", "-", "**", "And", "Or"]
conditional_index = {}
        
def to_lines(p):
    lines, j = [], 0
    for i in range(0, len(p)):
        if p[i] == "\n":
            lines.append(p[j:i])
            j = i
    if len(lines) == 0:
        lines.append(p)
    return lines     
        
def find_explicit_assumption(cond_id):
    explicits = []
    for l in code:
        if l.find("if") > 0:
            explicits.append(l)
    return explicits
    
def get_statement_components(cond_id):
    if cond_id not in conditional_index:
        return []
    comp = conditional_index[cond_id].split(" ")
    return comp[:1]
    
def index_conditionals(code):
    stack, order, cond = [], 0, {}
    for i in range(0, len(code)):
        idx = code[i].find("if")
        if idx > 0:
            order = order + 1
            stack.push((idx % 4, order, i))
        else:
            last = stack.peek()
            if code[i][:last[0]*4].replace(" ", "") == "":
                last = stack.pop()
                cond["if-" + order] = (last[3], i)
    return cond

def get_variables(code):
    var = {}
    for l in code:
        idx = l.find("=")
        if idx < 0:
            continue
        if l[idx+1] == "=":
            continue
        s = l.replace(" ", "").split("=")        
        left, right = s[0].split(","), s[1].split(",")
        for i in range(0, len(left)):
            var[left[i]] = [type(right[i]), right[i]]
    return var

def get_variable_range(var, code_p):
    restraints = find_explicit_assumption(code)
    for l in code:
        pass
    pass