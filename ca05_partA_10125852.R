# Data Analytics Group 1
# 10125852 InSun Ahn

# CA05 - PART A 
# Calculator Program


# Function 1 - compute summation of two values/vectors.
my_addition <- function(x,y) {
  x + y
}

# Function 2 - compute subtraction of two values/vectors.
my_subtraction <- function(x,y){
  x - y
}

# Function 3 - compute multiplication of two values/vectors.
my_multiplication <- function(x,y){
  x * y
}

# Function 4 - compute division of two values/vectors.
my_division <- function(x,y){
  x / y
}

# Function 5 - compute exponentiation(power) base = x, exponent = y
my_power <- function(x,y){
  x**y
}

# Function 6 - compute square root of a value/vector.
my_sqrt <- function(x){
  sqrt(x)
}

# Trigonometric Functions 7-9
## Function 7 - Sine
my_sin <- function(x){
  sin(x)
}
## Function 8 - Cosine
my_cos <- function(x){
  cos(x)
}
## Function 9 - Tangent
my_tan <- function(x){
  tan(x)
}

# Function 10 - Compute logarithms of a value/vector x and base = y. 
my_log <- function(x, y){
  logb(x, base = y)
}


a = 7
b = 5
c <- c(1, 2, 3, 4)
d <- c(5, 6, 7, 8)

my_addition(a, b)
my_addition(c, d)

my_subtraction(a, b)
my_subtraction(c, d)

my_multiplication(a, b)
my_multiplication(c, d)

my_division(a, b)
my_division(c, d)

my_power(a, b)
my_power(c, d)

my_sqrt(25)
my_sqrt(c)

my_sin(b)
my_sin(d)

my_cos(a)
my_cos(c)

my_tan(b)
my_tan(d)

my_log(100, base = 2)
my_log(a, base = b)
my_log(d, base = c)