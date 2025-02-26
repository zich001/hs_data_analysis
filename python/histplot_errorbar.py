def plotHist(iData,iNBins=30):
    #Ok enough of having fun, let's look at the asymmetry we observe in right asecion
    y0, bin_edges = np.histogram(iData, bins=iNBins)
    bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])
    norm0=len(iData)*(bin_edges[-1]-bin_edges[0])/iNBins
    plt.errorbar(bin_centers,y0/norm0,yerr=y0**0.5/norm0,marker='.',drawstyle = 'steps-mid',linestyle='none')
    plt.xlabel("RA")
    plt.ylabel("Intensity")
    plt.show()
    return bin_centers,y0
