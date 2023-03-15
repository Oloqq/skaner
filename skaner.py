class Scanner:
  def __init__(self, expression):
    self.expression = expression.replace(' ', '')
    self.cursor = 0

  def at_cursor(self) -> str:
    return self.expression[self.cursor]

  def scan(self):
    start = self.cursor

    token_id = ''

    # jeśli token zaczyna się na cyfrę skanujemy kolejne cyfry
    if self.at_cursor().isnumeric():
      token_id = 'number'

      self.cursor += 1
      while self.at_cursor().isnumeric() and self.cursor < len(self.expression):
        self.cursor += 1
      token_value = self.expression[start:self.cursor]

    # jeśli token zaczyna się na literę skanujemy kolejne litery i cyfry
    elif self.at_cursor().isalpha():
      token_id = 'ID'

      self.cursor += 1
      while (self.at_cursor().isnumeric() or self.at_cursor().isalpha()) and self.cursor < len(self.expression):
        self.cursor += 1
      token_value = self.expression[start:self.cursor]

    # operatory binarne
    elif (value := self.at_cursor()) in ['+', '-', '*', '/']:
      self.cursor += 1
      return "binary_op", value

    # nawiasy
    elif (value := self.at_cursor()) in ['(', ')']:
      self.cursor += 1
      return 'parenthesis', value

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


expr1 = 'xd123+**123koks.d+\/;.pnobhddd+5'
expr2 = '2+3 *(* (76+8/)3)+pat3+  7 +3*(9-3)'
scanner1 = Scanner(expr2)
scanner1.scan_expression()