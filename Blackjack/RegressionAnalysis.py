import csv
import numpy as np
import matplotlib.pyplot as plt

class RegressionAnalysis:

    def __init__(self, numFeature, verbose=False):
        self.param = np.ones(numFeature, dtype=np.float32)
        self.verbose = verbose

    def train(self, Xs, Ys, iteration=10):
        if self.verbose == True:
            print("--------------------------------" + "Initail" "--------------------------------")
            print(self.param)
            print(self.calculateMeanSquaredError(Xs, Ys))
        for itr in range(iteration):
            self.searchParameters(Xs, Ys)
            if self.verbose == True:
                print("--------------------------------"+"Iteration "+str(itr+1)+"--------------------------------")
                print (self.calculateMeanSquaredError(Xs,Ys))
                print (self.param)
        return self.calculateMeanSquaredError(Xs,Ys)

    def searchParameters(self, Xs, Ys):
        firstDeriv = self.calculateFirstDerivative(Xs,Ys)
        hessian = self.calculateSecondDerivative(Xs,Ys)
        Noise = np.zeros(shape=hessian.shape, dtype=np.float32)  # making noise to the diagonal element of hessian
        for i in range(len(Noise)):
            Noise[i][i] = 0.00001
        hessian = hessian + Noise
        invHessian = np.linalg.inv(hessian)
        self.param = self.param - np.dot(invHessian,firstDeriv)

    def test(self,Xs,Ys):
        return self.calculateMeanSquaredError(Xs,Ys)

    def calculateFirstDerivative(self,Xs,Ys):
        ret = np.zeros(shape=(len(Xs[0])),dtype=np.float32)
        for i in range(len(Xs[0])):
            sum2 = 0
            for r in range(len(Xs)):
                sum1 = 0
                for s in range(len(Xs[0])):
                    sum1 = sum1 + Xs[r][s]*self.param[s]
                sum2 = sum2 + (-2)*Xs[r][i]*(Ys[r]-sum1)
            ret[i] = sum2
        return ret

    def calculateSecondDerivative(self,Xs,Ys):
        ret = np.zeros(shape=(len(Xs[0]),len(Xs[0])),dtype=np.float32)
        for i in range(len(Xs[0])):
            for j in range(len(Xs[0])):
                sum1 = 0
                for r in range(len(Xs)):
                    sum1 = sum1 + 2*Xs[r][i]*Xs[r][j]
                ret[i][j] = sum1
        return ret
    
    def calculateMeanSquaredError(self,Xs,Ys):
        sumMSE = 0.0
        for r in range(len(Xs)):
            sumMSE = sumMSE + self.calculateMeanSquaredErrorPerInstance(Xs[r],Ys[r])
        sumMSE = sumMSE / len(Xs)
        return sumMSE
    
    def calculateMeanSquaredErrorPerInstance(self,X,Y):
        error = Y
        for i in range(len(X)):
            error = error - X[i]*self.param[i] 
        MSE = error * error
        return MSE
      
      
if __name__ == "__main__":
    dataX = []
    dataY = []
    file = open('./test6.csv','r')
    csvReader = csv.reader(file)
    next(csvReader)
    for row in csvReader:
        dataX.append([1.0]+row[:-1])
        dataY.append(row[-1])
    file.close()

    dataX = np.array(dataX,dtype=np.float32)
    dataY = np.array(dataY,dtype=np.float32)

    shuffle = np.arange(np.shape(dataX)[0])

    numFeature = 3
    numTesting = 50
    numReplication = 20.0
    x = []
    testMSEs = []
    testMSESTDs = []
    trainingMSEs = []
    trainingMSESTDs = []
    for numTraining in range(10,111,10):
        avgTrain = 0.0
        avgSquaredTrain = 0.0
        avgTest = 0.0
        avgSquaredTest = 0.0
        for itr in range(int(numReplication)):
            np.random.shuffle(shuffle)
            trainingX = dataX[shuffle[0:numTraining], 0:numFeature]
            trainingY = dataY[shuffle[0:numTraining]]
            testingX = dataX[shuffle[-numTesting-1:-1], 0:numFeature]
            testingY = dataY[shuffle[-numTesting-1:-1]]

            analysis = RegressionAnalysis(numFeature,verbose=False)
            trainMSE = analysis.train(trainingX,trainingY)
            testMSE = analysis.test(testingX,testingY)
            avgTrain = avgTrain + trainMSE
            avgSquaredTrain = avgSquaredTrain + trainMSE*trainMSE
            avgTest = avgTest + testMSE
            avgSquaredTest = avgSquaredTest + testMSE * testMSE

        avgTrain = avgTrain / numReplication
        avgSquaredTrain = avgSquaredTrain / numReplication
        avgTest = avgTest / numReplication
        avgSquaredTest = avgSquaredTest / numReplication

        x.append(numTraining)
        trainingMSEs.append(avgTrain)
        testMSEs.append(avgTest)
        trainingMSESTDs.append(np.sqrt(avgSquaredTrain-avgTrain*avgTrain))
        testMSESTDs.append(np.sqrt(avgSquaredTest-avgTest*avgTest))
        print ('Average Training MSE : '+str(avgTrain))
        print('Average Testing MSE : ' + str(avgTest))

    print(trainingMSEs)
    print(testMSEs)
    print(trainingMSESTDs)
    print(testMSESTDs)
    print('param is' ,analysis.param)
    plt.errorbar(x,trainingMSEs,trainingMSESTDs,color='Blue',linewidth=2.0)
    plt.errorbar(x,testMSEs,testMSESTDs,color='Red',linewidth=2.0)
    plt.legend(['Training Mean Squared Error','Testing Mean Squared Error'],loc="upper right")
    plt.xlabel('Training Instances')
    plt.ylabel('Mean Squared Error')
    plt.ylim([-0.01,max(testMSEs)])
    plt.xlim([min(x),max(x)])
    plt.show()