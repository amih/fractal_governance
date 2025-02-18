# Copyright (C) 2022 Matt Langston. All Rights Reserved.
"""Statistics functions for fractal governance data analysis"""

# builtins

# 3rd party
import numpy as np
import pandas as pd

# 2nd party


def combined_mean(
        df: pd.DataFrame,
        *,  # pylint: disable=C0103
        count_column_name: str = 'count',
        mean_column_name: str = 'mean') -> float:
    """Return the combined 'mean of means'"""
    return (df[count_column_name] *
            df[mean_column_name]).sum() / df[count_column_name].sum()


def combined_standard_deviation(
    df: pd.DataFrame,  # pylint: disable=C0103
    count_column_name: str = 'count',
    mean_column_name: str = 'mean',
    standard_deviation_column_name: str = 'standard_deviation'
) -> float:  # pylint: disable=C0301
    """Return the combined 'mean of standard deviations'"""
    ess = ((df[count_column_name] - 1) *
           np.power(df[standard_deviation_column_name], 2)).sum()
    tgss = (
        df[count_column_name] *
        np.power(df[mean_column_name] - df[mean_column_name].mean(), 2)).sum()  # pylint: disable=C0301
    degrees_of_freedom = df[count_column_name].sum() - 1
    return np.sqrt((ess + tgss) / degrees_of_freedom)
