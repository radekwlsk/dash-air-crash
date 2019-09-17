import time
from os import getenv

from requests.exceptions import ConnectionError
from pygeocoder import Geocoder
import pandas as pd
from pygeolib import GeocoderError
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata(getenv('SOCRATA_API_URL'), None)


def get_air_crashes(limit=6000, raw=False):
    try:
        df = pd.read_csv(f"air-crash-data-{limit}.csv", sep=';', encoding='utf-8')
    except FileNotFoundError:
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
            df['year'] = df['date'].map(lambda d: d.year)
            lat = []
            lon = []
            geocoder = Geocoder(api_key=getenv('GOOGLE_API_KEY'))
            for location in df['location']:
                try:
                    geo = geocoder.geocode(location)
                    lat.append(geo.coordinates[0])
                    lon.append(geo.coordinates[1])
                    print(geo)
                except (GeocoderError, ConnectionError) as e:
                    print(e)
                    lat.append(None)
                    lon.append(None)
                time.sleep(0.1)

            df['latitude'] = lat
            df['longitude'] = lon

            df.to_csv(f"air-crash-data-{limit}.csv", encoding='utf-8', index=False, sep=';')
    return df
