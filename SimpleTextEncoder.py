class ROOT:
    def __init__(self):
        # User Prompt
        self.user = input("Enter Your Text: ")
        
    ## Hash and encoder function
    def gloomyHash(self, password):
        # Variables to define the order index of alphabetic letters, numeric digits, and special characters
        order_lower = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
            'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
            'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }
        order_upper = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
            'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
            'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
        }
        order_puncs = {"!": 1,"#": 2,"$": 3,"%": 4,"&": 5,"*": 6,"+": 7,",": 8,"-": 9,".": 10,"/": 11,";": 12,"<": 13,
                       "=": 14,">": 15,"?": 16,"@": 17,"[": 18,"]": 19,"^": 20,"_": 21,"`": 23,"{": 24,"}":25,
                       "|": 26,"~": 27}
        
        result = ""  # Initialize an empty string to store the results
        
        try:
            for char in password:
                if char.islower():
                    res_low = order_lower[char]
                    result += str(res_low)  # Append the result to the existing string
                    
                elif char.isupper():
                    res_hi = order_upper[char]
                    result += str(res_hi)
                
                elif char in order_puncs:
                    res_pun = order_puncs[char]
                    result += str(res_pun)
                    
            print(f"The Encoded Text Is: {result}")  # Print the concatenated results
            
        except Exception as e:
            print(f"We Have The Error Of : {str(e)}")

    ## Func User Prompt Runner
    def run(self):
        self.gloomyHash(self.user)

if __name__ == "__main__":
    RUN = ROOT()
    RUN.run()