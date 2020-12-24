#
# @lc app=leetcode.cn id=1357 lang=python3
#
# [1357] 每隔 n 个顾客打折
#

# @lc code=start
import collections
class Cashier:
    count=0
    discount=0
    n=0
    d=collections.defaultdict()

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount=discount
        self.n=n
        self.d=dict(zip(products,prices))
        print (self.d)

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total=sum([self.d[p]*a for (p,a) in zip(product,amount)])
        # print (self.count)
        if self.count>=self.n-1:
            self.count=0
            return total*(100-self.discount)/100.0
        else:
            self.count+=1
            return total



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
# @lc code=end

