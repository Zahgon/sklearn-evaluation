import numpy as np
import pandas as pd


class DataGrid:
    def __init__(self, records, group_by=None):
        # build data frame
        df = pd.DataFrame.from_dict(records)

        # columns that will be interpreted as paramers
        params = sorted(set(df.columns) - set(["data"]))

        if group_by is None:
            if len(params) != 2:
                raise ValueError(
                    "There should be exactly two columns apart "
                    f"from data, found: {len(params)} ({params}) "
                    "if group_by is not specified"
                )
            else:
                group_by = params
        else:
            if len(group_by) != 2:
                raise ValueError(
                    "group_by must have 2 elements, " f"got: {len(group_by)}"
                )

        self.params = params
        self.group_by = group_by

        # fill with nas if any combination is missing
        unique = [df[p].unique().tolist() for p in params]
        prod = pd.MultiIndex.from_product(unique, names=params)

        df = df.set_index(params).reindex(prod, fill_value=np.nan).reset_index()

        self.shape = len(df[group_by[0]].unique()), len(df[group_by[1]].unique())
        self.df = df.sort_values(group_by)

    def celliter(self):
        # supply data by grouping on the first parameter
        pass

    def rowiter(self):
        # supply data by grouping on the first parameter
        pass

    def rownames(self):
        pass

    def colnames(self):
        pass
