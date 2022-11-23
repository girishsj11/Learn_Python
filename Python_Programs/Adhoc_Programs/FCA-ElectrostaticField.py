'''

Electrostatic Field-

Doug is fond of change, every now and then he tries to do new things. This time, he caught up with a rod comprising of negative (N) and positive (P) charges. He is asked to calculate the maximum net electrostatic field possible in the region due to the rod.
Note: Assume Electrostatic Field = Total charge * 100

Input specification:
Input 1: Integer array denoting the magnitude of each charge.
Input 2: String denoting nature of each charge ith represents a sign of charge at ithentry represents a sign of charge at ith location in input1
Input 3: No of charges it holds (length of input1)

Output Specification:
Return the next maximum electrostatic field possible in the rod.

Example 1:
Input 1: {4,3,5}
Input 2: PNP
Input 3: 3
Output: 600
Explanation:
The maximum electric charge on the rod is 4-3+5 = 6 units. So the magnitude of the electric field would be 6*100=600

Example 2:
Input 1: {2,3}
Input 2: PN
Input 3: 2
Output : 100
Explanation:
The maximum possible electric charge on the section of the rod is 2-3=-1 unit.

'''

def Electrostatic_Field(input1,input2,input3):
    result = 0
    if (input3==len(input1) and input3==len(input2)):
        for i in range(input3):
            if(input2[i]=='P'):
                result = result+input1[i]
            else:
                result = result-input1[i]
                
        return abs(result*100)
    else:
        return "Mismatch in Lengths of both inputs - 1 & 2"
        


if __name__ == "__main__":
    input1 = list(map(int, input().split()))
    input2 = input()
    input3 = len(input1)
    print(Electrostatic_Field(input1, input2, input3))

