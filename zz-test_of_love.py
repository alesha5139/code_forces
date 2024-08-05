for _ in range(int(input())):
    length,jump,swim = map(int,input().split())
    river = "B"+input()
    cont = True
    success = "NO"

    while cont:
        #print(river)
        length = len(river)
        current = river[0]
        if (length <= 1 and swim >= 1) or ((current == "B" or current == "L") and length <= jump):
            cont = False
            success = "YES"
        else:
            if (current == "B" or current == "L"):
                #print('JUMP')
                reach = river[jump:0:-1]
                try:
                    l_index = reach.index("L")
                except:
                    l_index = None
                if l_index != None:
                    dest = len(reach) - l_index
                    river = river[dest:]
                else:
                    try:
                        w_index = reach.index("W")
                    except:
                        w_index = None
                    if w_index != None:
                        dest = len(reach) - w_index
                        river = river[dest:]
                    else:
                        cont = False
            else:
                if swim == 0:
                    cont = False
                elif river[1] == "C":
                    #print("CROC")
                    cont = False
                else:
                    #print("SWIM")
                    swim -= 1
                    river = river[1:]



    print(success)    