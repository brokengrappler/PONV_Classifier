import imblearn.over_sampling
import numpy as np

def return_oversample(mx, x, y, rs=444):
    '''
    Use imblearn over-sampling to upsample minority class
    :param mx:
        Multiplier to upsample minority class
    :param x:
        train set features
    :param y:
        train targets
    :param rs:
        random state (default 444)
    :return:
        Returns oversampled x and y
    '''
    n_pos = np.sum(y == 1)
    n_neg = np.sum(y == 0)
    ratio = {1: n_pos * mx, 0: n_neg}
    ROS = imblearn.over_sampling.RandomOverSampler(sampling_strategy=ratio, random_state=rs)
    x_os, y_os = ROS.fit_sample(x, y)
    return x_os, y_os