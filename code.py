#from astropy.coordinates import SkyCoord
import astroquery.legacysurvey

#astroquery.legacysurvey.LegacySurvey.query_object_async(SkyCoord(83,22, unit="deg"))

print(astroquery.utils.process_asyncs._original_async_to_sync)

r = astroquery.legacysurvey.LegacySurvey.query_object_async("Crab")

print("astroquery returns:", r)

open("test-output.txt", "w").write("test!" + str(astroquery.hooked))

