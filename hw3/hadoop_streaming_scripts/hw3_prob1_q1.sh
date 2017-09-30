haddoop jar /usr/lib/hadoop/hadoop-streaming.jar
 -mapper "hw3_probl_mapper_count_url.py" 
 -reducer "hw3_prob1_reducer_count_url.py" 
 -input "hw3/prob1/data_q1" 
 -output hw3/prob1/ouput_q1-`date +%s` 
 -file hw3_problem1_mapper_count_url.py
 -file hw3_problem1_reducer_count_url.py
