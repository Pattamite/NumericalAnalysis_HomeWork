import copy
import math

def main():
    # Problem 1 #
    p1_a_a = [[3, -1, 1],
                [3, 6, 2],
                [3, 3, 7]]
    p1_a_b = [1, 0, 4]
    p1_a_ans = solve_matrix_jacobi(3, p1_a_a, p1_a_b)
    print("Problem 1 a: " + str(p1_a_ans) + "t")

    p1_b_a = [[10, -1, 0],
                [-1, 10, -2],
                [0, -2, 10]]
    p1_b_b = [9, 7, 6]
    p1_b_ans = solve_matrix_jacobi(3, p1_b_a, p1_b_b)
    print("Problem 1 b: " + str(p1_b_ans) + "t")

    p1_c_a = [[10, 5, 0, 0],
                [5, 10, -4, 0],
                [0, -4, 8, -1],
                [0, 0, -1, 5]]
    p1_c_b = [6, 25, -11, -11]
    p1_c_ans = solve_matrix_jacobi(4, p1_c_a, p1_c_b)
    print("Problem 1 c: " + str(p1_c_ans) + "t")

    p1_d_a = [[4, 1, 1, 0, 1],
                [-1, -3, 1, 1, 0],
                [2, 1, 5, -1, -1],
                [-1, -1, -1, 4, 0],
                [0, 2, -1, 1, 4]]
    p1_d_b = [6, 6, 6, 6, 6]
    p1_d_ans = solve_matrix_jacobi(5, p1_d_a, p1_d_b)
    print("Problem 1 d: " + str(p1_d_ans) + "t")

    # Problem 3 #
    p3_a_ans = solve_matrix_gauss_seidel(3, p1_a_a, p1_a_b)
    print("Problem 3 a: " + str(p3_a_ans) + "t")

    p3_b_ans = solve_matrix_gauss_seidel(3, p1_b_a, p1_b_b)
    print("Problem 3 b: " + str(p3_b_ans) + "t")

    p3_c_ans = solve_matrix_gauss_seidel(4, p1_c_a, p1_c_b)
    print("Problem 3 c: " + str(p3_c_ans) + "t")
    
    p3_d_ans = solve_matrix_gauss_seidel(5, p1_d_a, p1_d_b)
    print("Problem 3 d: " + str(p3_d_ans) + "t")

    # Problem 17 #
    p17_a = [[2, -1, 1],
                [2, 2, 2],
                [-1, -1, 2]]
    p17_b = [-1, 4, -5]
    p17_b_ans = solve_matrix_jacobi(3, p17_a, p17_b, 25)
    print("Problem 17 b: " + str(p17_b_ans) + "t")

    p17_d_ans = solve_matrix_gauss_seidel(3, p17_a, p17_b, 1000, 0.00001)
    print("Problem 17 d: " + str(p17_d_ans) + "t")

    # Problem 3 #
    pp3_a = [[1, 1/2, 1/3],
                [1/2, 1/3, 1/4],
                [1/3, 1/4, 1/5]]
    pp3_b = [5/6, 5/12, 17/60]
    pp3_a_ans = solve_matrix_gaussian(3, pp3_a, pp3_b)
    pp3_a_ans_round = [ round(elem, 3) for elem in pp3_a_ans ]
    print("Problem 3 a: " + str(pp3_a_ans_round) + "t")

    pp3_b_ans = solve_matrix_conjugate(3, pp3_a, pp3_b, 2)
    print("Problem 3 b: " + str(pp3_b_ans) + "t")

    pp11_a = [[4,-1,0,0,-1,0,0,0,0,0,0,0,0,0,0,0],
                [-1,4,-1,0,0,-1,0,0,0,0,0,0,0,0,0,0],
                [0,-1,4,-1,0,0,-1,0,0,0,0,0,0,0,0,0],
                [0,0,-1,4,0,0,0,-1,0,0,0,0,0,0,0,0],
                [-1,0,0,0,4,-1,0,0,-1,0,0,0,0,0,0,0],
                [0,-1,0,0,-1,4,-1,0,0,-1,0,0,0,0,0,0],
                [0,0,-1,0,0,-1,4,-1,0,0,-1,0,0,0,0,0],
                [0,0,0,-1,0,0,-1,4,0,0,0,-1,0,0,0,0],
                [0,0,0,0,-1,0,0,0,4,-1,0,0,-1,0,0,0],
                [0,0,0,0,0,-1,0,0,-1,4,-1,0,0,-1,0,0],
                [0,0,0,0,0,0,-1,0,0,-1,4,-1,0,0,-1,0],
                [0,0,0,0,0,0,0,-1,0,0,-1,4,0,0,0,-1],
                [0,0,0,0,0,0,0,0,-1,0,0,0,4,-1,0,0],
                [0,0,0,0,0,0,0,0,0,-1,0,0,-1,4,-1,0],
                [0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,4,-1],
                [0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,4]]
    pp11_b = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6]
    print("Problem 11 a: ")
    pp11_a_ans = solve_matrix_conjugate(16, pp11_a, pp11_b, 10, 0.05)
    print(str(pp11_a_ans) + "t")

    pp11_c = [[0 for x in range(16)] for y in range(16)] 
    for i in range(16):
        pp11_c[i][i] = 1/(pp11_a[i][i] ** 0.5)
    print("Problem 11 b: ")
    pp11_b_ans = solve_matrix_preconditioned_conjugate(16, pp11_a, pp11_b, pp11_c, 10, 0.05)
    print(str(pp11_b_ans) + "t")


def solve_matrix_jacobi(size, matrix_a, matrix_b, max_iter = 2, tol = 0):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    ans = [0] * size
    x = [0] * size
    max_error = 0
    current_error = 0

    for current_iter in range(max_iter):
        for i in range(size):
            ans[i] = b[i]
            for j in range(size):
                if j != i:
                    ans[i] -= a[i][j] * x[j]
            ans[i] /= a[i][i]
        
        max_error = abs(ans[0] - x[0])
        for i in range(size):
            current_error = abs(ans[i] - x[i])
            if current_error > max_error:
                max_error = current_error
        if max_error < tol:
            return ans

        x = copy.deepcopy(ans)
    
    return ans


def solve_matrix_gauss_seidel(size, matrix_a, matrix_b, max_iter = 2, tol = 0):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    ans = [0] * size
    x = [0] * size
    max_error = 0
    current_error = 0

    for current_iter in range(max_iter):
        for i in range(size):
            ans[i] = b[i]
            for j in range(i):
                ans[i] -= a[i][j] * ans[j]
            for j in range(i + 1, size):
                ans[i] -= a[i][j] * x[j]
            ans[i] /= a[i][i]
        
        max_error = abs(ans[0] - x[0])
        for i in range(size):
            current_error = abs(ans[i] - x[i])
            if current_error > max_error:
                max_error = current_error
        if max_error < tol:
            return ans

        x = copy.deepcopy(ans)
    
    return ans


def solve_matrix_gaussian(size, matrix_a, matrix_b):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    ans = [0] * size
    
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


def solve_matrix_conjugate(size, matrix_a, matrix_b, max_iter = 2, tol = 0):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    ans = [0] * size
    x = [0] * size
    r = copy.deepcopy(matrix_b)
    new_r = copy.deepcopy(matrix_b)
    p = copy.deepcopy(matrix_b)
    alpha = 0
    alpha_up = 0
    alpha_down  = 0
    beta = 0
    beta_up = 0
    beta_down = 0

    for current_iter in range(max_iter):
        alpha_up = 0
        alpha_down  = 0
        for i in range(size):
            alpha_up += r[i] ** 2
            temp = 0
            for j in range(size):
                temp += p[j] * a[j][i]
            alpha_down += temp * p[i]
        alpha = alpha_up / alpha_down 

        for i in range(size):
            ans[i] = x[i] + (alpha * p[i])
            temp = 0
            for j in range(size):
                temp += a[i][j] * p[j]
            new_r[i] = r[i] - (alpha * temp)
        
        if abs(max(r, key=abs)) < tol:
            print(str(current_iter + 1) + " iterations")
            return ans
        
        beta_up = 0
        beta_down = 0
        for i in range(size):
            beta_up += new_r[i] ** 2
            beta_down += r[i] ** 2
        beta = beta_up / beta_down

        for i in range(size):
            p[i] = new_r[i] + (beta * p[i])

        x = copy.deepcopy(ans)
        r = copy.deepcopy(new_r)
    
    return ans


def solve_matrix_preconditioned_conjugate(size, matrix_a, matrix_b, matrix_c, max_iter = 2, tol = 0):
    a = copy.deepcopy(matrix_a)
    b = copy.deepcopy(matrix_b)
    c = copy.deepcopy(matrix_c)
    ans = [0] * size
    r = copy.deepcopy(matrix_b)
    w = [0] * size
    v = [0] * size
    alpha = 0
    beta = 0
    u = [0] * size
    t = 0
    s = 0

    for i in range(size):
        for j in range(size):
            w[i] += c[i][j] * r[j]
   
    for i in range(size):
        for j in range(size):
            v[i] += c[j][i] * w[j]
    
    for i in range(size):
        alpha += w[i] ** 2

    for current_iter in range(max_iter):
        u = [0] * size
        for i in range(size):
            for j in range(size):
                u[i] += a[i][j] * v[j]
        
        t = 0
        for i in range(size):
            t += v[i] * u[i]
        t = alpha / t

        beta = 0
        for i in range(size):
            ans[i] += t * v[i]
            r[i] -= t * u[i]
            w = [0] * size
            for j in range(size):
                w[i] += c[i][j] * r[j]
            beta += w[i] ** 2

        if abs(beta) < tol and abs(max(r, key=abs)) < tol:
            print(str(current_iter + 1) + " iterations")
            return ans

        s = beta / alpha
        print(s)
        for i in range(size):
            v[i] = s * v[i]
            for j in range(size):
                v[i] += c[j][i] * w[j]
        alpha = beta

    return ans

main()
