import json
import csv


def csvConverter(path):
    """Convert csv to json or yaml, depends on last value on 1st line"""
    with open(path, 'r') as file:
        reader = csv.reader(file)
        columnHeaders = next(reader)
        outFormat = columnHeaders.pop()

        if outFormat == 'json':
            data = []
            for row in reader:
                data.append(dict(zip(columnHeaders, row)))
            return json.dumps(data, indent=4)

        if outFormat == 'yaml':
            data = '---'
            for row in reader:
                rowData = list(zip(columnHeaders, row))
                data += tupleListToYaml(rowData)
            return data


def tupleListToYaml(data):
    return '\n-\n' + '\n'.join(str(e) for e in data).replace(" ", ": ").replace(
        "(", "    ").replace(")", "").replace("'", '').replace(",", '')
