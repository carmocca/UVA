import sys


class Car:

    def __init__(self, plate):
        self.plate = plate
        self.records = []

    def __repr__(self):
        return str(self.records)

    def add_record(self, record):
        self.records.append(Record(record[0], record[1], record[2]))

    def order_records(self):
        self.records.sort(key=lambda x: x.timestamp)

    def calculate_bill(self, fares):
        bill = 0.0
        valid_bill = False
        enter = False
        for record in self.records:
            if record.action == "enter":
                fare = fares[int(record.timestamp[4:6])]
                km = int(record.km)
                enter = True
            if enter and record.action == "exit":
                km = abs(km - int(record.km))
                bill += fare / 100 * km + 1.0
                valid_bill = True
                enter = False
        if not valid_bill:
            return bill
        return bill + 2.0


class Record:

    def __init__(self, timestamp, action, km):
        self.timestamp = timestamp
        self.action = action
        self.km = km

    def __repr__(self):
        return self.timestamp + " - " + self.action + " - " + self.km


cars = {}


def solve(fares, records):
    global cars
    res = []
    for record in records:
        cars.setdefault(record[0], Car(record[0])).add_record(record[1:])
    for plate in sorted(cars.keys(), key=lambda x: x.lower()):
        cars[plate].order_records()
        bill = cars[plate].calculate_bill(fares)
        if bill:
            res.append(plate + " $" + "{0:.2f}".format(round(bill, 2)))
    cars.clear()
    return res


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        fares = [int(f) for f in file.readline().split()]
        records = []
        while True:
            record = [x.replace(':', '') for x in file.readline().split()]
            if len(record) == 0:
                break
            records.append(record)
        bills = solve(fares, records)
        res.extend(bill + '\n' for bill in bills)
        res.append('\n')
    return res[:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
