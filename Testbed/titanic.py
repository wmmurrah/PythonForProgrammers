# titanic.py

import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
    'Rdatasets/csv/carData/TitanicSurvival.csv')

titanic.head()
titanic.tail()

titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

titanic.describe()

titanic.value_counts('survived')
titanic.value_counts(['sex'])
titanic.value_counts('class')


mtcars = pd.read_csv(
    "https://vincentarelbundock.github.io/"
    + "Rdatasets/csv/datasets/mtcars.csv"
)

mtcars.plot.scatter('hp', 'mpg', s = 'cyl')
