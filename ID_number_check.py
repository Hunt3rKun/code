def CheckCode(num18):
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    tablecM = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '7', 8: '4', 9: '3', 10: '2'}
    sum = 0
    num17 = num18[0:17]
    check_bit = num18[-1]
    for i, data in enumerate(num17):
        sum += int(data) * weight[i]
    result = (tablecM.get(sum % 11) == check_bit)
    return result

print(CheckCode(''))
