from astropy.coordinates import SkyCoord
import astroquery.legacysurvey

astroquery.legacysurvey.LegacySurvey.query_region(SkyCoord(83,22, unit="deg"))

open("test-output.txt", "w").write("test!" + str(astroquery.hooked))

