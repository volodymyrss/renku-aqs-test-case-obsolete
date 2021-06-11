#from astropy.coordinates import SkyCoord
import astroquery.legacysurvey

#astroquery.legacysurvey.LegacySurvey.query_object_async(SkyCoord(83,22, unit="deg"))

print(astroquery.legacysurvey.LegacySurvey.query_object)

r = astroquery.legacysurvey.LegacySurvey.query_object("nothing")

print("astroquery returns:", r)

open("test-output.txt", "w").write("test!" + str(astroquery.hooked))

