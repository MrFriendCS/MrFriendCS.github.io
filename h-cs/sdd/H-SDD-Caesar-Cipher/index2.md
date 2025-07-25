# H SDD - Caesar Cipher Part 2


## Task

Use the structure diagram to create a sub-program that will decrypt a ciphertext message and return the plaintext.

All punctuation and spaces are maintained.  The plaintext will have the same case as the ciphertext.

Save the code as `caesar.py`.


## Structure diagram

![Structure diagram](assets/sd2.png)


## Examples

### Example 1

#### Code
``` python
decode("Ifmmp!", 1)
```

#### Output
```
'Hello!'
```

### Example 2

#### Code
``` python
decode("def ABC", 29)
```

#### Output
```
'abc XYZ'
```

## Testing

Run the file [caesarTests.py](assets/caesarTests.py "Download file") and choose 'Decode test'.  The file must be in the same folder as `caesar.py`.
