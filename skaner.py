class Scanner:
	def __init__(self, expression):
		self.expression = expression.replace(' ', '')
		self.idx = 0
		self.token_ids = {
			'+': 'plus',
			'-': 'minus',
			'*': 'multiply',
			'/': 'divide',
			'(': 'opening bracket',
			')': 'closing bracket'
		}


	def scan(self):
		expr = self.expression
		start = self.idx
		last_read = self.idx

		token_id = ''
		token_value = expr[start]

		# jeśli token zaczyna się na cyfrę skanujemy kolejne cyfry
		if token_value.isnumeric():
			token_id = 'number'

			while token_value.isnumeric():
				if last_read - 1 == len(expr):
					self.idx = last_read
					return token_id, token_value

				last_read += 1
				token_value = expr[start:last_read]

		# jeśli token zaczyna się na literę skanujemy kolejne litery i cyfry
		elif token_value.isalpha():
			token_id = 'ID'

			while token_value[-1].isnumeric() or token_value[-1].isalpha():
				if last_read - 1 == len(expr):
					self.idx = last_read
					return token_id, token_value

				last_read += 1
				token_value = expr[start:last_read]

		# tokeny jednoliterowe
		elif token_value in self.token_ids.keys():
			self.idx += 1
			return self.token_ids[token_value], token_value

		# jeśli żaden token nie został dopasowany do pierwszej litery - wypisuje komunikat i skanuje dalej
		else:
			print(f'\'{token_value}\' in position {start} isn\'t allowed in mathematical expression')
			self.idx += 1
			return '', ''


		# obsługa przypadku ciąg cyfr + litera (np. '4278s')
		if token_value[0].isnumeric() and token_value[-1].isalpha():
			print(f'\'{token_value}\' in position {start} isn\'t allowed in mathematical expression')
			self.idx = last_read - 1
			return '', ''

		self.idx = last_read - 1

		return token_id, token_value[:-1]


	def scan_expression(self):
		while self.idx < len(self.expression):
			token = self.scan()
			if token[0] != '':
				print(f'(kod: {token[0]}, value: {token[1]})')


expr1 = 'xd123+**123koks.d+\/;.pnobhddd+5'
expr2 = '2+3 *(* (76+8/)3)+pat3+  7 +3*(9-3)'
scanner1 = Scanner(expr2)
scanner1.scan_expression()