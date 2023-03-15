class Scanner:
  def __init__(self, expression):
    self.expression = expression.replace(' ', '')
    self.cursor = 0
    self.binops = {
      '+': 'plus',
      '-': 'minus',
      '*': 'mult',
      '/': 'div',
      '(': 'open_paren',
      ')': 'close_paren'
    }

  def at_cursor(self) -> str:
    return self.expression[self.cursor]

  def scan(self):
    start = self.cursor
    token_id = ''

    # jeśli token zaczyna się na cyfrę skanujemy kolejne cyfry
    if self.at_cursor().isnumeric():
      token_id = 'number'

      while self.cursor < len(self.expression) and self.at_cursor().isnumeric():
        self.cursor += 1
      token_value = self.expression[start:self.cursor]

    # jeśli token zaczyna się na literę skanujemy kolejne litery i cyfry
    elif self.at_cursor().isalpha():
      token_id = 'ID'

      while self.cursor < len(self.expression) and (self.at_cursor().isnumeric() or self.at_cursor().isalpha()):
        self.cursor += 1
      token_value = self.expression[start:self.cursor]

    # operatory jednoznakowe
    elif (key := self.at_cursor()) in self.binops.keys():
      self.cursor += 1
      return self.binops[key], key

    # jeśli żaden token nie został dopasowany do pierwszej litery - wypisuje komunikat i skanuje dalej
    else:
      print(f'\'{self.at_cursor()}\' at position {start} isn\'t allowed in mathematical expression')
      self.cursor += 1
      return '', ''

    return token_id, token_value

  def scan_expression(self):
    while self.cursor < len(self.expression):
      token = self.scan()
      if token[0] != '':
        print(f'(kod: {token[0]}, value: {token[1]})')


expr1 = 'xd123+**123koks.d+\/;.xyz+5abc'
expr2 = '2+3 *(* (76+8/)3)+pat3+  7 +3*(9-3)'
scanner1 = Scanner(expr1)
scanner1.scan_expression()