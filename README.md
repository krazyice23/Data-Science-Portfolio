## Background
The data set is made by Justinas Cirtautas who utilised the NBA Stats API to pull together this data set with https://stats.nba.com/ being the source. The dataset can be found here: https://www.kaggle.com/datasets/justinas/nba-players-data

This data set has data on each player who has been part of an NBA teams' roster (from seasons 1996-2021). 
There is biographic variables such as :
- age
- height
- weight
- country of birth
- the team played for
- draft year and round. In addition
- it has basic box score statistics such as:
  - games played
  - average number of points
  - rebounds
  - assists
  - as well advanced statistics such as true shooting percentage.

I wanted to single out one variable to be a dependent variable, 

I decided that the dependent variable will be an in-game statistic since I would like a 📈 model to predict a player’s performance 📈 from some kind of standpoint.

Then I decided on choosing either:
- **net rating** (Team's point differential per 100 possessions while the player is on the court, how much a team is outscored by or outscore the other team by when they're playing)
- **usage percentage** (Percentage of team plays used by the player while he was on the floor)
- and **true shooting percentage** (Measure of the player's shooting efficiency that takes into account free throws, 2 and 3 point shots).

Eventually I decided on using **net rating** as the dependent variable. This is because from all the statistics, **net rating** is a good statistic (for the most part) on a player’s impact during a match, 
since it’s basically to find out how much your teams outscores another team (or how much your gets outscored by) and is a good indicator on a player’s performance. 

So I try to find the best model that best predicts a player’s **net rating** using the other variables and on the way answer questions such as “Does a higher height mean you’re going to score more or not?”.


## Summary
- I used linear regression 📈 since, **net rating** is a dependent variable and continuous variable as well
- this will be best suited to try and find a model using the other variables to predict **net rating**.
- I used a polynomial regression model to make a model with multiple predictors (in-game statistics and biological information) to predict **net rating**.
  - This is done mostly so that I can use RFE to find the relevant columns,
  - since from my analysis some of the variables negatively affect the r-squared as well the mean square error (which are used to indicate how good of a fit a linear model is).

🌟Key conclusions or takeaways that I found is that:
- non-NBA watchers might think a player's team is more likely to outscore the other team if the player has a higher height, however this model says that this isn't necessarily true, and the opposite may be true.
  - I didn’t necessarily think that **height** will positively affect **net rating**,
  - because after watching the NBA for some time now, being taller than everyone doesn’t really guarantee more success anymore (since height affects mobily in most cases).
- Another takeaway is a team will be more likely to outscore an opponent if the players get a higher percentage of available offensive rebounds while he is on the floor (since this gives the team another chance to score after a missed attempt to score).
- However what’s more surprising to me is that **offensive rebound percentage** is more significant compared to a player’s shooting efficiency (**true shooting percentage**) in predicting **net rating**.


