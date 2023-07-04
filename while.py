from datetime import datetime

datetime.now().second

wait_until = datetime.now().second + 2
#while datetime.now().second != wait_until:
#    pass

#print(f"we are at {wait_until} seconds!")

#while True:
#    if datetime.now().second == wait_until:
#        print(f"we are at {wait_until} seconds!")
#        break

#while True:
#    while datetime.now().second == wait_until:
#        print(f"we are at {wait_until} seconds!")
#        break

#while datetime.now().second != wait_until:
#    continue
#    print("Still Waiting!")


#print(f"we are at {wait_until} seconds!")


while True:
    if datetime.now().second < wait_until:
        continue
    break

print(f"we are at {wait_until} seconds!")
