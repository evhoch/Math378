from palmerpenguins import penguins
from pandas import get_dummies
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

from vetiver import VetiverModel
from vetiver import VetiverAPI


import pins
from vetiver import vetiver_pin_write

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

from sklearn.tree import DecisionTreeRegressor

import duckdb

# Assuming your data model folder is correctly pointed to by this path
b = pins.board_folder('data/model', allow_pickle_read=True)

# Check what's inside the board
print(b.pin_list())

# Check versions for the specific pin
print(b.pin_versions('penguin_model'))

# Load the model
v = VetiverModel.from_pin(b, 'penguin_model', version='20240402T203910Z-baf25')

# Create and run the API
vetiver_api = VetiverAPI(v)
api = vetiver_api.app

app = VetiverAPI(v, check_prototype = True)

app.run(port = 8080)
