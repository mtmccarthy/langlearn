#modDigitsPi: Int -> Int -> [Int]
#Takes a modulo, a list size and outputs a list of numbers
#correponding to the modulo of the indexth digit of pi
import sys, math

def main():
	modulo = int(sys.argv[1])
	listSize = int(sys.argv[2])
	template = '{0:.' + str(listSize - 1) + 'f}'
	strPi = str(template.format(math.pi))
	for digit in modDigitsPi(modulo, listSize, strPi):
		print(digit)

def modDigitsPi(modulo, listSize, strPi):
  return map((lambda digit: modPi(digit, modulo)), strPi)

def modPi(strDigit, modulo):
	if(strDigit == '.'):
		return -1
	return int(strDigit)*31 % modulo


if __name__ == "__main__":
  main()