setwd("C:/R")

load("exampleData.rData")
summary(custdata)
# states: a lot of people are from california. all states are not represented.
# sex: similar number of males and females
# is.employed: data not clear - what is the difference between false and NA?
# income: minimum income is negative - what does that mean? max is an outlier - it's 615,000 while the mean is 53,505
# heal.ins: most people are insured
# housing.type: what does NA mean?
# recent.move: what does NA mean?
# num.vehicles: outlier at 6 vehicles. What does NA mean?
# age: range is huge - 0 to 146.7. also, what does 0 age mean?
# income.lt.30K: what does this variable represent?

uciCar <- read.table('http://www.win-vector.com/dfiles/car.data.csv', sep=',', header=T)
summary(uciCar)
# buying: same number of low, med, and high. what does this variable mean?
# maint: same number of low, med, and high. what does this variable mean?
# doors: same number of 2, 3, 4, and 5more.
# persons: same number of 2, 4, and more.
# lug_boot: same number of big, med, small.
# safety: same number of high, low, med.
# rating: what do acc and unacc mean?

load("credit.RData")
summary(d$Personal.status.and.sex)
# not returning any useful info

summary(d$Other.debtors.guarantors)
# not returning any useful info

custdata2 <- subset(custdata, (custdata$age > 0 & custdata$age < 100 & custdata$income > 0))
bin <- hexbin(custdata2$age, custdata2$income)
plot(bin, style="lattice")
# the hexbin plot shows density with size of the dot in the hexagon
# a scatter plot would just plot all of the points


plot(custdata2$num.vehicles, custdata2$income)
# I used a sactter plot
# I see a that 1-4 cars has many people in the lower income range. 
# I also see that not many people have more that 4 cars, most people have 2 cars

counts = table(custdata2$income.lt.30K, custdata2$recent.move)
barplot(counts)
# I used a bar plot to visualize the data
# I see that most people under $30k have not moved recently

