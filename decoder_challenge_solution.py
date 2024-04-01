# Decode Function
# Input     -> a Coded Text File into the Function Parameter
# Output    -> String with the Decoded Message

# The input in this example is a coded text file named "encoded_message.txt" in the same directory than this Python File

# The decode function sets a File Variable -Only-Read and Text Mode- and open the file to extract every line into an array excluding
# the CarryReturn '\n'. Once with all the lines in the array, the function order the array using the number and cut the numbers,
# leaving in the array only the ordered words. After that I reused the base of the Pyramid of Words code (Excercise 5) just to put
# the words in a Pyramid, but I modified the function to get only the last word of every line. That words I re-storaged them in the
# same array. At the end, the only thing left was to concatenate the words inserting spaces " " between them.


# Sort Function for List
def myFuncSort(e):
   # Find a space in the line to extract the integer index
   space = e.find(" ")
   index = e[:space]
   return int(index)


# Piramid of Words Function, the base of the SRC is taken and reused from DataAnnotation.tech from the previous exercise (Question 5)
# and modified to return the last ocurrencies of each sublist
def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[step-1])
      nums = nums[step:]
      step += 1
    else:
      return False
  return subsets



# Decoding Function
def decode(message_file):
    
    # Sets the File Variable, Only-Read and Text Mode
    encoded_file = open(message_file, 'rt')

    # Array of Lines of the File, set in new List lines and excludes '\n'
    lines = []
    for line in encoded_file:
        lines.append(line[:-1])
    
    # Order the array of lines using the first number of each line
    lines.sort(key=myFuncSort)

    # Once ordered, I extract the number in the begining of each word
    for x in range(len(lines)):
        aux = lines[x].find(" ") + 1
        lines[x] = lines[x][aux:]

    # Call Pyramid of Words (previous function) and Take the last word of each line in same variable 'lines'
    lines = create_staircase(lines)

    # Initialize decoded message variable
    decoded_message = ""

    # Concatenate of every word setting a space in the middle of words
    for x in range(len(lines)):
       decoded_message += (lines[x])
       if x < (len(lines)-1):
          decoded_message += " "

    return decoded_message

# Call Function
decode('./encoded_message.txt')
