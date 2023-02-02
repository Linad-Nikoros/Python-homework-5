
txt= open('rle_input.txt', 'r' ,encoding='UTF-8')
input_data=txt.readline()
print(input_data)

def encode(data):
    encoding = "" 
    i = 0
    while i < len(data):    
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + data[i]
        i += 1
    return encoding


def decode(data): 
 decode = '' 
 count = '' 
 for char in data: 
   if char.isdigit(): 
     count += char 
   else: 
     decode += char * int(count) 
     count = '' 
 return decode


output_data = encode(input_data)
print(output_data)

with open('rle_output.txt', 'w', encoding='UTF-8') as RLE_output:
    RLE_output.write(f'{output_data}')
