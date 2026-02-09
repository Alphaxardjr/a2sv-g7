### Modulo index mapping /circular array rotation
formular 
new_index = (i-k)%n - left rotation
new_index = (i+k)%n -  righ rotation

or new[i] = old[(i+k)%n]

where 
n = lenth of an array
i = index
k = number of steps
