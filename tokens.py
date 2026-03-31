import re

RULES = [
    ('KEYWORD', r'\b(if|else|while|for|return|def)\b'),
    ('NUMBER', r'\d+'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MUL', r'\*'),
    ('DIV', r'/'),
    ('ASSIGN', r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SPACE', r'[ \t\n\r]+')
]

COLORS = {
    'KEYWORD': '#C586C0',
    'NUMBER': '#B5CEA8',
    'ID': '#9CDCFE',
    'PLUS': '#D4D4D4',
    'MINUS': '#D4D4D4',
    'MUL': '#D4D4D4',
    'DIV': '#D4D4D4',
    'ASSIGN': '#D4D4D4',
    'LPAREN': '#FFD700',
    'RPAREN': '#FFD700',
    'LBRACE': '#DA70D6',
    'RBRACE': '#DA70D6',
    'SPACE': None 
}
