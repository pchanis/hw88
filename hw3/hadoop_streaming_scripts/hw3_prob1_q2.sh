haddoop jar /usr/lib/hadoop/hadoop-streaming.jar
 -mapper "hw3_prob1_mapper_unique_visitor_by_url.py" 
 -reducer "hw3_prob1_reducer_unique_visitor_by_url.py" 
 -input "hw3/prob1/data_q2" 
 -output hw3/prob1/ouput_q2-`date +%s` 
 -file hw3_prob1_mapper_unique_visitor_by_url.py
 -file hw3_prob1_reducer_unique_visitor_by_url.py
