# Create an EC2 Instance on AWS using Pulumi (Python)

## Detailed Instructions 

To understand this repository in detail you can follow the blog piece here: [Create an EC2 Instance on AWS using Pulumi (Python)]()

---
## Quickstart 

1. Configure/Install the prerequisites 
- An AWS account https://aws.amazon.com/resources/create-account/
- Install Python https://www.python.org/downloads/
- Install Pulumi https://www.pulumi.com/docs/get-started/install/

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

5. Set Pulumi configuration variables
    ```
    pulumi config set key_pair_name <key-pair-name>
    pulumi config set instance_ami <instance-ami>
    pulumi config set instance_ami <instance-type>
    ```

6. Activate the Virtual Environment
   ```
   source venv/bin/activate
   ```

7. Install the requirements in your Virtual Environment
    ```
    pip3 install -r requirements.txt
    ```

8. Install the python packages needed for this Pulumi project
    ```
    pip3 install pulumi_tls
    pip3 install pulumi_aws
    ```

9. Run the Pulumi stack to create the resources
    ```
    pulumi up
    ```

10.  Create the SSH key from the Pulumi output
    ```
    pulumi stack output private_key_pem --show-secrets >> my-pulumi-created-key-pair2.pem
    ```

11. In AWS amend the Security Group inbound rules to permit SSH traffic from your IP address. 
   

12.   Use the private SSH key, created during the terraform apply, to connect the machine 
    ```
    chmod 400 <<private-key-file>.pem
    ssh -i <private-key-file>.pem <username>@<instance-host-name>
    ```
    
13.   Run a Pulumi Destroy to destroy the resources 
    ```
    pulumi destroy
    ```

14.   Destroy the Pulumi Stack 
    ```
    pulumi stack rm <stack-name>
    ```
