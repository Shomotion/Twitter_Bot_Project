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

Output of program after removing irrelevant columns:


Confusion Matrix on Test Set:
###################################################

Epoch: 50       Time: 0.8621875
Training:
genuine_account social_spambot  traditional_spambot
1967    094     020     | genuine_account
053     2850    049     | social_spambot
146     774     656     | traditional_spambot
Accuracy: 0.8281

Validation:
genuine_account social_spambot  traditional_spambot
623     030     007     | genuine_account
016     957     020     | social_spambot
071     249     230     | traditional_spambot
Accuracy: 0.8216

###################################################

Epoch: 100      Time: 0.8609375
Training:
genuine_account social_spambot  traditional_spambot
1921    146     014     | genuine_account
028     2899    025     | social_spambot
012     291     1273    | traditional_spambot
Accuracy: 0.9219

Validation:
genuine_account social_spambot  traditional_spambot
610     044     006     | genuine_account
009     968     016     | social_spambot
010     125     415     | traditional_spambot
Accuracy: 0.9047

###################################################

Epoch: 150      Time: 0.8504166666666667
Training:
genuine_account social_spambot  traditional_spambot
1836    034     211     | genuine_account
053     2579    320     | social_spambot
008     033     1535    | traditional_spambot
Accuracy: 0.9003

Validation:
genuine_account social_spambot  traditional_spambot
584     021     055     | genuine_account
015     873     105     | social_spambot
008     013     529     | traditional_spambot
Accuracy: 0.9015

###################################################

Epoch: 200      Time: 0.84359375
Training:
genuine_account social_spambot  traditional_spambot
1938    049     094     | genuine_account
027     2827    098     | social_spambot
020     094     1462    | traditional_spambot
Accuracy: 0.9422

Validation:
genuine_account social_spambot  traditional_spambot
608     024     028     | genuine_account
009     946     038     | social_spambot
011     037     502     | traditional_spambot
Accuracy: 0.9333

###################################################

Epoch: 250      Time: 0.8375625
Training:
genuine_account social_spambot  traditional_spambot
1979    011     091     | genuine_account
066     2816    070     | social_spambot
018     035     1523    | traditional_spambot
Accuracy: 0.9560

Validation:
genuine_account social_spambot  traditional_spambot
626     011     023     | genuine_account
017     946     030     | social_spambot
014     020     516     | traditional_spambot
Accuracy: 0.9478

###################################################

Epoch: 300      Time: 0.8342708333333333
Training:
genuine_account social_spambot  traditional_spambot
1892    060     129     | genuine_account
027     2860    065     | social_spambot
006     049     1521    | traditional_spambot
Accuracy: 0.9492

Validation:
genuine_account social_spambot  traditional_spambot
594     031     035     | genuine_account
010     956     027     | social_spambot
009     020     521     | traditional_spambot
Accuracy: 0.9401

###################################################

Epoch: 350      Time: 0.8347767857142857
Training:
genuine_account social_spambot  traditional_spambot
2010    024     047     | genuine_account
043     2832    077     | social_spambot
028     037     1511    | traditional_spambot
Accuracy: 0.9613

Validation:
genuine_account social_spambot  traditional_spambot
628     017     015     | genuine_account
014     954     025     | social_spambot
015     015     520     | traditional_spambot
Accuracy: 0.9542

###################################################

Epoch: 400      Time: 0.8362890625
Training:
genuine_account social_spambot  traditional_spambot
2002    031     048     | genuine_account
036     2860    056     | social_spambot
024     067     1485    | traditional_spambot
Accuracy: 0.9604

Validation:
genuine_account social_spambot  traditional_spambot
629     019     012     | genuine_account
010     962     021     | social_spambot
014     034     502     | traditional_spambot
Accuracy: 0.9501

###################################################

Epoch: 450      Time: 0.9100347222222223
Training:
genuine_account social_spambot  traditional_spambot
1908    044     129     | genuine_account
029     2832    091     | social_spambot
022     041     1513    | traditional_spambot
Accuracy: 0.9461

Validation:
genuine_account social_spambot  traditional_spambot
601     022     037     | genuine_account
012     954     027     | social_spambot
014     018     518     | traditional_spambot
Accuracy: 0.9410

###################################################

Epoch: 500      Time: 0.96084375
Training:
genuine_account social_spambot  traditional_spambot
1975    042     064     | genuine_account
030     2814    108     | social_spambot
024     033     1519    | traditional_spambot
Accuracy: 0.9545

Validation:
genuine_account social_spambot  traditional_spambot
617     025     018     | genuine_account
009     956     028     | social_spambot
013     012     525     | traditional_spambot
Accuracy: 0.9523

***************************************************

Confusion Matrix on Test Set:
genuine_account social_spambot  traditional_spambot
696     020     017     | genuine_account
013     925     029     | social_spambot
008     014     482     | traditional_spambot
Accuracy: 0.9542
Average time: 0.96084375
