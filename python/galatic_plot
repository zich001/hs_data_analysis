from astropy.coordinates import SkyCoord
from astropy import units
from astropy.coordinates import Galactic

coords = SkyCoord(ra=ra, dec=dec, unit='rad')
rap = coords.galactic.l.wrap_at(180 * units.deg).radian
decp = coords.galactic.b.radian

color_map = plt.cm.Spectral_r
fig = plt.figure(figsize=(20, 8))
fig.add_subplot(111, projection='mollweide')
image = plt.hexbin(rap, decp, cmap=color_map,gridsize=45, mincnt=1,reduce_C_function=np.sum)

plt.xlabel('R.A.')
plt.ylabel('Decl.')
plt.grid(True)
plt.colorbar(image, spacing='uniform', extend='max')
plt.show()
