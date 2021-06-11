#from astropy.coordinates import SkyCoord
import astroquery.legacysurvey

#astroquery.legacysurvey.LegacySurvey.query_object_async(SkyCoord(83,22, unit="deg"))
astroquery.legacysurvey.LegacySurvey.query_object_async("Crab")

open("test-output.txt", "w").write("test!" + str(astroquery.hooked))

