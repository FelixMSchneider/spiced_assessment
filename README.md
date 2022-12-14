# Assessment
In the assessment you will implement a linear model for a set of 20 x/y data points.

We assume that the data can be described by a straight line with the slope a through the origin and an intercept b.

y = a * x + b

## Task 1
    Read the x/y data points from the file datapoints.csv into Python
## Task 2
    Create a scatterplot of the data.
## Task 3
    Set the slope a to 10 and the intercept b to 0. Calculate y for every value of x.
## Task 4

    Calculate the Mean Squared Error (MSE) of y and ytrue using the formula:
    MSE = 1/N∑(y−ytrue)2

## Task 5
    Find a value for a that gives the lowest possible MSE. Implement the following procedure:
        initially set a to 10
        repeat the following procedure 100 times:
            decrease a by 0.1
            re-calculate y using the modified a
            re-calculate the MSE
            check if the new MSE is smaller than the previous one
            if it is smaller, keep the new values for the MSE and a, otherwise discard it 
        print the final value for a and the corresponding MSE

## Task 6
    Also modify b in the above procedure.

## Task 7
    How could the algorithm be improved? Write down one or two ideas.

## Hints
        the implementation must be done in Python
        do not use any existing linear regression functions
        you may use pandas or numpy
        use any Python plotting library you like. Do not use Excel for plotting. 

