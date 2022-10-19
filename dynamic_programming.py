class Dynamic_programming:
    def __init__(self, price_per_len_arr, len_per_slice_arr, knapsack_val_arr, knapsack_wt_arr, W, grid):
        self.price_per_len_arr = price_per_len_arr
        self.len_per_slice_arr = len_per_slice_arr
        self.knapsack_val_arr = knapsack_val_arr
        self.knapsack_wt_arr = knapsack_wt_arr
        self.knapsack_W = W
        self.grid = grid


    def rod_cut_rec_ext_2(self, len_of_rod_int_2):
        profit_c = 0
        for k in range(0, len_of_rod_int_2, 1):
            c = self.rod_cut_rec_ext_**(k) + self.price_per_len_arr[self.len_per_slice_arr.index(len_of_rod_int_2- k)]
            profit_b = max(c, profit_c)


    def rod_cut_rec_ext_1(self, len_of_rod_int_1):
        profit_b = 0
        for j in range(0, len_of_rod_int_1, 1):
            b = self.rod_cut_rec_ext_2(j) + self.price_per_len_arr[self.len_per_slice_arr.index(len_of_rod_int_1- j)]
            profit_b = max(b, profit_b)


    def rod_cut_rec(self, len_of_rod_int):
        if len_of_rod_int ==0:
            return 0
    
        profit = 0
        for i in range(0, len_of_rod_int, 1):
            print('p(',i,')+ Vopt', len_of_rod_int- i)
            a = self.rod_cut_rec(i) + self.price_per_len_arr[self.len_per_slice_arr.index(len_of_rod_int- i)]
            profit = max(profit, a)
        return profit

##############################################################################################
##############################################################################################
##############################################################################################

    def knap_ext_2(self, wt_avail_int_1, j):
        profit_c = 0
        for l in range(j, len(self.knapsack_val_arr), 1):
            if self.knapsack_wt_arr[k] <= wt_avail_int_1:
                c = self.knap_ext_**(wt_avail_int_1 - self.knapsack_wt_arr[l]) + self.knapsack_val_arr[l]
                profit_c(c, profit_c)
        return profit_c

    def knap_ext_1(self, wt_avail_int_1, j):
        profit_b = 0
        for k in range(j, len(self.knapsack_val_arr), 1):
            if self.knapsack_wt_arr[k] <= wt_avail_int_1:
                b = self.knap_ext_2(wt_avail_int_1 - self.knapsack_wt_arr[k], j+1) + self.knapsack_val_arr[k]
                profit_b(b, profit_b)
        return profit_b

    def knap(self, wt_avail_int, j):
        if wt_avail_int ==0:
            return 0
        profit = 0
        for i in range(j, len(self.knapsack_val_arr), 1):
            if self.knapsack_wt_arr[i] <= wt_avail_int:
                print('0: val of item(',i,'/', len(self.knapsack_val_arr),')+ Vopt (', wt_avail_int, ')kg', 'item val : ', self.knapsack_val_arr[i], 'profit :', profit)
                a = self.knap(wt_avail_int - self.knapsack_wt_arr[i], j+1) + self.knapsack_val_arr[i]
                profit = max(a, profit)
                print('1: val of item(',i,'/', len(self.knapsack_val_arr),')+ Vopt (', wt_avail_int - self.knapsack_wt_arr[i], ')kg', 'item val : ', self.knapsack_val_arr[i], 'profit :', profit)
        return profit

##############################################################################################
##############################################################################################
##############################################################################################

    def grid_path_ext_2(self, n, o, grid, ii, jj):

        num_of_paths = 0

        for k in range(1, 3, 1):
            if grid[n][o+1] == 1:
                self.grid_path_ext_**(self, n, o+1, grid)
            else:
                pass
            if grid[n+1][o] == 1:
                self.grid_path_ext_**(self, n+1, o, grid)
            else:
                pass
            if grid[n][o+1] == 0 and grid[n+1][o] == 0:
                if n == ii and o == jj:
                    num_of_paths = num_of_paths +1
                    return num_of_paths




    def grid_path_ext_1(self, l, m, grid, ii, jj, num_of_paths):

        num_of_paths =0
        for k in range(1, 3, 1):
            if grid[l][m+1] == 1:
                self.grid_path_ext_2(self, l, m+1, grid)
            else:
                pass
            if grid[l+1][m] == 1:
                self.grid_path_ext_2(self, l+1, m, grid)
            else:
                pass
            if grid[l][m+1] == 0 and grid[l+1][m] == 0:
                if l == ii and l == jj:
                    num_of_paths = num_of_paths +1
                    return num_of_paths
            



    def grid_path(self, i, j, ii, jj, grid, num_of_paths):

        # for _ in range(1, 3, 1):
        print('0: (', i, ',',j,')', '{d:', grid[i+1][j], ', r:', grid[i][j+1], '}', 'num_of_paths :', num_of_paths)
        if grid[i][j+1] == 1:
            # print(i, j+1, grid[i][j+1])
            num_of_paths = self.grid_path(i, j+1, ii, jj, grid, num_of_paths)
            print('1: (', i, ',',j,')', '{d:', grid[i+1][j], ', r:', grid[i][j+1], '}', 'num_of_paths :', num_of_paths)

        if grid[i+1][j] == 1:
            num_of_paths = self.grid_path(i+1, j, ii, jj, grid, num_of_paths)
            print('2: (', i, ',',j,')', '{d:', grid[i+1][j], ', r:', grid[i][j+1], '}', 'num_of_paths :', num_of_paths)


        if grid[i][j+1] == 0 and grid[i+1][j] == 0:
            if i == ii and j == jj: 
                num_of_paths = num_of_paths +1
                print("num_of_paths :", num_of_paths)
                return num_of_paths
        return num_of_paths
    

test = Dynamic_programming([1.5, 5.2, 8.6, 10.7, 10.8, 11.2, 11.6, 20.2, 24.0, 30.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [60, 100, 120], [10, 20, 30], 50, [[1, 1, 1, 1],[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

# a = test.grid_path(0, 0, 4, 4, [[1, 1], [1, 1]])
a = test.grid_path(0, 0, 3, 3, [[1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]], 0)