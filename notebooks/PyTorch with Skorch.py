# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# PyTorch/Tensorflow are extremely verbose packages.
#
#
# The <b>good</b> thing about it is that you learn by having to do every single step of it.<br>
# The obvious <b>bad</b> thing about it is that you have to do every single step of it, and whenever you have to write a lot of code, bugs appear...
#
# There are many packages to short the amount of code people have to write. For example:
#
# - Ignite  --> https://pytorch.org/ignite/ | https://github.com/pytorch/ignite (3.2k stars)
# - Pytorch-lightning --> https://www.pytorchlightning.ai/ (11.3k stars)
# - Skorch -->  https://github.com/skorch-dev/skorch (3.7k stars)
#
# - Poutyne --> https://poutyne.org/ | https://github.com/GRAAL-Research/poutyne (422 stars)
# - Catalyst --> https://github.com/catalyst-team/catalyst (2.4k stars)
#

# Example of what are these frameworks for:
#
# ![image.png](https://www.comet.ml/site/app/uploads/2020/03/Screen-Shot-2020-03-20-at-12.31.04-PM.png)

# +
import numpy as np
from sklearn.datasets import make_classification
from torch import nn

from skorch import NeuralNetClassifier

X, y = make_classification(1000, 24, n_informative=10, random_state=0)
X = X.astype(np.float32)
y = y.astype(np.int64)

class MyNet(nn.Module):
    def __init__(self, num_units=10, nonlin=nn.ReLU()):
        super(MyNet, self).__init__()

        self.dense0 = nn.Linear(24, num_units)
        self.nonlin = nonlin
        self.dropout = nn.Dropout(0.5)
        self.dense1 = nn.Linear(num_units, num_units)
        self.output = nn.Linear(num_units, 2)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x, **kwargs):
        X = self.nonlin(self.dense0(x))
        X = self.dropout(X)
        X = self.nonlin(self.dense1(X))
        X = self.softmax(self.output(X))
        return X


net = NeuralNetClassifier(
    MyNet,
    max_epochs=10,
    lr=0.1,
    # Shuffle training data on each epoch
    #iterator_train__shuffle=True,
)

net.fit(X, y)
y_proba = net.predict_proba(X)

# +
from pycaret.datasets import get_data
from pycaret.classification import *

data = get_data('diabetes')
clf1 = setup(data, target = 'Class variable')
# The transformed data has shape (_, 24)
# -

create_model(net)

# Wrote my complain/question: https://github.com/pycaret/pycaret/issues/700
