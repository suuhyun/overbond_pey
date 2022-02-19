import datetime
import matplotlib.pyplot as plt

def parse_data(f):
    result = []
    file = open(f, "r", encoding="utf8")
    while file.readline():
        issuance_date = ''
        cleanbid = 0
        cleanask = 0
        last_price = 0

        for line in file.readlines():
            line = line.strip()
            if line.startswith('DIs'):
                if issuance_date:
                    result.append((issuance_date, cleanbid, cleanask, last_price))
                    cleanbid = 0
                    cleanask = 0
                    last_price = 0
                issuance_date = line[3:]
            elif line.startswith('BPr'):
                cleanbid = float(line[3:])
            elif line.startswith('APl'):
                cleanask = float(line[3:])
            elif line.startswith('Pl'):
                last_price = float(line[2:])

        if issuance_date and cleanbid + cleanask + last_price != 0:
            result.append((issuance_date, cleanbid, cleanask, last_price))

    return result

def display(result_data):
    dates = []
    cleanbids = []
    cleanasks = []
    last_prices = []
    result_data.sort(key=lambda result_data:result_data[0])
    
    for i in result_data:
        dates.append(i[0])
        cleanbids.append(i[1])
        cleanasks.append(i[2])
        last_prices.append(i[3])
    
    x_values = dates
    ax = plt.gca()
    plt.ylim(0, max(cleanbids+cleanasks+last_prices)+10)
    ax.scatter(x_values, cleanbids, color='b')
    ax.scatter(x_values, cleanasks, color='r')
    ax.scatter(x_values, last_prices, color='y')
    plt.show()

if __name__ == '__main__':
    f = 'example.txt'
    result = parse_data(f)
    print(result)
    display(result)
