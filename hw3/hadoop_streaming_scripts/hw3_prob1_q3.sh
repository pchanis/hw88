haddoop jar /usr/lib/hadoop/hadoop-streaming.jar
 -mapper "hw3_prob1_mapper_unique_clicks.py" 
 -reducer "hw3_prob1_reducer_unique_clicks.py" 
 -input "hw3/prob1/data_q3" 
 -output hw3/prob1/ouput_q3-`date +%s` 
 -file hw3_prob1_mapper_unique_clicks.py
 -file hw3_prob1_reducer_unique_clicks.py
