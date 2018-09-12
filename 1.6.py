def compression(word):
    check = True
    final = []
    current = ""
    count =1
    for i in range(0,len(word)-1):
        current = word[i]
        if(current != word[i+1]):
            final.append(current)
            final.append(count)
            count = 1
        elif (current == word[i + 1]):
            check = False
            count += 1

    final.append(word[len(word)-1])
    final.append(count)
    if(check==True):
        print(word)
    else:
        print(final)



def main():
    compression("iiitttworkd")


if __name__== "__main__":
  main()