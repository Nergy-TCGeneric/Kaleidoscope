#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import disassembler
import codepacker

code = input("enter the python code : \n")
    
meta = codepacker.get_meta("STUB", code)
print(meta)
assumptions = disassembler.find_explicit_assumption(c_lines)
print(assumptions)