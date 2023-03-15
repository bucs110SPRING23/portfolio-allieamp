
def percentage_to_letter(score=0):
    """
    This is a function that returns a letter based on percentage
    args: score (float)
    return: letter (str)
    """
    if score >= 90:
        let = "A"
    elif score >= 80:
        let = "B"
    elif score >= 70:
        let = "C"
    elif score >= 60:
        let = "D"
    else:
        let = "F"
    return let
def is_passing(letter): #boolean function -> connvention to start with "is" or "has"
    """
    Boolean function to determine is letter grade is passing
    arg: letter(str)
    return: boolean
    """
    return letter in ["A", "B", "C"] #returns True or False
    
def main():
    score = float(input("Input grade percentage:"))
    letter = percentage_to_letter(score)
    if is_passing(letter): #checks if it is true
        print("You passed (:")
    else:
         print("You suck ):")

main()