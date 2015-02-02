import sys, numpy, scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
import matplotlib
from matplotlib.pyplot import show

#open the file assuming the data above is in a file called 'dataFile'
inFile = open('daneLotniskaOK.txt','r')
#save the column/row headers (conditions/genes) into an array
colHeaders = inFile.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

for line in inFile:
	data = line.strip().split('\t')
	rowHeaders.append(data[0])
	dataMatrix.append([float(x) for x in line.strip().split()[1:]])

#convert native python array into a numpy array
dataMatrix = numpy.array(dataMatrix)
#print dataMatrix

#calculate distance matrix and convert to squareform
distanceMatrix = dist.pdist(dataMatrix)
distanceSquareMatrix = dist.squareform(distanceMatrix)

#print distanceMatrix
#print distanceSquareMatrix

#calculate linkage matrix
linkage = hier.linkage(distanceSquareMatrix, 'median')
#print linkage

#get the order of the dendrogram leaves
heatmapOrder = hier.leaves_list(linkage)

#print heatmapOrder

ccc = hier.fcluster(linkage, 1, criterion = 'distance')
    
#print aaa

bbb = scipy.cluster.hierarchy.leaders(linkage, ccc)

#print bbb

#ccc= scipy.cluster.hierarchy.fclusterdata(dataMatrix, 2, metric='euclidean')
cccl = len(ccc)

fff = scipy.cluster.hierarchy.dendrogram(linkage, no_plot=False)
#show()

wynik = []
for i in range(cccl):  

        wynik = wynik + [[ccc[i], dataMatrix[i][0], dataMatrix[i][1]]]

wynik.sort()
wynik = numpy.array(wynik)
#print wynik


#print scipy.cluster.hierarchy.leaves_list(linkage)

wsx = wynik[0][1]
wsy = wynik[0][2]
licznik = 1
gotowe = []

for k in range(cccl):
        if k < cccl-1:
                if wynik[k][0] == wynik[k+1][0]:
                        wsx = wsx + wynik[k+1][1]
                        wsy = wsy + wynik[k+1][2]
                        licznik = licznik +1
                else:
                        wsx = wsx/licznik
                        wsy = wsy/licznik
                        xy = [wsx, wsy]
                        gotowe = gotowe + [xy]
                        licznik = 1
                        wsx = wynik[k+1][1]
                        wsy = wynik[k+1][2]
        else:
                if wynik[k][0] == wynik[k-1][0]:
                        wsx = wsx/licznik
                        wsy = wsy/licznik
                        xy = [wsx, wsy]
                        gotowe = gotowe + [xy]
                else:
                        wsx = wynik[k][1]
                        wsy = wynik[k][2]
                        xy = [wsx, wsy]
                        gotowe = gotowe + [xy]

#gotowe = numpy.array(gotowe)
print gotowe

print len(gotowe)

plik = open('wczytywanie.txt', 'w')
for i in range(len(gotowe)):
        plik.writelines(str(gotowe[i]))
        plik.writelines("\n")
plik.close()



