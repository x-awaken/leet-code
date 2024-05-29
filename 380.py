'''
380. O(1) 时间插入、删除和获取随机元素
中等
相关标签
相关企业
实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

'''
import random
class RandomizedSet(object):

    def __init__(self):
        self.data = {}
        self.vals = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            self.data[val] = len(self.vals)
        else:
            return False
        self.vals.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        i =  self.data[val]
        self.vals[i] = self.vals[-1]
        self.data[self.vals[i]] = i
        self.vals.pop()
        del self.data[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        i = random.randint(0,len(self.vals)-1)
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:

methods = ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
params = [[],[0],[0],[0],[],[0],[0]]
for f,param in zip(methods,params):
    if f == "RandomizedSet":
        print("RandomizedSet")
        obj = RandomizedSet()
        ret = None
    elif f == 'insert':
        print("insert")
        ret = obj.insert(param[0])
    elif f == 'remove':
        print("remove")
        ret = obj.remove(param[0])
    elif f == 'getRandom':
        print("getRandom")
        ret = obj.getRandom()
    print('\t',ret)
    print('\t',obj.vals,obj.data)
