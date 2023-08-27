class Solution:
    def numberOfShelves(self , N):
        # write code here
        min_row = 0
        max_row = N - 1

        min_col = 0
        max_col = N - 1

        cur_num = 1
        cur_col = 0
        cur_row = 0

        res = []
        for _ in range(N):
            res.append([0] * N)

        res[cur_row][cur_col] = cur_num

        while min_col < max_col and min_row < max_row:
            print(min_col, max_col, min_row, max_row)
            # 向下
            while cur_row < max_row - cur_col:
                cur_row += 1
                cur_num += 1
                res[cur_row][cur_col] = cur_num
            print(res)

            print(min_col, max_col, min_row, max_row)
            # 斜向上
            while cur_row > min_row and cur_col <= max_col - cur_row:
                cur_row -= 1
                cur_col += 1
                cur_num += 1
                res[cur_row][cur_col] = cur_num
            print(res)

            min_col += 1
            max_row -= 1

            print(min_col, max_col, min_row, max_row)
            # 向左
            while cur_col > min_col:
                cur_col -= 1
                cur_num += 1
                res[cur_row][cur_col] = cur_num
            max_col -= 1
            min_row += 1

            print(res)

        final_res = []
        for l in res:
            final_res.extend(l)
        final_res = [i for i in final_res if i != 0]
        return final_res

s = Solution()
res = s.numberOfShelves(5)
print(res)


        



