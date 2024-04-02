import ply.yacc as yacc
from analizador_lexico import tokens



def p_program(p):
    '''
    program : statements
    '''
    return "Programa válido."

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

def p_statement(p):
    '''
    statement : expression SEMICOLON
              | for_loop
              | println_statement
    '''
    return "Declaración válida."

def p_for_loop(p):
    '''
    for_loop : FOR LPAREN for_assignment SEMICOLON condition SEMICOLON increment RPAREN LEFT_BRACE statements RIGHT_BRACE
    '''
    p[0] = "Bucle For válido."

def p_for_assignment(p):
    '''
    for_assignment : ID EQUALS NUMBER
    '''
    p[0] = "Asignación en bucle For válida."

def p_println_statement(p):
    '''
    println_statement : SYSTEM DOT OUT DOT PRINTLN LPAREN expression RPAREN SEMICOLON
    '''
    return "Declaración de impresión válida."

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    return "Asignación válida."

def p_condition(p):
    '''
    condition : expression
    '''
    return "Condición válida."

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | ID
               | NUMBER
               | INCREMENT
               | STRING
               | expression LESS_THAN expression
               | expression GREATER_THAN expression
               | expression LESS_THAN_EQUAL expression
               | expression GREATER_THAN_EQUAL expression
               | expression EQUAL_EQUAL expression
               | expression NOT_EQUAL expression
    '''
    return"Expresión válida."

def p_increment(p):
    '''
    increment : ID INCREMENT
    '''
    return"Incremento válido."

def p_error(p):
    if p:
        return f"Error de sintaxis en el token '{p.value}', tipo '{p.type}' en la línea {p.lineno}"
    else:
        return "Error de sintaxis no valida"

parser = yacc.yacc()

input_code = "for(i = 0; i < 10; i++) { println(System.out.println(i)); }"
resultado = parser.parse(input_code)
print(resultado)
