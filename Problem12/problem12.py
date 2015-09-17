

class Solver:

    def __init__(self):
        pass

    def genTriangleNumber(self, n):
        return(n*(n+1)/2)

    def findPrimeDivisors(self, number):
        primes = []
        numberDivide = 2
        foundAll = False
        while (not foundAll):
            if (number % numberDivide == 0):
                number = number/numberDivide
                primes.append(numberDivide)
                if (number == 1):
                    foundAll = True
                numberDivide = 1
            numberDivide += 1
        return primes

    def numDivisors(self, primeList):
        numDivs = 1
        count = 1
        for i in range(1, len(primeList)):
            if (primeList[i-1] == primeList[i]):
                count += 1
            else:
                numDivs *= count + 1
                count = 1
        numDivs *= count + 1
        return numDivs

    def solveProblem(self):
        triangleNumber = 100
        while(self.numDivisors(self.findPrimeDivisors(self.genTriangleNumber(triangleNumber))) < 500):
            triangleNumber += 1

        print triangleNumber
        return self.genTriangleNumber(triangleNumber)

if __name__ == "__main__":
    solver = Solver()
    print(solver.genTriangleNumber(2))
    print(solver.findPrimeDivisors(28))
    print(solver.numDivisors(solver.findPrimeDivisors(28)))
    print(solver.solveProblem())
