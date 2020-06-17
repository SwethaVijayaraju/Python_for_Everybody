# Write code using find() and string slicing (see section 6.10) to extract the number at the end
# of the line below. Convert the extracted value to a floating point number and print it out.
# text = "X-DSPAM-Confidence:    0.8475";

text = input("Enter text:")
colon_pos = text.find(":")
str_num = text[colon_pos + 1:]
str_strip = str_num.strip()
try:
    float_num = float(str_strip)
except:
    print("Error - given input has no numbers or has invalid numbers")
    exit()
print(float_num)
