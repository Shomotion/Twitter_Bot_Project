Original data set found here by clicking on the "cresci-2017" data set: https://botometer.iuni.iu.edu/bot-repository/datasets.html
Data files:
genuine_accounts.csv
social_spambots.csv
traditional_spambots.csv

social_spambots.csv has been produced by combining the 3 social_spambots users.csv files, and the same is true for traditional_spambots.csv

command:
sed 's/^.*$/"traditional_spambot",&/' traditional_spambots.csv > traditional_spambots_labeled.csv

Output of program before removing irrelevant columns:
###################################################

Epoch: 50 	Time: 34.9371875
Training:
genuine_account	social_spambot	traditional_spambot	
008 	1723 	000 	| genuine_account
000 	2458 	000 	| social_spambot
001 	1318 	000 	| traditional_spambot
Accuracy: 0.4477

Validation:
genuine_account	social_spambot	traditional_spambot	
003 	844 	000 	| genuine_account
000 	1244 	000 	| social_spambot
000 	663 	000 	| traditional_spambot
Accuracy: 0.4528

###################################################

Epoch: 100 	Time: 32.46109375
Training:
genuine_account	social_spambot	traditional_spambot	
008 	1723 	000 	| genuine_account
000 	2458 	000 	| social_spambot
001 	1318 	000 	| traditional_spambot
Accuracy: 0.4477

Validation:
genuine_account	social_spambot	traditional_spambot	
003 	844 	000 	| genuine_account
000 	1244 	000 	| social_spambot
000 	663 	000 	| traditional_spambot
Accuracy: 0.4528

###################################################

Epoch: 150 	Time: 33.92572916666666
Training:
genuine_account	social_spambot	traditional_spambot	
008 	1723 	000 	| genuine_account
000 	2458 	000 	| social_spambot
001 	1318 	000 	| traditional_spambot
Accuracy: 0.4477

Validation:
genuine_account	social_spambot	traditional_spambot	
003 	844 	000 	| genuine_account
000 	1244 	000 	| social_spambot
000 	663 	000 	| traditional_spambot
Accuracy: 0.4528