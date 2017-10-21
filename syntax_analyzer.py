"""Handles Syntax Analysis"""
#!/usr/bin/python3
import enum
import lexical_analyzer

# with open('symbols.txt') as file:
#     with open('out.txt', mode='w') as out_f:
#         myList = sorted((x for x in file), key=len)
#         for item,i in zip(myList,range(len(myList))):
#             out_f.write('{} = {}\n'.format(str(item).strip(), i))
#         out_f.close()

CONSOLE_DEBUG = True


class Symbol(enum.Enum):
    """Holds the symbols for syntax analysis"""
    If = 0
    IDs = 1
    Body = 2
    Read = 3
    Term = 4
    Real = 5
    Empty = 6
    Write = 7
    While = 8
    Relop = 9
    Rat17F = 10
    Return = 11
    Assign = 12
    Factor = 13
    Primary = 14
    Integer = 15
    Function = 16
    Compound = 17
    Parameter = 18
    Qualifier = 19
    Statement = 20
    Condition = 21
    Identifier = 22
    Expression = 23
    Declaration = 24
    StatementList = 25
    ParameterList = 26
    DeclarationList = 27
    OptParameterList = 28
    OptDeclarationList = 29
    FunctionDefinitions = 30
    OptFunctionDefinitions = 31


class SyntaxAnalyzer(object):
    def __init__(self, file_name):
        in_file = open(file_name)
        self.next_token = lexical_analyzer.Lexer.result("token", "lexeme")
        self.lexer = lexical_analyzer.Lexer()
        self.lex = self.lexer.tokenize(in_file)
        self.factor()
        in_file.close()
    
    def next_tok(self):
        try:    
            self.next_token = next(self.lex)
            return self.next_token
        except StopIteration:
            return False

    def lexeme_is(self, char):
        return self.next_token.lexeme is char

    def lexeme_is_not(self, char):
        return self.next_token.lexeme is not char

    def IDs(self, consume_next=True):
        """  <IDs> ::= <Identifier> | <Identifier>, <IDs>   """

        # Consume next token from generator ?
        if consume_next:
            self.next_tok()

        # Case: Not <IDs>
        if self.next_token.token is not "Identifier":
            return False

        # Case: <Identifier>, ...
        # print("Identifier", end='')
        self.next_tok()
        if self.next_token.lexeme is ',':
            # print(", ", end='')
            return self.IDs()

        # Case: <Identifier>
        print("<IDs>", end='')
        return True

    def primary(self, consume_next=True):
        """   <Primary> ::= <Identifier> | <Integer> | <Identifier> [<IDs>]
                           | ( <Expression> ) |  <Real>  | true | false   """

        # Consume next token from generator ?
        if consume_next:
            self.next_tok()

        if self.next_token.token is "Identifier":
            print("<Primary>", end='')
            self.next_tok()

            print(self.next_token.lexeme, end='')
            if self.next_token.lexeme is not '[':
                return True
            if not self.IDs():
                return False
            self.next_tok()
            print(self.next_token.lexeme, end='')
            return self.lexeme_is(']')

        # TODO Case: ( <Expressio> )

        if self.next_token.token not in {"Float", "Integer"}:
            if self.next_token.lexeme not in {"true", "false"}:
                return False

        print("<Primary>", end='')
        return True


    def factor(self, consume_next=True):
        """"   <Factor> ::= - <Primary> | <Primary>   """

        # Consume next token from generator
        if consume_next:
            self.next_tok()

        # Case: <Primary>
        if self.lexeme_is_not('-'):
            if self.primary(consume_next=False):
                print("<Factor>")
                return True
            else: return False

        # Case: - <Primary>
        if self.primary():
            print("<Factor>")
            return True
        else: return False

    # def addition(self):
    #     self.integer()
    #     self.addition_prime()

    # def addition_prime(self):
    #     self.next_token = next(self.lex)
    #     if self.next_token[1] in {'+', '-'}:
    #         print("Operator Accepted")
    #         self.integer()
    #         self.addition_prime()
    #     else:
    #         pass

    # def integer(self):
    #     self.next_token = next(self.lex)
    #     if self.next_token[0] == 'Integer':
    #         print("Integer Accepted")
    #         return True
    #     else:
    #         print("Error!")
    #         return False
    

def main():
    # with open('test_syntax.txt') as in_file:
    #     la = lexical_analyzer.Lexer()
    #     tokens = la.tokenize(in_file)
    #     for token in tokens:
    #         print(token)
    mySA = SyntaxAnalyzer("test_syntax.txt")



if __name__ == "__main__":
    main()























































