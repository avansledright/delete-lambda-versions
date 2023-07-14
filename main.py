import boto3
from botocore.exceptions import CLientError

client = boto3.client("lambda", region_name='us-west-2')
def delete_function_version(function_name, version):
    
    try:
       response = client.delete_function(
           FunctionName=function_name,
           Qualifier=str(version)
       ) 
    except ClientError as e:
        print("Failed to delete version of", function_name, "version number", str(version))
        print(e)
def get_layer_versions(function_name):
    try:
        response = client.list_versions_by_function(
            FunctionName=function_name
        )
        return response['Versions']
    except ClientError as e:
        print('failed to get info for', function_name)
        print(e)

if __name__ == "__main__":
    print("Starting lambda update")
    with open("lambda_list.txt", "r") as text:
        lambda_list = text.read().splitlines()
        text.close()
    version_info_results = {}
    for lambda_function in lambda_list:
        print("Working with lambda", lambda_function)
        lambda_versions = get_layer_versions(lambda_function)
        lambda_version_list = []
        for version in lambda_versions:
            version_number = version['Version']
            if version_number == "$LATEST":
                pass
            else:
                lambda_version_list.append(int(version_number))
        for lambda_version in lambda_version_list:
            if y == max(lambda_version_list):
                print("This is the latest version skipping", str(lambda_version))
                pass
            else:
                print("Deleting version", lambda_version, "of", lambda_function)
                delete_function_version(lambda_function, lambda_version)
            