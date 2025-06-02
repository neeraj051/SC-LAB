def centroid(x, mf):
    return sum(x * mf) / sum(mf)

x = np.random.rand(5)
print(x)
mf = np.exp(-(x - 5)**2 / 4)
print(mf)
print("Centroid (Defuzzified value):", centroid(x, mf))


def fuzzy_controller(temp):
    if temp < 20:
        return "HEAT"
    elif 20 <= temp <= 25:
        return "MAINTAIN"
    else:
        return "COOL"

print(fuzzy_controller(18))
print(fuzzy_controller(23))
print(fuzzy_controller(30))
