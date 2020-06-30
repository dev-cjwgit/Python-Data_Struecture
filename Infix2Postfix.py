import Stack

def precedence(op):
    if op == '(' or op == ')': return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1

class Infix():
    def __init__(self):
        super().__init__()
        self.expr = []

    def add(self,expr):
        for i in range(len(expr)):
            if expr[i] == '（':
                self.expr.append('(')
            elif expr[i] == '）':
                self.expr.append(')')
            elif expr[i] == '＋':
                self.expr.append('+')
            elif expr[i] == '―':
                self.expr.append('-')
            elif expr[i] == 'Ｘ':
                self.expr.append('*')
            else:
                self.expr.append(str(expr[i]))

    def Infix2Postfix(self): #중위 -> 후위 변환
        s = Stack.Stack()

        output = []
        for term in self.expr:
            if term in '(':
                s.push('(')
            elif term in ')':
                while not s.isEmpty():
                    op = s.pop()
                    if op == '(': break
                    else:
                        output.append(op)
            elif term in "+-*/":
                while not s.isEmpty():
                    op = s.peek()
                    if (precedence(term) <= precedence(op)):
                        output.append(op)
                        s.pop()
                    else: break
                s.push(term)
            else:
                output.append(term)
        while not s.isEmpty():
            output.append(s.pop())

        return output

    def evalPostfix(self,result): #계산
        s = Stack.Stack()
        try:
            for token in result:
                if token in "+-*/":
                    val2 = s.pop()
                    val1 = s.pop()

                    if token == '+': s.push(val1 + val2)
                    elif token == '-': s.push(val1 - val2)
                    elif token == '*': s.push(val1*val2)
                    elif token == '/': s.push(val1 / val2)
                else:
                    s.push(int(token))
            return s.pop()
        except Exception:
            return None