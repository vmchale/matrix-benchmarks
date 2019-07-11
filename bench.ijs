NB. see https://news.ycombinator.com/item?id=19637188 and 
NB. https://www.jsoftware.com/help/learning/31.htm

simpleTime =: (6!:2)

NB. array containing two 3000x3000 arrays of random numbers
NB. twoMatrices =: ? 2 3000 3000 $ 1e10

NB. Time to invert such a matrix
invertTime =: simpleTime '%. ? 3000 3000 $ 1e10'

NB. Time to multiply the two matrices together
multTime =: simpleTime '(+/ .*) / ? 2 3000 3000 $ 1e10'
multCheck =: simpleTime '(? 3000 3000 $ 1e10) (+/ .*) (? 3000 3000 $ 1e10)'
