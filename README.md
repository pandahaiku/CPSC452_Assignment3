# CPSC452_Assignment3
Assignemnt 3 for CPSC 452: Cryptography - Utilization of SHA512 integrity checking

Team Members:
Alan Adame          aadame4@csu.fullerton.edu
Douglas Galm        douglasgalm@csu.fullerton.edu
Johnson Lien        johnsonlien95@csu.fullerton.edu
Michael Lindwall    michaellindwall@csu.fullerton.edu

Programming Language:
python

Instructions:
1. open terminal in program directory
2. python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>
3. with the paramaters:
    KEY FILE NAME: The name of the file containing private key (if signing) or public key (when verifying the digital signature)
    SIGNATURE FILE NAME: The file to which to save the digital signature (if signing) or from which to load the digital signature (when verifying)
    INPUT FILE NAME: The file for which to generate or verify the digital signature
    MODE: Can be one of the following things:
        sign: This mode tells the program to:
            1. Read the INPUT FILE NAME
            2. Compute a SHA-512 hash of the contents read
            3. Encrypt the hash with the private key from KEY FILE NAME file
            4. Save the result (i.e, the digital signature) to the SIGNATURE FILE NAME.
        verify: This mode tells the program to:
            1. Read the INPUT FILE NAME
            2. Compute a SHA-512 hash of the contents read
            3. Decrypt the signature from SIGNATURE FILE NAME using the public key from file KEY FILE NAME
            4. Compare the decrypted value against the SHA-512 hash, and output whether the signature matches
 
 Extra Credit:

 Notes:
