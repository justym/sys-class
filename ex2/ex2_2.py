def converter(text: str):
    lines = text.splitlines()
    nums = []
    for l in lines:
        num = int(l)
        nums.append(num)

    return nums

def addDigits(nums: list):
    result = 0
    for num in nums:
        result += num

    return result

def execution(src,dest):
    rf = open(src, 'r')
    text = rf.read()
    rf.close()
    nums = converter(text)
    result = addDigits(nums)
    wf = open(filename, 'w')
    wf.write(str(result) + '\n')
    wf.close()


in_name = './id.txt'
out_name = './result.txt'

execution(in_name,out_name)




    

 
    
