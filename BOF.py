import os
import sys

def errorHandling():
    print("Usage:")
    print("python3 BOF.py [--start <int>] [--step <int>] [--end <end>] \"<path_to_executable>\"")
    exit()


def setParameters():
    start = 5
    end = 10000
    step = 5

    counter = 0

    for arg in sys.argv:
        temp = 0
        if arg == "--start":
            try:
                temp = int(sys.argv[counter+1])
            except:
                errorHandling()
            start = temp

        if arg == "--end":
            try:
                temp = int(sys.argv[counter+1])
            except:
                errorHandling()
            end = temp

        if arg == "--step":
            try:
                temp = int(sys.argv[counter+1])
            except:
                errorHandling()
            step = temp
        counter = counter + 1

    return (start, end, step)


def crashTesting(start, end, step):
    print("Inside crashTesting...")
    for i in range(start, end+1, step):
        print("Trying BOF with input size : " + str(i))
        inp = 'P'*i
        path = "'" + sys.argv[-1] + "'"
        command = "echo " + inp + " | " + path
        print("Executing command:")
        print(command)
        val = os.system(command)
        if val != 0:
            print("Program's Stack Overflowed.")
            print("Buffer Size < " + str(i))
            break

def main():

    if len(sys.argv) == 1:
        errorHandling()

    start = 0
    step = 0
    end = 0

    (start, end, step) = setParameters()
    crashTesting(start, end, step)


if __name__ == "__main__":
    main()
