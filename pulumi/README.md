# Create an EC2 Instance on AWS using Pulumi (Python)

## Detailed Instructions 

To understand this repository in detail you can follow the blog peice here: [Create an EC2 Instance on AWS using Pulumi (Python)]()

---
## Quickstart 

1. Download this repository

2. Create an IAM user in the AWS Console with: 
   - Programmatic Access so that you can obtain an access key 
   - The existing _AdministrationAccess_ policy 

3. Export the AWS credentials 
    ```bash
    export AWS_ACCESS_KEY_ID="<access-key-id>"
    export AWS_SECRET_ACCESS_KEY="<secret-access-key>"
    ```
    Replace the _<access-key-id>_ and _<secret-access-key>_ with the Access Key ID and the Secret Access key values that you obtained from the step above

4. Set Pulumi configuration variables
```
pulumi config set key_pair_name <key-pair-name>
pulumi config set instance_ami <instance-ami>
pulumi config set instance_ami <instance-type>
```

5. Activate the Virtual Environment
   ```
   source venv/bin/activate
   ```

6. Install the requirements in your Virtual Environment
    ```
    pip3 install -r requirements.txt
    ```

7. Install the python packages needed for this Pulumi project
    ```
    pip3 install pulumi_tls
    pip3 install pulumi_aws
    ```

8. Run the Pulumi stack to create the resources
    ```
    pulumi up
    ```

9. Create the SSH key from the Pulumi output
    ```
    pulumi stack output private_key_pem --show-secrets >> my-pulumi-created-key-pair2.pem
    ```

10. Use the private SSH key, created during the terraform apply, to connect the machine 
    ```
    chmod 400 <<private-key-file>.pem
    ssh -i <private-key-file>.pem <username>@<instance-host-name>
    ```
    
11. Run a Pulumi Destroy to destroy the resources 
    ```
    pulumi destroy
    ```

12. Destroy the Pulumi Stack 
    ```
    pulumi stack rm <stack-name>
    ```
---