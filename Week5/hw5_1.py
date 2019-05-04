import copy
import math

def main():
    # Problem 5 #
    x = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
    y = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 229.50, 326.72]

    p5a_a = [[len(x), sum(x)], 
        [sum(x), sum([i**2.0 for i in x])]]
    p5a_b = [sum(y), sum([a*b for a,b in zip(x,y)])]
    p5a_ans = solve_matrix(2, p5a_a, p5a_b)
    p5a_error = 0
    for i in range(len(x)):
        p5a_error += ((p5a_ans[0] + (x[i] * p5a_ans[1])) - y[i] ) ** 2
    p5a_error **= 0.5
    print('Problem 5 a : ({0:.5f}) + ({1:.5f})x -> error : {2:.5f}'.format(p5a_ans[0], p5a_ans[1], p5a_error))


    p5b_a = [[len(x), sum(x), sum([i**2.0 for i in x])], 
        [sum(x), sum([i**2.0 for i in x]), sum([i**3.0 for i in x])],
        [sum([i**2.0 for i in x]), sum([i**3.0 for i in x]), sum([i**4.0 for i in x])]]
    p5b_b = [sum(y), sum([a*b for a,b in zip(x,y)]), sum([(a**2)*b for a,b in zip(x,y)])]
    p5b_ans = solve_matrix(3, p5b_a, p5b_b)
    p5b_error = 0
    for i in range(len(x)):
        p5b_error += ((p5b_ans[0] + (x[i] * p5b_ans[1]) + ((x[i] ** 2) * p5b_ans[2])) - y[i] ) ** 2
    p5b_error **= 0.5
    print('Problem 5 b : ({0:.5f}) + ({1:.5f})x + ({2:.5f})x^2 -> error : {3:.5f}'.format(p5b_ans[0], p5b_ans[1], p5b_ans[2], p5b_error))


    p5c_a = [[len(x), sum(x), sum([i**2.0 for i in x]), sum([i**3.0 for i in x])], 
        [sum(x), sum([i**2.0 for i in x]), sum([i**3.0 for i in x]), sum([i**4.0 for i in x])],
        [sum([i**2.0 for i in x]), sum([i**3.0 for i in x]), sum([i**4.0 for i in x]), sum([i**5.0 for i in x])],
        [sum([i**3.0 for i in x]), sum([i**4.0 for i in x]), sum([i**5.0 for i in x]), sum([i**6.0 for i in x])]]
    p5c_b = [sum(y), sum([a*b for a,b in zip(x,y)]), sum([(a**2)*b for a,b in zip(x,y)]), sum([(a**3)*b for a,b in zip(x,y)])]
    p5c_ans = solve_matrix(4, p5c_a, p5c_b)
    p5c_error = 0
    for i in range(len(x)):
        p5c_error += ((p5c_ans[0] + (x[i] * p5c_ans[1]) + ((x[i] ** 2) * p5c_ans[2]) + ((x[i] ** 3) * p5c_ans[3])) - y[i] ) ** 2
    p5c_error **= 0.5
    print('Problem 5 c : ({0:.5f}) + ({1:.5f})x + ({2:.5f})x^2 + ({3:.5f})x^3 -> error : {4:.5f}'.format(p5c_ans[0],
         p5c_ans[1], p5c_ans[2], p5c_ans[3], p5c_error))


    p5d_y = copy.deepcopy(y)
    for i in range(len(p5d_y)):
        p5d_y[i] = math.log(p5d_y[i])
    p5d_a = [[len(x), sum(x)], 
        [sum(x), sum([i**2.0 for i in x])]]
    p5d_b = [sum(p5d_y), sum([a*b for a,b in zip(x,p5d_y)])]
    p5d_ans = solve_matrix(2, p5d_a, p5d_b)
    p5d_ans[0] = math.exp(p5d_ans[0])
    p5d_error = 0
    for i in range(len(x)):
        p5d_error += ((p5d_ans[0] * math.exp(p5d_ans[1] * x[i])) - y[i] ) ** 2
    p5d_error **= 0.5
    print('Problem 5 d : ({0:.5f}) * (e ^ (({1:.5f})x) -> error : {2:.5f}'.format(p5d_ans[0], p5d_ans[1], p5d_error))


    p5e_x = copy.deepcopy(x)
    for i in range(len(p5e_x)):
        p5e_x[i] = math.log(p5e_x[i])
    p5e_y = copy.deepcopy(y)
    for i in range(len(p5e_y)):
        p5e_y[i] = math.log(p5e_y[i])
    p5e_a = [[len(p5e_x), sum(p5e_x)], 
        [sum(p5e_x), sum([i**2.0 for i in p5e_x])]]
    p5e_b = [sum(p5e_y), sum([a*b for a,b in zip(p5e_x,p5e_y)])]
    p5e_ans = solve_matrix(2, p5e_a, p5e_b)
    p5e_ans[0] = math.exp(p5e_ans[0])
    p5e_error = 0
    for i in range(len(x)):
        p5e_error += ((p5e_ans[0] * (x[i] ** p5e_ans[1])) - y[i] ) ** 2
    p5e_error **= 0.5
    print('Problem 5 e : ({0:.5f}) * (x ^ ({1:.5f})) -> error : {2:.5f}'.format(p5e_ans[0], p5e_ans[1], p5e_error))

    # Problem 13 #
    w = [0.017, 0.087, 0.174, 1.11, 1.74, 4.09, 5.45, 5.96, 0.025, 0.111,
        0.211, 0.999, 3.02, 4.28, 4.58, 4.68, 0.020, 0.085, 0.171, 1.29, 
        3.04, 4.29, 5.30, 0.020, 0.119, 0.210, 1.32, 3.34, 5.48, 0.025, 
        0.233, 0.783, 1.35, 1.69, 2.75, 4.83, 5.53]
    r = [0.154, 0.296, 0.363, 0.531, 2.23, 3.58, 3.52, 2.40, 0.23, 0.357, 
        0.366, 0.771, 2.01, 3.28, 2.96, 5.10, 0.181, 0.260, 0.334, 0.87, 
        3.59, 3.40, 3.88, 0.180, 0.299, 0.428, 1.15, 2.83, 4.15, 0.234, 
        0.537, 1.47, 2.48, 1.44, 1.84, 4.66, 6.94]

    p13a_w = copy.deepcopy(w)
    for i in range(len(p13a_w)):
        p13a_w[i] = math.log(p13a_w[i])
    p13a_r = copy.deepcopy(r)
    for i in range(len(p13a_r)):
        p13a_r[i] = math.log(p13a_r[i])
    p13a_a = [[len(p13a_w), sum(p13a_w)], 
        [sum(p13a_w), sum([i**2.0 for i in p13a_w])]]
    p13a_b = [sum(p13a_r), sum([a*b for a,b in zip(p13a_w,p13a_r)])]
    p13a_ans = solve_matrix(2, p13a_a, p13a_b)
    p13a_ans[0] = math.exp(p13a_ans[0])
    print('Problem 13 a : ({0:.5f}) * (w ^ ({1:.5f}))'.format(p13a_ans[0], p13a_ans[1]))


    p13b_error = 0
    for i in range(len(w)):
        p13b_error += ((p13a_ans[0] * (w[i] ** p13a_ans[1])) - r[i] ) ** 2
    print('Problem 13 b : error : {0:.5f}'.format(p13b_error))


    p13c_w = copy.deepcopy(w)
    for i in range(len(p13c_w)):
        p13c_w[i] = math.log(p13c_w[i])
    p13c_r = copy.deepcopy(r)
    for i in range(len(p13c_r)):
        p13c_r[i] = math.log(p13c_r[i])
    p13c_a = [[len(p13c_w), sum(p13c_w), sum([i**2.0 for i in p13c_w])], 
        [sum(p13c_w), sum([i**2.0 for i in p13c_w]), sum([i**3.0 for i in p13c_w])],
        [sum([i**2.0 for i in p13c_w]), sum([i**3.0 for i in p13c_w]), sum([i**4.0 for i in p13c_w])]]
    p13c_b = [sum(p13c_r), sum([a*b for a,b in zip(p13c_w,p13c_r)]), sum([(a**2.0)*b for a,b in zip(p13c_w,p13c_r)])]
    p13c_ans = solve_matrix(3, p13c_a, p13c_b)
    p13c_ans[0] = math.exp(p13c_ans[0])
    print('Problem 13 a : ({0:.5f}) * (w ^ ({1:.5f})) * (e ^ (({2:.5f}) * (ln(W) ^ 2)))'.format(p13c_ans[0], p13c_ans[1], p13c_ans[2]))

    p13d_error = 0
    for i in range(len(w)):
        p13d_error += ((p13c_ans[0] * (w[i] ** p13c_ans[1]) * math.exp(p13c_ans[2] * (math.log(w[i]) ** 2) ) ) - r[i] ) ** 2
    print('Problem 13 b : error : {0:.5f}'.format(p13d_error))
    

def solve_matrix(size, matrix_a, matrix_b):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    ans = [0] * size
    x = [0] * size
    is_done = False
    
    for i in range(size):
        min_value = abs(a[i][i])
        min_index = i
        
        for j in range(i + 1, size):
            if abs(a[j][i]) < min_value and a[j][i] != 0:
                min_value = abs(a[j][i])
                min_index = j
    
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            b[i], b[min_index] = b[min_index], b[i]

        if a[i][i] == 0:
            print("solve_matrix Fail")
            return ans

        for j in range(i + 1, size):
            m = a[j][i] / a[i][i]
            for k in range(size):
                a[j][k] -= (m * a[i][k])
            b[j] -= (m * b[i])

    if a[size - 1][size - 1] == 0:
        print("solve_matrix Fail")
        return ans
    
    ans[size - 1] = b[size - 1] / a[size - 1][size - 1]

    for i in range(size - 2, -1, -1):
        ans[i] = b[i]
        for j in range(i + 1, size):
            ans[i] -= a[i][j] * ans[j]
        ans[i] /= a[i][i]

    return ans 

main()
