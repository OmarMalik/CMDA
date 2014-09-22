setwd("C:/R")

load("exampleData1.RData")

merged = merge(medianincome, custdata)

norm.income = scale(merged$Median.Income)
summary(norm.income)
# Normalizing the income is useful because income is different in different locations
# because of different costs of living. A high income in one state might be a low 
# income in another state.

test.set <- subset(custdata, custdata$gp <= 0.3)
training.set <- subset(custdata, custdata$gp > 0.3)