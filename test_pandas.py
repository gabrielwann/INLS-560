import pandas as pd

mydataset = {
  'superheroes': ["spiderman", "goku", "beastboy"],
  'power level': [88, 9000, 65]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

