def get_det_2x2(ary):
    a1, a2 = ary
    a, b = a1
    c, d = a2
    return (a * d) - (b * c)

def get_det_3x3(ary):
    a1, a2, a3 = ary
    a11, a12, a13 = a1
    a21, a22, a23 = a2
    a31, a32, a33 = a3
    return (a11 * a22 * a33) + (a21 * a32 * a13) + (a12 * a23 * a31) - (a31 * a22 * a13) - (a21 * a12 * a33) - (a32 * a23 * a11)

def get_ext_ary(ary, x, y):
    ext_ary = ary[:y] + ary[y+1:]
    for i in range(len(ary) - 1):
        ext_ary[i] = ext_ary[i][:x] + ext_ary[i][x+1:]
    return ext_ary

def get_det(ary):
    if len(ary) == 3:
        return get_det_3x3(ary)
    elif len(ary) == 2:
        return get_det_2x2(ary)
    elif len(ary) == 1:
        return ary[0][0]
    else:
        det = 0
        for y in range(len(ary)):
            det += ((-1)**y) * ary[y][0] * get_det(get_ext_ary(ary, 0, y))
        return det

if __name__ == "__main__":
    vec = [
        [3, 1, 2, 4, 5],
        [3, 0, 3, 2, 3],
        [1, 1, 5, 2, 3],
        [1, 2, 0, 5, 2],
        [4, 1, 3, 2, 1],
    ]
    print(get_det(vec))

