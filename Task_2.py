# 2 . A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array of N number of integer values. The task is to find the empty packets(0) chocolate and push it to the end of the conveyor belt(array).

def push_empty_packets(chocolate_packets):
    non_empty_packets = []
    empty_packets = []
    for packet in chocolate_packets:
        if packet != 0:
            non_empty_packets.append(packet)
        else :
            empty_packets.append(packet)
    return non_empty_packets + empty_packets

input_string = input("Enter the list of element with spaces: ")
input_list = input_string.split()
chocolate_packets = [int(num) for num in input_list]
print(chocolate_packets)
result = push_empty_packets(chocolate_packets)
print(result)