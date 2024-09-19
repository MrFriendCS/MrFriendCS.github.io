# Use Ctrl + Shift + s to open the command shell

# Type 'pytest' to run the tests

# Do not change this program!

import functions

def test_areaSquare():
    assert functions.areaSquare(1) == 1
    assert functions.areaSquare(2) == 4
    assert functions.areaSquare(3) == 9


def test_areaRectangle():
    assert functions.areaRectangle(1,1) == 1
    assert functions.areaRectangle(2,3) == 6
    assert functions.areaRectangle(3,4) == 12


def test_areaTriangle():
    assert functions.areaTriangle(1,1) == 0.5
    assert functions.areaTriangle(2,3) == 3
    assert functions.areaTriangle(3,4) == 6


def test_areaCircle():
    assert functions.areaCircle(1) == 3.14
    assert functions.areaCircle(2) == 12.56
    assert functions.areaCircle(10) == 314


def test_volCube():
    assert functions.volCube(1) == 1
    assert functions.volCube(2) == 8
    assert functions.volCube(3) == 27


def test_volCuboid():
    assert functions.volCuboid(1,1,1) == 1
    assert functions.volCuboid(1,2,3) == 6
    assert functions.volCuboid(2,3,4) == 24


def test_volCylinder():
    assert functions.volCylinder(1,1) == 3.14
    assert functions.volCylinder(2,3) == 37.68
    assert functions.volCylinder(10,10) == 3140


def test_findAt():
    assert functions.findAt("@") == 0
    assert functions.findAt("pupil@glow.sch.uk") == 5
    assert functions.findAt("@@") == 1


def test_findChar():
    assert functions.findChar("test@test.com","@") == True
    assert functions.findChar("pupilglow.sch.uk","@") == False
    assert functions.findChar("abcdef","c") == True
    assert functions.findChar("12345","c") == False