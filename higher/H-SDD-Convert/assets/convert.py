# Title: H-SDD-Convert
# Author: Mr Friend
# Date: 8 Sep 2024


def f2c(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    
    # Local variables
    celcius = 0.0
    
    # Convert
    celsius = (fahrenheit - 32) * (5/9)
    
    # Round to 1 dp
    celsius = round(celsius, 1)
    
    # Return result
    return celsius


def c2f(celsius):
    """Convert Celsius to Fahrenheit"""
    
    # Local variables
    fahrenheit = 0.0
    
    # Convert
    fahrenheit = (celsius * (9/5)) + 32
    
    # Round to 1 dp
    fahrenheit = round(fahrenheit, 1)
    
    # Return result
    return fahrenheit


def m2km(miles):
    """Convert miles to kilometres"""
    
    # Local variables
    km = 0.0
    
    # Convert
    km = miles * 1.609344
    
    # Round to 1 dp
    km = round(km, 1)
    
    # Return result
    return km


def km2m(km):
    """Convert kilometres to miles"""
    
    # Local variables
    miles = 0.0
    
    # Convert
    miles = km / 1.609344
    
    # Round to 1 dp
    miles = round(miles, 1)
    
    # Return result
    return miles


def fi2cm(feet, inches):
    """Convert feet and inches to centimetres"""
    
    # Local variables
    cm = 0.0
    
    # Convert
    inches = inches + feet * 12
    cm = inches * 2.54
    
    # Round to 1 dp
    cm = round(cm, 1)
    
    # Return result
    return cm


def cm2fi(cm):
    """Convert centimetres to feet and inches"""
    
    # Local variables
    feet = 0
    inches = 0.0
    inches0dp = 0
    
    # Convert
    inches = cm / 2.54
    feet = int(inches / 12)
    
    # Round to 0 dp
    inches0dp = round(inches % 12)
    
    # Return result
    return feet, inches0dp


def sl2kg(stones, lbls):
    """Convert stones and pounds to kilograms"""
    
    # Local variables
    kg = 0.0
    
    # Convert
    lbls = lbls + stones * 14
    kg = lbls / 2.205
    
    # Round to 1 dp
    kg = round(kg, 1)
    
    # Return result
    return kg


def kg2sl(kg):
    """Convert kilograms to stones and pounds"""
    
    # Local variables
    stones = 0
    pounds = 0.0
    pounds0dp = 0
    
    # Convert
    pounds = kg * 2.205
    stones = int(pounds / 14)
    
    # Round to 0 dp
    pounds0dp = round(pounds % 14)
    
    # Return result
    return stones, pounds0dp
