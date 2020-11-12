import matplotlib.pyplot as plt
import numpy as np
from readin import readinXsec
runs = [f"run_{i+1:02d}" for i in range(6)]
print(runs)

widthes = np.asarray([i/1000 + 3.38233934e-03 for i in range(6)])

muDir = "testdir1"
eDir = "testdir2"
tauDir = "testdir3"

muMass = 1.056600e-01
eMass = 5.110000e-04
tauMass = 1.777000e+00


muXseces,muErrorBars = readinXsec(muDir)
eXseces,eErrorBars = readinXsec(eDir)
tauXseces,tauErrorBars = readinXsec(tauDir)


plt.subplot(121)
plt.semilogy(widthes,muXseces,'-o',alpha=0.5)
plt.semilogy(widthes,eXseces,'-x',alpha=0.5)
plt.semilogy(widthes,tauXseces,'-*',alpha=0.5)
plt.legend(['mu','e','tau'])
plt.title("Xsec")
plt.subplot(122)
plt.semilogy(widthes,muXseces/muMass**2,'-o',alpha=0.5)
plt.semilogy(widthes,eXseces/eMass**2,'-x',alpha=0.5)
plt.semilogy(widthes,tauXseces/tauMass**2,'-*',alpha=0.5)
plt.legend(['mu','e','tau'])
plt.title('Xsec scaled by lepton mass')
plt.suptitle("Lepton Higgs Xsec at different Higgs Decay Width")
plt.savefig('test.pdf')
plt.figure()
plt.plot(1/widthes**2,muXseces/muMass**2,'-o',alpha=0.5)
plt.plot(1/widthes**2,eXseces/eMass**2,'-x',alpha=0.5)
plt.plot(1/widthes**2,tauXseces/tauMass**2,'-*',alpha=0.5)
plt.legend(['mu','e','tau'])
plt.title('Xsec scaled by lepton mass')
plt.savefig('test1.pdf')
