def gcd(a, b):
	"""Рекурсивная функция нахождения НОДа"""
	return b and gcd(b, a%b) or a


def usinp():
	while(1):
		try:
			a = int(input("input a: "))
			b = int(input("input b: "))
			break
		except:
			print('wrong input')
	print('GSD = {}'.format(gcd(a, b)))


if __name__ == "__main__":
	usinp()
	