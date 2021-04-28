#Import libraries
library('readr')
library('dplyr')
library('TraMineR')
library("tidyr")

sequences <- read_csv(file ='Ressources/Example/Data/Prepared_Sequences.csv')
sequences <- select(sequences, -'X1')
head(sequences)

sequences_Advanced <- select(sequences, -'Ressources_Type_Basic')

seq_dbt <- spread(sequences_Advanced, Ressources_Rank,Ressources_Type_Basic)
seq_dbt


seq_dbt_2016 <- seq_dbt %>% filter(Year == 2016)
seq_dbt_2016

seq_dbt_2016_10frst <- seq_dbt_2016[,-c(2:4)] # Keep the Course_ID
seq_dbt_2016_10frst <- seq_dbt_2016_10frst[,-c(12:31)] # 10 First_messages

seq_dbt_2016_10frst

table(is.na(seq_dbt_2016_10frst))
seq_dbt_2016_10frst_cl <-drop_na(seq_dbt_2016_10frst)
seq_dbt_2016_10frst_cl


mvad.seq <- seqdef(seq_dbt_2016_10frst_cl[, c(2:10)])
head(mvad.seq, 10)

#seqiplot(mvad.seq, border = NA, withlegend = "right", tlim = 1:10, space=0)
