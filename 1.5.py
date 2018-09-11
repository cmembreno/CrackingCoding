def arrayMethod(array1, array2):
    if(abs(len(array1)-len(array2)>1)):
        print("False")

    word = {}
    result = 0
    j = 0

    if(len(array1)>len(array2)):
        for i in range(0,len(array1)):
            if(array1[i]==array2[j]):
                j+=1
                continue
            else:
                result+=1
    elif(len(array1)==len(array2)):
        for i in range(0,len(array1)):
            if (array1[i] == array2[j]):
                j += 1
                continue
            else:
                result += 1
                j+=1
    else:
        for i in range(0,len(array2)):
            if(array1[j]==array2[i]):
                j+=1
                continue
            else:
                result+=1

    print(result)
    if(result>1):
        print("false")
    else:
        print("true")


def main():
    arrayMethod("pale","bakllllllle")


if __name__== "__main__":
  main()
