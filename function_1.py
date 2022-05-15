def get_sum(one, two, delimiter ="&"):
        if delimiter != ("&"):
            raise ValueError("Тут неверный символ")
        else:
            allsumm = (one+delimiter+two)
        return(allsumm)
x = get_sum("Learn","python")
x = str(x.upper())
print(x)
