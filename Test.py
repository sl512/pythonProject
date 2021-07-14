print('Hello test')

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    def step_function(x):
        y = x > 0
        return y.astype(np.int)

is_one=lambda x: x==1
add = lambda x,y: x+y
is_str = lambda x: 'a string' if isinstance(x, str) else None

if __name__ == '__main__':
    print (is_one(2))
    print (add (1,2))


    l = [1,2,3]
    l2= [4,5,6]
    print(dir(l))
    print(list(map(is_one, l)))
    print(list(filter(is_one, l)))
    print(list(map(add,l,l2)))

    print(is_str('shanshan'))
    print(is_str(1))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


