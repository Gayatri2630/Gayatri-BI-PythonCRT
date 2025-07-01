#loc-to locate the row
import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)
#locate named indexes:
#refer to the named index
print(myvar.loc["day2"])
print(myvar.loc["day3"])