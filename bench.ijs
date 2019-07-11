simpleTime =: (6!:2)

NB. array containing two 3000x3000 arrays of random numbers
twoMatrices =: ? 2 3000 3000 $ 1e10
first =: {: twoMatrices

NB. Time to invert such a matrix
invertTime =: simpleTime '%. first'

NB. Time to multiply the two matrices together
multTime =: simpleTime '(+/ .*) / twoMatrices'
