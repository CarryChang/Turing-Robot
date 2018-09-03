import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import os
def run():
    s= '今天天气不错'
    s = SnowNLP(s)
    score = s.sentiments
    print(score)

if __name__ == '__main__':
    run()

