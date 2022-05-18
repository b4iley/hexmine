def row(y):
        num = 1
        for i in range (4):
            row = []
            x = 76
            for i in range (9):
                xy = str(x) + ',' + str(y)
                type(xy)
                co = str(xy)
                row.append(co)
                x = x + 55
                num = num + 1
                    
                        
            print (row)
        return row