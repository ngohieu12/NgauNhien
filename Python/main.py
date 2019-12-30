import numpy as np
from input import Algorithms


def mainMenu ():
    print("********************* Quá trình quyết định Markov (MDP) *********************")
    print("1. Cải thiện chi phí có chiết ")
    print("2. Cải tiến chính sách theo tiêu chi tổng chi phí có chiết ")
    print("3. Cải tiến chính sách theo tiêu chí chi phí trung bình dài hạn")
    print("4. Thoát")
    selection = int(input("Lựa chọn: "))
    if selection == 1:
        method1()
    elif selection == 2:
        method2()
    elif selection == 3:
        method3()
    elif selection == 4:
        exit()
    else:
        print("pls chose menu")
        mainMenu()

def method1 ():
    test = Algorithms()
    a = test.ImprovementAlgorithm()
    for i in a['listV']:
       print("v=",i)
    print("a=",a['a'])
    mainMenu()

def method2 ():
    test = Algorithms()
    a=test.PolicyImprovementAlgorithm()
    for i in range(a['number']):
        print("\nBước lặp", i+1)
        print("a=",a['listA'][i])
        print("v=",a['listV'][i])
    mainMenu()

def method3 ():
    test = Algorithms()
    a=test.PolicyImprovementforAverageCosts()
    for i in range(a['number']):
        print("\nBước lặp", i+1)
        print("a=",a['listA'][i])
        print("h=",a['listH'][i])
        print("Phi=",a['listPhi'][i])
    mainMenu()

#main
mainMenu()