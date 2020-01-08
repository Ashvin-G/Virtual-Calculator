# Virtual-Calculator

### Description
Virtual Calculator is a calculator which will perform basic Arithmetic operation without keyboard intervention. All you have to do is place your finger(anything blue colored) on particular button display this will result in clicking corresponding button.

### Prerequisites
The Program is written in Python 3.7 and excludes two external Library for Image Processing.

1. OpenCV
2. Numpy

You can install these packages by following command.
```
$ pip install opencv-python
$ pip install numpy
```


### How does it Work?
The Video frames undergoes several image processing operation in order to detect blue colored object in particular region of interest.The user moves his finger(blue colored) to the corresponding number, by doing so the numbers are appended to number list. This calculator takes in first all the operand i.e. if you want to add 5 + 7 you need to hover your finger above 5 first followed by 7 and finally + .The result will be appended to list.
You can clear the operand list by hovering on C button.

### Demo


# Future Work
This calculator is basic one, it only works with single digit number. Improvements such as ability to add any number of digits number and other improvements such as operand followed by operator and then operand can be implemented.
