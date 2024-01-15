#!/usr/local/anaconda3/bin/python

import pandas as pd
import scipy.stats as stats


def anova(frame, varName):
    anv = pd.DataFrame()
    anv["feature"] = varName
    pvals = []
    for c in varName:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]["score"].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")
