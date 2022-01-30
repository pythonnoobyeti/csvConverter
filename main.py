from utils import csvConverter
data_1 = 'data_1.csv'
data_2 = 'data_2.csv'

if __name__ == "__main__":
  convertedData_1 = csvConverter(data_1)
  convertedData_2 = csvConverter(data_2)
  print(convertedData_1)
  print(convertedData_2)