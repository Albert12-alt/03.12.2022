result = []



def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b




data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")
    except SyntaxError:
        print("SyntaxError")
    except AssertionError:
        print("AssertionError")
    except AttributeError:
        print("AttributeError")
    except TabError:
        print("TabError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
print(result)