import logging

logging.basicConfig(
    filename='apps.log',
    filemode='w',
    level = logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y %m %d %H %M %S'
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"The Addition of {a}+{b} is : {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"The Subtraction of {a}-{b} is : {result}")
    return result

def mul(a,b):
    result = a*b
    logger.debug(f"The Multiplication of {a}*{b} is : {result}")
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f"The Divison of {a}/{b} is : {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Error: Division by zero is not allowed")
        return None
    
add(10,15)
sub(10,5)
mul(10,10)
div(10,2)