import pandas as pd

def test_no_null_values():

    data = pd.DataFrame({
        "Age": [22, 30]
    })

    assert data["Age"].isnull().sum() == 0