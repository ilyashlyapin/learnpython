def get_vat(payment, percent=18):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * 20
		vat = round(vat,2)
		return 'НДС: {}'.format(vat) 
	except (TypeError, ValueError):
		return 'Wrong input, please check' 


result = get_vat(400, 18)
print(result)
