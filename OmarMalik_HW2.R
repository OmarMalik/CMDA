setwd("C:/R")
load("phsample.RData")

summary(dhus)
summary(dpus)
# the phsample.RData file contains census data such as a employment, age, education level, etc.



#2.12
psub= subset(dpus,with(dpus,(PINCP>1000)&(ESR==1)&
                         (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
                         (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
                         (PWGTP1>0)&(COW%in%(1:7))&(SCHL%in% (1:24))))
# this creates a subset of the dpus data frame with certain conditions on the values of the variables and saves it to psub



#2.13
psub$SEX= as.factor(ifelse(psub$SEX==1,'M','F'))
psub$SEX= relevel(psub$SEX,'M')
cowmap<- c("Employeeofa privatefor-profit",
           "Privatenot-for-profitemployee",
           "Localgovernmentemployee",
           "Stategovernmentemployee",
           "Federalgovernmentemployee",
           "Self-employednotincorporated",
           "Self-employedincorporated")
psub$COW= as.factor(cowmap[psub$COW])
psub$COW= relevel(psub$COW,cowmap[1])
schlmap= c(
  rep("nohighschooldiploma",15),
  "Regularhighschooldiploma",
  "GEDor alternativecredential",
  "somecollegecredit,nodegree",
  "somecollegecredit,nodegree",
  "Associate'sdegree",
  "Bachelor'sdegree",
  "Master'sdegree",
  "Professionaldegree",
  "Doctoratedegree")
psub$SCHL= as.factor(schlmap[psub$SCHL])
psub$SCHL= relevel(psub$SCHL,schlmap[1])
dtrain=subset(psub,ORIGRANDGROUP>= 500)
dtest=subset(psub,ORIGRANDGROUP< 500)
# this code makes the data in psub much more readable by reencoding the variables
# it also creates two subsets of the data, one for the variable ORIGRANDGROUP >= 500, and one for ORIGRANDGROUP < 500




#2.14
summary(dtrain$COW)
# this provides a summary of the COW variable in the dtrain data frame


athletes = read.table("OlympicAthletes_0.csv", sep = ",", head = T)











