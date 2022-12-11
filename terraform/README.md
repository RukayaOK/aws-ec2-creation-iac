# Create an EC2 Instance on AWS using Terraform

## Detailed Instructions 

To understand this repository in detail you can follow the blog peice here: [Create an EC2 Instance on AWS using Terraform](https://medium.com/@roadtocloude/create-an-ec2-instance-using-terraform-7606cba03d2c)

---
## Quickstart 

1. Configure/Install the prerequisites 
- An AWS account https://aws.amazon.com/resources/create-account/
- Install Terraform https://developer.hashicorp.com/terraform/downloads

2. Download this repository

3. Create an IAM user in the AWS Console with: 
   - Programmatic Access so that you can obtain an access key 
   - The existing _AdministrationAccess_ policy 

4. Export the AWS credentials 
    ```bash
    export AWS_ACCESS_KEY_ID="<access-key-id>"
    export AWS_SECRET_ACCESS_KEY="<secret-access-key>"
    ```
    Replace the _<access-key-id>_ and _<secret-access-key>_ with the Access Key ID and the Secret Access key values that you obtained from the step above

5. Update the __vars.tfvars__ file with the instance details 

6. Initialise Terraform 
   ```
    terraform init 
   ```

7. Run a Terraform Plan to check the resources to be created
    ```
    terraform plan --var-file vars.tfvars
    ```

8. Run a Terraform Apply to create the resources
    ```
    terraform apply --var-file vars.tfvars
    ```

9. In AWS amend the Security Group inbound rules to permit SSH traffic from your IP address. 
   
10. Use the private SSH key, created during the terraform apply, to connect the machine 
    ```
    ssh -i <private-key-file>.pem <username>@<instance-host-name>
    ```
    
11.  Run a Terraform Destroy to destroy the resources 
    ```
    terraform destroy --var-file vars.tfvars
    ```
