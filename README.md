# delete-lambda-versions
This script will take input from the lambda_list.txt file and read each line for a new lambda function.

It will then check that function for its versions. It will delete all the versions except for those associated with an alias, the highest version number and the $LATEST version.

For more information check out my blog at https://aaron.vansledright