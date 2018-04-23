################################################################
# This file illustrates how to generate an SHA-512 hash of data
################################################################

from Crypto.Hash import SHA512

# The data I want to hash
myData = "hello world"

# Compute the SHA-512 hash of the data
dataHash = SHA512.new(myData).hexdigest()

print dataHash
