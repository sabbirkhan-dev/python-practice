"""# Python Packages – Important Notes

## 1. What is a Package?

* A **package** is a collection of modules.
* A **module** is a single Python file (`.py`).
* A **package** is a folder that contains multiple modules.

Example structure:

```
package_name/
    module1.py
    module2.py
```

## 2. Importing a Package

Import a package:

```python
import package_name
```

Import a specific module or function:

```python
from package_name import module_name
```

Example:

```python
from math import sqrt
```

## 3. Package Manager

* **pip** is the default package manager in Python.
* It is used to install external packages.

Example:

```bash
pip install numpy
```

## 4. Package Repository

* **PyPI (Python Package Index)** is the official repository for Python packages.
* It contains thousands of open-source Python packages.

## 5. Main Application Areas of Python

* Data Science
* Machine Learning / Artificial Intelligence
* Web Development
* Automation
* Application Development
* Hardware Interfacing

## 6. Popular Built-in Packages

These come with Python and do not require installation.

* os
* sys
* csv
* json
* math
* re
* importlib
* itertools

Example:

```python
import os
```

## 7. Data Science Packages

* numpy
* pandas
* scipy
* nltk
* matplotlib
* opencv

## 8. Machine Learning / AI Packages

* tensorflow
* pytorch
* keras
* scikit-learn
* theano

## 9. Web Development Packages

* flask (lightweight micro framework)
* django (full-stack web framework)
* pyramid
* cherrypy
* beautifulsoup
* selenium

## 10. Key Idea

Python has thousands of packages.
Most problems in development can be solved using an existing package.
"""


# Popular Python Packages Examples

import numpy as np

a = np.zeros(5)  # 5 zeros
print("zeros", a) 

b = np.full((2, 10), 0.7)
print("full", b)

c = np.linspace(0, 25, 7)
print("linspace", c)

import pandas as pd
p1 = pd.DataFrame({
    "numbers" : [1, 2, 3, 4, 5],
    "letters" : ["a", "b", "c", "d", "e"]
})

print(p1) 
print(p1.describe())

p1 = pd.DataFrame({"mix": ["x", 3, "y", 1, "z"]})
print(p1)


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))
# Print statement 2
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)

