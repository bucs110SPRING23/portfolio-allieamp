def main():
    filename = "exercises/ideas.txt"
    fptr = open(filename, "r")
    accumulator = 0
    for ch in fptr.read():
        if ch.isalnum():
            accumulator += 1
    fptr.close()

    fptr = open(filename+".dat", "w") #creates new file so we're not writing over the other
    fptr.write(str(accumulator) + " characters")
    fptr.close()

main()