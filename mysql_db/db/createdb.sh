#!/usr/bin/env bash
# trap 'exit 0' SIGTERM
# i=1
# while i==1 ; 

# do :

#trap 'startup' SIGINT


mysql -uroot -proot -hlocalhost -e "
CREATE DATABASE fresco_segment;
use fresco_segment;

CREATE TABLE customer_segments (
  party_id VARCHAR(20),
  fresco13_mseg  VARCHAR(3),
  fresco13_seg  VARCHAR(3),
  fresco13_sseg VARCHAR(3),
  match_flag CHAR(1)
);

LOAD DATA INFILE '/var/lib/mysql-files/Dataset.csv' 
INTO TABLE customer_segments 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;"


#Define cleanup procedure
cleanup() {
	
	echo "*************remove files************"
	
    echo "**************************Stopping the container, performed cleanup**************************"
	sleep
}


#Trap SIGTERM
trap 'cleanup' SIGTERM

trap 'userinterupt' SIGINT


#Wait
wait $!
