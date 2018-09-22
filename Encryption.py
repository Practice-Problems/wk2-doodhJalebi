import math

print("Input string:",end=' ')
string = input().replace(" ","")
strlen = len(string)
#print("DEBUG    String length:",strlen)

rows = math.floor(math.sqrt(strlen))
cols = math.ceil(math.sqrt(strlen))
#print("DEBUG    rows = ",rows,"cols = ",cols)

def validity(rows, cols, len):
    if(rows*cols>=len):
        return True
    else:
        return False

while(validity(rows,cols,strlen)==False):
    rows = rows + 1

#---------------------------------------------------------------------------------------------------
# Now we have the dimensions of the "array".
# Now we go through the entire string and chop it up into slices, each the size of the column width.
# --------------------------------------------------------------------------------------------------
seg = []
def slicer(s, x):
    i=0
    while i+x <=len(s):
        seg.append(s[i:i+x])
        i = i + x
    if(i < len(string)):
        seg.append(string[i:])
slicer(string,cols)
#print(seg)
temp = ""

enc = []

for character in range(cols):
    for slice_number in range(rows):

        if(character+1 <= len(seg[slice_number])):

           temp = temp + seg[slice_number][character]
            #print("DEBUG   ",slice_number,character,seg[slice_number][character])
    enc.append(temp)
    temp = ""
#print(enc)

for a in range(len(enc)):
    print(enc[a],end=" ")