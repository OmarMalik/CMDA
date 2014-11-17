library(rpart)
library(rpart.plot)

data(mtcars)

head(mtcars)
names(mtcars)

?mtcars

mtcars$gp <- runif(dim(mtcars)[1])
train <- subset(mtcars, mtcars$gp > 0.50)
test <- subset(mtcars, mtcars$gp <= 0.50)

head(train$am)  
head(test$am)   

train$response <- train$am > 0
head(train$response)

selectedVars = "mpg + cyl + disp + hp + drat + qsec + vs + gear + carb + gp"
f <- paste('response ~ ', paste(selectedVars, collapse=' + '), sep=' ')
f
tmodel <- rpart(f, data=train, control=rpart.control(cp=0.01, minsplit=1, minbucket=1, maxdepth=5))
tmodel

prp(tmodel)

library(ROCR)


train$pred <- predict(tmodel, newdata = train)
eval <- prediction(train$pred, train$response) 


auc_calc <- performance(eval,'auc')
auc_calc@y.values 
plot(performance(eval, "tpr", "fpr"))



fit <- rpart(mtcars$am~., data=mtcars)
fit

predictions <- predict(fit, mtcars, type="matrix")


table(predictions, mtcars$am)

prp(fit)
