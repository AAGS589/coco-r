from codecs import code_page_encode
from lib2to3.pgen2 import grammar
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from turtle import title
from lexer import CFG
from direct_afd import AFD
import sys
from parsing import Parser 
from code_generator import CodeGen
from utils import DumpAutomata
from pprint import pprint 


program_title = '''

#\tCOCOR Evaluador de expresiones\t#

Evalúe los tokens en función de un archivo de gramática definido por el usuario. El archivo de gramática predeterminado se toma como input/grammar.cfg. Si desea especificar una gramática propia, puede editar el archivo grammar.cfg actual o crear un archivo .cfg y especificarlo en la entrada del programa.
'''

tokens_generated = '''
Los Tokens generados son los siguientes: '''

file_generated = '''

scanner.py se ha generado en la carpeta raíz. Puede ejecutarlo como `python scanner.py` en su terminal. También puede especificar cualquier archivo para que el escáner lea los tokens; de lo contrario, ./input/test_input.txt se tomará como el archivo predeterminado.

'''

if __name__ == "__main__":

    grammar_file = '.\input\grammar.cfg'

    if len(sys.argv) > 1:
        grammar_file = sys.argv[1]

        try:
            cfg = CFG(grammar_file)
        except FileNotFoundError as e:
            print(f'\tERR: "{grammar_file} archivo sin contenido"')
        except Exception as e:
            print(f'\tERR: {e}')
            exit(-1)

        allchars = cfg.getAllChars()
        parser = Parser(cfg)
        tokens = parser.ToSingleExpression()
        tree = parser.Parse(tokens)


        afd = AFD(tree, allchars, cfg.keywords, cfg.ignore)
        DumpAutomata(afd)

        CodeGen('.\scanner.py', cfg.tokens, afd).GenerateScannerFile()

        print(program_title)
        print(file_generated)           