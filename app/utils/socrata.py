from os import getenv

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata(getenv('SOCRATA_API_URL'), None)


def get_air_crashes(limit=2000, raw=False):
    results = client.get(
        getenv('SOCRATA_AIRCRASHES_DATASET_ID'),
        limit=limit,
        order='date DESC',
    )
    if raw:
        return results
    else:
        # Convert to pandas DataFrame
        df = pd.DataFrame.from_records(results)
        df['date'] = pd.to_datetime(df['date'], unit='s').dt.date
        df['fatalities'] = pd.to_numeric(df['fatalities'])
        df['aboard'] = pd.to_numeric(df['aboard'])
        return df
