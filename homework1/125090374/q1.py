#get the imput, save it as a str
num = input("Enter a binary number: ")

#0000: 0    0001: 1     0010: 2     0011: 3
#0100: 4    0101: 5     0110: 6     0111: 7
#1000: 8    1001: 9     1010: A     1011: B
#1100: C    1101: D     1110: E     1111: F

match len(num) % 4:
    case 1:
        num = "000" + num
    case 2:
        num = "00" + num
    case 3:
        num = "0" + num

hex_num = ""
for i in range(len(num) // 4):
    temp = num[4*i : 4 * i + 4]
    match temp:
        case "0000":
            hex_num = hex_num + "0"
        case "0001":
            hex_num = hex_num + "1"
        case "0010":
            hex_num = hex_num + "2"
        case "0011":
            hex_num = hex_num + "3"
        case "0100":
            hex_num = hex_num + "4"
        case "0101":
            hex_num = hex_num + "5"
        case "0110":
            hex_num = hex_num +"6"
        case "0111":
            hex_num = hex_num + "7"
        case "1000":
            hex_num = hex_num + "8"
        case "1001":
            hex_num = hex_num +"9"
        case "1010":
            hex_num = hex_num + "A"
        case "1011":
            hex_num = hex_num +"B"
        case "1100":
            hex_num = hex_num + "C"
        case "1101":
            hex_num = hex_num +"D"
        case "1110":
            hex_num = hex_num + "E"
        case "1111":
            hex_num = hex_num +"F"

print(hex_num)