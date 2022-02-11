#generating the fibonaci series for n number terms

def fibonaci(num):
    fibonaci_series = [0,1]
    for i in range(2,num):
        fibonaci_series.append(fibonaci_series[i-2]+fibonaci_series[i-1])
    
    print(fibonaci_series)

if __name__ == "__main__":
    fibonaci(5) #output [0, 1, 1, 2, 3]
    fibonaci(8) #output [0, 1, 1, 2, 3, 5, 8, 13]
