#!/bin/bash
account_file=$1
prefix=$2
index=0

## Read all available accounts and projects
declare -a accounts projects
while IFS=, read account project; do
	accounts[$index]=$account
	projects[$index]=$project
	# echo "List servers with prefix $prefix in account $account and project $project !"
	gcloud config set account $account 1>&-
	gcloud config set project $project 1>&-
	gcloud compute instances list |grep $prefix |awk '$5!="TERMINATED" {print $1","$2","$3","$5}'

	index=$(($index+1))
done < $account_file
