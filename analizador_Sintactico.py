import ply.yacc as yacc
from analizador_lexico import tokens  # Asegúrate de que esto coincida con el nombre de tu archivo léxico

# Definición de reglas sintácticas
def p_program(p):
    '''
    program : object_declaration
    '''
    p[0] = "Programa Scala válido."

def p_object_declaration(p):
    '''
    object_declaration : OBJECT ID LBRACE main_declaration RBRACE 
    '''
    p[0] = "Declaración de objeto válida."

def p_main_declaration(p):
    '''
    main_declaration : DEF MAIN LPAREN args LBRACE statements RBRACE 
    '''
    p[0] = "Declaración del método main válida."


def p_args(p):
    '''
    args : ARGS COLON ARRAY LEFT_BRACKET STRING_TYPE RIGHT_BRACKET RPAREN COLON UNIT EQUALS
    '''
    p[0] = "Argumentos del método main válidos."

def p_block(p):
    '''
    block : LBRACE statements RBRACE
    '''
    p[0] = "Bloque de código válido."

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    # Esta estructura permite múltiples declaraciones en un bloque.
    # No es necesario asignar un valor a p[0] en esta definición.

def p_statement(p):
    '''
    statement : expression SEMICOLON
              | println_statement
              | assignment
    '''
    # Esta definición permite expresiones, declaraciones de impresión y asignaciones como declaraciones válidas.

def p_println_statement(p):
    '''
    println_statement : PRINTLN LPAREN expression RPAREN SEMICOLON
                      | PRINTLN LPAREN STRING_LITERAL RPAREN SEMICOLON
    '''
    p[0] = "Declaración de impresión válida."
    
def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
    '''
    # Completa con lógica similar a la mostrada anteriormente.

def p_term(p):
    '''
    term : factor
         | term TIMES factor
         | term DIVIDE factor
    '''
    # Completa con lógica para manejar términos.

def p_factor(p):
    '''
    factor : NUMBER
           | ID
           | LPAREN expression RPAREN
    '''
    # Ya está correctamente definido.

# Para `p_assignment`, asegúrate de que está correctamente definido.
# Si tienes otras estructuras como bucles for/while, condicionales, etc., asegúrate de definirlas aquí.

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = "Asignación válida."


def p_error(p):
    if p is not None:
        mensaje_error = f"Error de sintaxis en el token '{p.value}', tipo '{p.type}' en la línea {p.lineno}"
        raise SyntaxError(mensaje_error)
    else:
        raise SyntaxError("Error de sintaxis: No se pudo construir el árbol de análisis.")

parser = yacc.yacc(errorlog=yacc.NullLogger())


def parse_code(code, debug=None):
    try:
        parser.parse(code, debug=debug)
        resultado_sintactico = {"status": "success", "message": "Análisis sintáctico exitoso"}
    except SyntaxError as e:
        resultado_sintactico = {"status": "error", "message": str(e)}
        if debug:
            debug.append(resultado_sintactico)  

    return resultado_sintactico