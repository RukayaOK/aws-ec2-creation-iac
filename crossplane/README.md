# Create an EC2 Instance on AWS using Crossplane

## Detailed Instructions 

To understand this repository in detail you can follow the blog piece here: [Create an EC2 Instance on AWS using Crossplane]()

---
## Quickstart 

1. Configure/Install the prerequisites 
- An AWS account https://aws.amazon.com/resources/create-account/
- Install Docker https://docs.docker.com/get-docker/
- Install Kind https://kind.sigs.k8s.io/docs/user/quick-start/
- Install Kubectl https://kubernetes.io/docs/tasks/tools/
- Install Helm https://helm.sh/docs/intro/install/

2. Download this repository

3. Install Crossplane CLI 
    ```
    curl -sL https://raw.githubusercontent.com/crossplane/crossplane/master/install.sh | sh
    ```

4. Create a Kubernetes In Docker (KIND) cluster
    ```
    kind create cluster --image kindest/node:v1.25.3 --wait 5m
    ```

5. Install Crossplane in your cluster
   ```
    kubectl create namespace crossplane-system
    helm repo add crossplane-stable https://charts.crossplane.io/stable
    helm repo update
    helm install crossplane --namespace crossplane-system crossplane-stable/crossplane
   ```

6. Create an IAM user in the AWS Console with: 
   - Programmatic Access so that you can obtain an access key 
   - The existing _AdministrationAccess_ policy 

7. Create a file containing the Access key ID and Secret access key
    ```bash
    [default]
    aws_access_key_id = <access-key-id>
    aws_secret_access_key = <secret-access-key>
    ```
    Replace the _<access-key-id>_ and _<secret-access-key>_ with the Access Key ID and the Secret Access key values that you obtained from the step above

8. Create a kubernetes secret using the credentials
    ```
    kubectl create secret generic aws-creds -n crossplane-system --from-file=creds=./aws-creds.conf
    ```

9. Install the AWS Crossplane provider in your cluster
   ```
   kubectl crossplane install provider crossplane/provider-aws:v0.27.0
   ```

10. Create the Provider Configuration
    ```
    kubectl apply -f aws-provider-config.yml
    ```

11. Create an SSH Key Pair in the AWS Console

12. Create your EC2 instance
    ```
    kubectl apply -f ec2.yml
    ```

13. In AWS amend the Security Group inbound rules to permit SSH traffic from your IP address. 
   
14. Use the private SSH key, created during the terraform apply, to connect the machine 
    ```
    chmod 400 <<private-key-file>.pem
    ssh -i <private-key-file>.pem <username>@<instance-host-name>
    ```
    
15. Destroy your Instance
    ```
    kubectl delete -f ec2.yml
    ```
