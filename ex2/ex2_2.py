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

def execution(reader,filename):
    text = reader.read()
    nums = converter(text)
    result = addDigits(nums)
    wf = open(filename, 'w')
    wf.write(str(result) + '\n')


in_name = './id.txt'
out_name = './result.txt'

rf = open(in_name, 'r')
execution(rf,out_name)



    

 
    