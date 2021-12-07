# Euclidean Algorithm
The `euclidean.py` file contains my implementations of the Euclidean Algorithm and the Extended Euclidean Algorithm, the latter of which is used to calculate the modular inverse of `a mod N`, where `a` is a non-zero integer and `N` is the modulus.

## Running as a Script
`euclidean.py` accepts three arguments and returns the result:
- ALGORITHM: The algorithm to be used. Can either be "EA" or "EEA". Use "EA" to calculate the GCD using the Euclidean Algorithm. Use "EEA" to calculate the modular inverse using the Extended Euclidean Algorithm.
- MODULUS: The modulus.
- INTEGER: The integer.

If "EA" is used, then the GCD of the two numbers will be calculated. If "EEA" is used, then the modular inverse of `a mod N` (where `a` is the integer and `N` is the modulus) will be calculated.

## Dependencies
The scripts don't require anything except Python 3.9+ to run. The packages in `requirements.txt` are only needed for testing (via Pytest) and code formatting (via Black).
