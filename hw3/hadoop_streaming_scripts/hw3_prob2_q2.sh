haddoop jar /usr/lib/hadoop/hadoop-streaming.jar
 -mapper "hw3_prob2_mapper_unique_visitor_by_url_hour.py" 
 -reducer "hw3_prob2_reducer_unique_visitor_by_url_hour.py" 
 -input "hw3/prob2/data_q2" 
 -output hw3/prob2/ouput_q2-`date +%s` 
 -file hw3_prob2_mapper_unique_visitor_by_url_hour.py
 -file hw3_prob2_reducer_unique_visitor_by_url_hour.py
