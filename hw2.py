k_idx = (3, 3)
p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)}
move = [(k_idx)]
movedone = [(k_idx)]
index = False

valid = [(k_idx[0]+2, k_idx[1]+1), (k_idx[0]+2, k_idx[1]-1), (k_idx[0]-2, k_idx[1]+1), (k_idx[0]-2, k_idx[1]-1), (k_idx[0]+1, k_idx[1]+2), (k_idx[0]+1, k_idx[1]-2), (k_idx[0]-1, k_idx[1]+2), (k_idx[0]-1, k_idx[1]-2)]




while len(p_idxs) >= len(move):

    for i in p_idxs:
        for z in valid:
            index = False
            for k in move:
                if z==i and k == z and index == False:
                    index = True
                elif z==i and k==z and index == True:
                    move.remove(k)
                    index = False

            if z == i and index == False:
                move.append(z)
                k_idx = z
                valid = [(k_idx[0] + 2, k_idx[1] + 1), (k_idx[0] + 2, k_idx[1] - 1), (k_idx[0] - 2, k_idx[1] + 1), (k_idx[0] - 2, k_idx[1] - 1), (k_idx[0] + 1, k_idx[1] + 2), (k_idx[0] + 1, k_idx[1] - 2), (k_idx[0] - 1, k_idx[1] + 2), (k_idx[0] - 1, k_idx[1] - 2)]


print(move)
print('order of moves needed to capture all pawns:')
for i in move:
    print(i, end=' ')







