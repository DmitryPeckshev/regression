try:
    file_open = open('input.txt','r')
except IOError:
    print('File not found!')
    input()
    exit()
else:
    with file_open as inptxt:
        input_array = []
        n = 0
        for line in inptxt:
            arr_line = line.replace('\t', ' ').replace(',', '.').replace('\n', ' ')
            arr_line = arr_line.strip(' ')
            arr_line = arr_line.split(' ')
            i = 0
            while i < len(arr_line):   
                if arr_line[i] == ' ' or arr_line[i] == '':
                    del arr_line[i]
                else:
                    try:
                        arr_line[i] = float(arr_line[i])  
                    except:
                        print('there is no digit')
                        input()
                        exit()
                    i += 1
            if n>0 and n!=len(arr_line):  
                print("error: in input file length of rows not the same")
                input()
                exit()
            n = len(arr_line)
            input_array.append(arr_line)  
input("Input.txt open successfully! Press Enter.")

i = 0
sum_x = 0 
sum_y = 0
sum_xy = 0
sum_xsqr = 0

for dig in input_array[0]: 
    sum_x += dig 
    sum_y += input_array[1][i]
    sum_xy += dig*input_array[1][i]  
    sum_xsqr += dig*dig
    i += 1

x_vector = sum_x/n
y_vector = sum_y/n
xy_vector = sum_xy/n
xsqr_vector = sum_xsqr/n

a = (xy_vector-x_vector*y_vector)/(xsqr_vector-x_vector*x_vector)
b = (y_vector*xsqr_vector-x_vector*xy_vector)/(xsqr_vector-x_vector*x_vector)

equation = 'y = '+str(a)+' x + '+str(b)
file_write = open('output.txt', 'w')
file_write.write(equation)
file_write.close

param1 = 0
param2 = 0
i = 0
for dig in input_array[0]: 
    yp = a*dig + b
    param1 += (yp-y_vector)*(yp-y_vector)
    param2 += (input_array[1][i]-y_vector)*(input_array[1][i]-y_vector)
    i+=1

r = param1/param2

print(equation)	
print('Coefficient of determination:',round(r*100),'%')

print('All good!')
input()