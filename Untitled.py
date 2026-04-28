def clear_and_print()
    for i in range(1,18):
        print("██████████████████████████████████████████████")

while True:
    move = input("Next Move")
    
    if move == "W" or "w":
        clear_and_print()
        print("w!!!")