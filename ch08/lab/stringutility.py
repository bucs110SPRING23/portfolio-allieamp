import re
class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        """
        returns the internal string unchanged
        args: self [str] refers to StringUtility initialization
        return: self.string [str] the internal string
        """
        return self.string
    
    def vowels(self):
        """
        Counts the number of vowels in the string is less than 5
        args: self [str] refers to StringUtility initialization
        return: count [str] the number of vowels if less than 5, "many" if more than 5
        """
        count = 0
        for char in self.string:
            if char in "aeiouyAEIOUY":
                count = count + 1
        if count < 5:
            return str(count)
        else:
            return "many"
        
    def bothEnds(self):
        """
        Makes a string made of the first 2 and last 2 characters of the original string.
        args: self [str] refers to StringUtility initialization
        return: shrt_string [str] of the first and last two letters or empy string if there are less than 2 letters
        """
        if len(self.string) > 2:
                shrt_string = self.string[0]+self.string[1]+self.string[-2]+self.string[-1]
                return shrt_string
        else:
            return ""
        
    def fixStart(self):
        """
        Makes a string where all occurrences of the first letter are '*', for the first.
        args: self [str] refers to StringUtility initialization
        return: new_string [str] the orginal string replaces with the "*" or the original string or the unchanges string is 1 or less
        """
        if len(self.string) > 1:
            if len(self.string)>1:
                new_string = self.string[0]+re.sub(self.string[0],"*",self.string[1:])
            return new_string
        else:
            return self.string
        
    def asciiSum(self):
        """
        Sums up all theascii values in the string
        args: self [str] refers to StringUtility initialization
        return: acsii [int] the sum of the acsii values
        """
        ascii_sum = 0
        for char in self.string:
            ascii_sum += ord(char)
        return ascii_sum
    
    def cipher(self):
        """
        Encodes the string by incrementing all letters by the length of the string
        args: self [str] refers to StringUtility initialization
        return: result [str] the encoded string
        """
        result = ""
        shift = len(self.string)
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + shift) % 26
                char = chr(start + new_pos)
            result += char
        return result


