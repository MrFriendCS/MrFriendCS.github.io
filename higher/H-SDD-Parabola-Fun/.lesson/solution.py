# Title: Parabola Fun
# Author: Mr Friend
# Date: 9 Jun 2024


#
# Subprogram
#

def discriminant(a, b, c):
    "Calculates the discriminant from the coefficients. Displays the discriminant and the type of roots."

    # Local variable
    disc = 0.0

    # Display data
    print("\na = " + str(a) + "\tb = " + str(b) + "\tc = " + str(c))

    # Calculate discriminant
    disc = b**2 - 4 * a * c

    # Display discriminant
    print("Discriminant: " + str(disc))

    # Display type of roots
    if disc > 0:
        print("Two real and distinct roots")
    elif disc == 0:
        print("Two real and equal roots")
    else:
        print("No real roots")

def roots(a, b, c):
    "Calculates the roots from the coefficients, rounded to 1 decimal place."

    # Local variables
    root1 = 0.0
    root2 = 0.0

    # Display data
    print("\na = " + str(a) + "\tb = " + str(b) + "\tc = " + str(c))

    # Calculate roots
    root1 = (-b+(b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b-(b**2 - 4*a*c)**0.5) / (2*a)

    # Round roots to 1 dp
    root1 = round(root1, 1)
    root2 = round(root2, 1)

    # Display roots
    print("x = " + str(root1))
    print("x = " + str(root2))


#
# Main program
#

# Calculate discriminant and type of roots
discriminant(1, 2, 4)
discriminant(4, 7, 3)
discriminant(1, 6, 9)

# Calculate roots
roots(1, 2, -24)
roots(-1, -3, 54)
