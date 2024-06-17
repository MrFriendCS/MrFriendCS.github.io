export function simplify (value1, value2) {
    // Local variable
    let divided = true;

    while (divided) {
        divided = false;

        if (value1 % 2 == 0 && value2 % 2 == 0) {
            value1 = value1 / 2;
            value2 = value2 / 2;
            divided = true;
        }
        else if (value1 % 3 == 0 && value2 % 3 == 0) {
            value1 = value1 / 3;
            value2 = value2 / 3;
            divided = true;
        }
        else if (value1 % 5 == 0 && value2 % 5 == 0) {
            value1 = value1 / 5;
            value2 = value2 / 5;
            divided = true;
        }
        else if (value1 % 7 == 0 && value2 % 7 == 0) {
            value1 = value1 / 7;
            value2 = value2 / 7;
            divided = true;
        }
        else if (value1 % 13 == 0 && value2 % 13 == 0) {
            value1 = value1 / 13;
            value2 = value2 / 13;
            divided = true;
        }
        else if (value1 % 17 == 0 && value2 % 17 == 0) {
            value1 = value1 / 17;
            value2 = value2 / 17;
            divided = true;
        }
        else if (value1 % 19 == 0 && value2 % 19 == 0) {
            value1 = value1 / 19;
            value2 = value2 / 19;
            divided = true;
        }
        else if (value1 % 23 == 0 && value2 % 23 == 0) {
            value1 = value1 / 23;
            value2 = value2 / 23;
            divided = true;
        }
    }

    return [value1, value2];
}
