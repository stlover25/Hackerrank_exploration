x = 0.12

firstcase = (1-x)**10 + 10*x*((1-x)**9) + 45*(x**2)*((1-x)**8)
secondcase = 1- (1-x)**10 - 10*x*((1-x)**9)

print("%.3f" %firstcase)
print("%.3f" %secondcase)
