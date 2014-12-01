load('KDD2009.Rdata')
library(ROCR)
library(rpart)
library(class)

names(dTrain)

head(dTrain$churn) 

dTrain$response <- dTrain$churn > 0

??ksvm
library(kernlab)
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
f

system.time(mSVMV <- ksvm(as.formula(f),data = dTrain, kernel = 'vanilladot')) #bad kernel function

system.time(svm_pred <- predict(mSVMV, newdata = dTrain, type = 'response'))
head(svm_pred)

eval <- prediction(svm_pred, dTrain$response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values

system.time(mSVMV1 <- ksvm(as.formula(f),data = dTrain, kernel = 'rbfdot'))

system.time(svm_pred1 <- predict(mSVMV1, newdata = dTrain, type = 'response'))

head(svm_pred1)

eval <- prediction(svm_pred1, dTrain$response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values

install.packages("e1071")
library(e1071)
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
f

system.time(fit <- naiveBayes(as.formula(f), data=dTrain))

system.time(naivB_pred <- predict(fit, dTrain, type = 'raw'))
head(naivB_pred)
?naiveBayes

eval <- prediction(naivB_pred[,2], dTrain$response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values

knnTrain <- dTrain[,selVars]
names(knnTrain)

response <- dTrain$churn > 0

head(response)
head(knnTrain)
dim(knnTrain)

system.time(knnDecision <- knn(knnTrain,knnTrain,response,k=200,prob=T))
?knn

head(knnDecision)

knnPred <- ifelse(knnDecision==TRUE,
attributes(knnDecision)$prob,
1-(attributes(knnDecision)$prob))
head(knnPred)

eval <- prediction(knnPred, response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='') 
system.time(gmodel <- glm(as.formula(f),
data=knnTrain,
family=binomial(link='logit'))) 

log_predict <- predict(gmodel,
newdata=knnTrain,
type = "response")

eval <- prediction(log_predict, response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values 

f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
system.time(tmodel <- rpart(f,data=dTrain,
control=rpart.control(cp=0.001,minsplit=1000,
minbucket=1000,maxdepth=5)))
dTrain$pred <- predict(tmodel, newdata = dTrain)
dTrain$response <- dTrain$churn > 0

eval <- prediction(dTrain$pred, dTrain$response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values
