data(mtcars)

head(mtcars)
names(mtcars)

?mtcars

library(class)

mtcars$gp <- runif(dim(mtcars)[1])
train <- subset(mtcars, mtcars$gp > 0.25)
test <- subset(mtcars, mtcars$gp <= 0.25)

head(train$am)
head(test$am)

train$response <-train$am > 0
head(train$response)

system.time(knnDecision <- knn(train,train,train$response,k=20,prob=T))

head(knnDecision)

knnPred <- ifelse(knnDecision==TRUE, attributes(knnDecision)$prob, 1-(attributes(knnDecision)$prob))
head(knnPred)

library(ROCR)

eval <- prediction(knnPred, train$response)
auc_calc <- performance(eval,'auc')
auc_calc@y.values 

f <- "response ~ mpg + cyl + disp + hp + drat + wt + qsec + vs + gear + carb + gp"


system.time(gmodel <- glm(as.formula(f), data=train))

log_predict <- predict(gmodel, newdata=train, type = "response")

eval <- prediction(log_predict, train$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values 

library(rpart)

system.time(tmodel <- rpart(f,data=train, control=rpart.control(cp=0.001,minsplit=10, minbucket=10,maxdepth=5)))

train$pred <- predict(tmodel, newdata = train)
train$response <- train$am > 0

eval <- prediction(train$pred, train$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

library(e1071)

system.time(fit <- naiveBayes(as.formula(f), data=train))

system.time(naivB_pred <- predict(fit, train, type = 'raw'))

head(naivB_pred)

eval <- prediction(naivB_pred[,2], train$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values