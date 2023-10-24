**Step 1: Creating an EKS Cluster**

1. Creating a new Amazon EKS cluster using the `eksctl` command:

  ```bash
  eksctl create cluster --name=eksdemo1 --region=us-east-1 --zones=us-east-1a,us-east-1b --without-nodegroup
  ```

  - if didnt specified `--withougt-nodegroup` eksctl will create default `production grade` cluster

  - When you create an EKS cluster without a default node group, it means that no worker nodes (EC2 instances) are created as part of the cluster creation process.

  ```bash
  eksctl create cluster --name my-eks-cluster --region us-east-1 --nodegroup-name my-nodegroup --node-type t2.small --nodes 3 --nodes-min 1 --nodes-max 5 --managed
  ```

  - `--nodes 3`: This flag sets the desired number of nodes in the node group to 3. These are the initial EC2 instances that will be part of the node group.

  - `--nodes-min 1`: The --nodes-min flag sets the minimum number of nodes in the node group to 1. This means the node group can scale down to a minimum of 1 instance if the workload is low.

  - `--nodes-max 5`: The --nodes-max flag defines the maximum number of nodes in the node group, which is 5 in this example. This is the upper limit for scaling the node group to accommodate increased workloads.

  - `--managed`: The --managed flag indicates that this is a managed node group, which means AWS takes care of the operational aspects of the nodes, such as scaling, patching, and maintenance. can choose to create self-managed node groups if prefer more control over the node group operations.

2. Create & Associate IAM OIDC Provider for our EKS Cluster
  - To enable and use AWS IAM roles for Kubernetes service accounts on our EKS cluster, we must create & associate OIDC identity provider.
    # Template
    eksctl utils associate-iam-oidc-provider \
        --region region-code \
        --cluster <cluter-name> \
        --approve

    # Replace with region & cluster name
    eksctl utils associate-iam-oidc-provider \
        --region us-east-1 \
        --cluster eksdemo1 \
        --approve

***Here are some additional attributes you can attach to the `eksctl` command for further customization:**

1. **VPC Configuration**:
   - `--vpc-public-subnets`: Specify the public subnets where EKS control plane endpoints will be deployed.
   - `--vpc-private-subnets`: Define the private subnets where worker nodes will be placed.
   - `--vpc-cidr`: Set the VPC CIDR block for the cluster's VPC.
   - `--vpc-id`: If you have an existing VPC, you can specify its ID to use it for the EKS cluster.

2. **Kubernetes Version**:
   - `--kubernetes-version`: Specify the desired Kubernetes version for your EKS cluster.

3. **EC2 Instance Attributes**:
   - `--node-ami-family`: Set the Amazon Machine Image (AMI) family to use for worker nodes (e.g., Amazon Linux 2 or Ubuntu).
   - `--node-volume-size`: Define the EBS volume size in GiB for each node.
   - `--node-labels` and `--node-tags`: Attach custom labels and tags to the worker nodes for organizational purposes.

4. **Instance Profile and Security Group**:
   - `--node-instance-profile`: Configure the IAM instance profile for worker nodes.
   - `--node-security-groups`: Attach custom security groups to the worker nodes.

5. **Key Pair and SSH Access**:
   - `--ssh-access`: Enable SSH access to worker nodes.
   - `--ssh-public-key`: Specify an SSH public key to use for accessing worker nodes.

6. **Additional Node Group Options**:
   - You can add more node groups to the cluster by repeating the `--nodegroup-name`, `--node-type`, `--nodes`, `--nodes-min`, and `--nodes-max` options for each additional group.

7. **Node Group Scaling**:
   - `--asg-access`: Enable AWS Auto Scaling group integration for worker nodes.
   - `--node-labels` and `--node-tags`: Use these flags to attach labels and tags to node groups.
   - `--node-termination-handler`: Enable or disable the node termination handler.

8. **Kubernetes Add-ons**:
   - You can enable or disable various Kubernetes add-ons like CoreDNS, KubeProxy, and more using flags such as `--install-vpc-controllers`, `--install-kube-proxy`, etc.

9. **Logging and Monitoring**:
   - `--enable-pod-logs`: Enable or disable pod-level CloudWatch logging.
   - `--enable-node-termination-handler`: Enable or disable the node termination handler.

10. **Node Group Instances Distribution**:
    - `--node-zones`: Specify which availability zones to distribute the worker nodes across.


**Step 2: Deploying a Sample Application**

1. Create a new file named `deployment.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

2. Deploy the sample application to your EKS cluster:

```bash
kubectl apply -f deployment.yaml
```

**Step 4: Exposing the Application**

1. Expose the application using a Kubernetes service:

```bash
kubectl expose deployment nginx-deployment --type=LoadBalancer --name=my-service
```

2. Get the external IP address of the LoadBalancer:

```bash
kubectl get services my-service
```

can access the application using the external IP address and port number.

**Step 5: Setting up Horizontal Pod Autoscaler (HPA)**

1. Create a new file named `hpa.yaml` with the following content:

```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-deployment-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

2. Apply the HPA configuration:

```bash
kubectl apply -f hpa.yaml
```

Now, your EKS cluster will automatically scale the number of pods based on the CPU utilization.

3. Configure permissions for your IAM user account

```bash
kubectl get configmap aws-auth -n kube-system -o yaml > aws-auth.yaml
```
Edit the `aws-auth.yaml` file and add the `mapUsers` section (as per the below example)

- IAM user is granted administrative access to the Kubernetes cluster and can perform actions such as deploying, modifying, and deleting resources

```yaml
apiVersion: v1
data:
  mapRoles: |
    - groups:
      - system:bootstrappers
      - system:nodes
      rolearn: arn:aws:iam::<account-number>:role/eksctl-my-eks-cluster-nodegroup-m-NodeInstanceRole-ZKA8ZSWLC7Z2
      username: system:node:{{EC2PrivateDNSName}}
  mapUsers: |
    - userarn: <your-iam-user-arn>
      username: <your-iam-user-name>
      groups:
        - system:masters

kind: ConfigMap
metadata:
  creationTimestamp: "2023-05-12T10:41:25Z"
  name: aws-auth
  namespace: kube-system
  resourceVersion: "1215"
  uid: 54d885a3-3484-41d4-b032-41959915d8b6
```

Then, run:

```bash
kubectl apply -f aws-auth.yaml
```

You should now have access to view all objects in the cluster

## Delete the service and cluster

kubectl delete svc my-service

eksctl delete cluster --name my-eks-cluster