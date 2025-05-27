class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        total_sum = "0"

        for index2 in range(len(num2) - 1, -1 , -1):
            cur_sum = ""
            temp = 0

            for index1 in range(len(num1) - 1, -1 , -1):
                cur_multiple = int(num1[index1]) * int(num2[index2]) + temp
                temp = 0

                if cur_multiple >= 10:
                    temp = cur_multiple // 10
                    cur_multiple = cur_multiple % 10
                
                cur_sum = str(cur_multiple) + cur_sum
            
            if temp:
                cur_sum = str(temp) + cur_sum

            cur_sum = cur_sum + "0" * (len(num2) - index2 - 1)
            total_sum = self.sum(total_sum, cur_sum)

        return total_sum
        
    def sum(self, num1:str, num2: str) -> str:
        filled_num1 = num1.zfill(max(len(num1),len(num2)))
        filled_num2 = num2.zfill(max(len(num1),len(num2)))
        temp = 0
        total_sum = ""

        for index in range(len(filled_num1) - 1,  -1 , -1):
                cur_sum = int(filled_num1[index]) + int(filled_num2[index]) + temp
                temp = 0

                if cur_sum >= 10:
                    temp = cur_sum // 10
                    cur_sum = cur_sum % 10
                
                total_sum = str(cur_sum) + total_sum

        if temp:
            return str(temp) + total_sum
        
        return total_sum