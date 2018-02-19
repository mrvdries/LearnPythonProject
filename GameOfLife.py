def toonGeneratie(matrix):
    for list in matrix:
        for i in list:
            if i:
                print('x ', end="", flush=True)
            else:
                print('o ', end="", flush=True)
        print("")

def aantalBuren(matrix, i, j):
    count = 0
    for x in range(max(i-1,0),i+2):
        for y in range(max(j-1,0),j+2):
            try:
                prev = count
                if matrix[x][y] and (x!=i or y!=j):
                    count+=1
            except IndexError:
                pass
    return count

def volgendeGeneratie(matrix):
    new_matrix = []
    for i in range(0,len(matrix)):
        new_row = []
        for j in range(0,len(matrix)):
            count = aantalBuren(matrix, i, j)
            if matrix[i][j]:
                if count==2 or count==3:
                    new_row.append(True)
                else:
                    new_row.append(False)
            else:
                if count==3:
                    new_row.append(True)
                else:
                    new_row.append(False)
        new_matrix.append(new_row)
    return new_matrix

# generatie = [[True] + [False] * 7 for _ in range(6)]
# toonGeneratie(generatie)
# print(aantalBuren(generatie, 0, 0))
# print(aantalBuren(generatie, 1, 1))
# print(aantalBuren(generatie, 2, 2))
# volgende = volgendeGeneratie(generatie)
# toonGeneratie(volgende)
# volgende = volgendeGeneratie(volgende)
# toonGeneratie(volgende)
# volgende = volgendeGeneratie(volgende)
# toonGeneratie(volgende)
# volgende = volgendeGeneratie(volgende)
# toonGeneratie(volgende)