setwd("C:/R")

athletes = read.table("OlympicAthletes_0.csv", sep = ",", head = T)
summary(athletes$Athlete)
summary(athletes$Age)
summary(athletes$Country)
summary(athletes$Year)
summary(athletes$Closing.Ceremony.Date)
summary(athletes$Sport)
summary(athletes$Gold.Medals)
summary(athletes$Silver.Medals)
summary(athletes$Bronze.Medals)
summary(athletes$Total.Medals)

plot(athletes$Age, athletes$Total.Medals)
# this plot shows the relationship between athlete age and number of medals they won
# we can see that athlete in their 20s won the most medals

agecounts = table(athletes$Age)
barplot(agecounts)
# this chart shows the number of athletes at each age
# we can see that most athletes are in their 20s

sportcounts = table(athletes$Sport)
barplot(sportcounts)
# this chart shows how many people were in each sport


# no data transformations had to be made on this data set


