#!/usr/bin/env python3
# Script to launch the CEBRA API REST

import pycbr
from pycbr.models import *

# Define a case base from the csv file
case_base = pycbr.casebase.SimpleCSVCaseBase("cb.csv")
# Define the set of similarity functions
recovery = pycbr.recovery.Recovery([
    ("Age", LinearAttribute(40), 1),
    ("Children", ExponentialAttribute(0.5), 1),
    ("Gender", KroneckerAttribute(), 1),
    ("Type of contract", LinearOrdinalAttribute(["G.O", "P.C.", "P", "T"]), 1)
],
    algorithm="brute")
# Define the aggregation method
aggregation = pycbr.aggregate.ColumnRankAggregate(["Applied for a mortgage",
                                                   "Applied for a loan",
                                                   "Applied for a deposit",
                                                   "Applied for an investment fund",
                                                   "Applied for an accident insurance"],
                                                  true_values=("Yes",),
                                                  weighted=True)

# Create a CBR instance
cbr = pycbr.CBR(case_base, recovery, aggregation, server_name="CEBRA")

# Expose the WSGI app
app = cbr.app

if __name__ == '__main__':
    # Start the development server
    app.run()
