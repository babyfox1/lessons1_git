# Function Vat


def get_vat(payment, persent = 20):
    try:
        payment = float(payment)
        vat = payment / 100 * persent
        vat = round(vat, 2)
        return "sum VAT: {}".format(vat)
    except TypeError:
        return "loh"
result = get_vat(400, 15)
print(result)
