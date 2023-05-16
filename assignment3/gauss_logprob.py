import numpy as np


def gauss_logprob(pDs, x):
    nObj = len(pDs)  # Number of GaussD Objects
    nx = x.shape[1]  # Number of observed vectors
    print(nx)
    logP = np.zeros((nObj, nx))

    for i, pD in enumerate(pDs):
        dSize = pD.dataSize
        # assert dSize == x.shape[0]
        print(pD.covEigen)
        print(np.matlib.repmat(pD.means, 1, nx))
        print(x-np.matlib.repmat(pD.means, 1, nx))
        z = np.dot(pD.covEigen, (x-np.matlib.repmat(pD.means, 1, nx)))
        print(z)

        z /= np.matlib.repmat(np.expand_dims(pD.stdevs, 1), 1, nx)

        logP[i, :] = -np.sum(z*z, axis=0)/2
        logP[i, :] = logP[i, :] - sum(np.log(pD.stdevs)) - dSize*np.log(2*np.pi)/2
    return logP


def prob(gauss_dist, x):
    px = []


    return px