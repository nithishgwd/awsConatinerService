Amazon Elastic Kubernetes Service (EKS) does not create any nodes by default. Instead, EKS provides a managed Kubernetes control plane and allows you to bring your own Amazon Elastic Compute Cloud (EC2) instances as worker nodes.

When you create an Amazon EKS cluster, you need to specify how many worker nodes you want to include in the cluster and what type of EC2 instances you want to use for these nodes. EKS does not create any worker nodes for you; you are responsible for provisioning and managing these nodes yourself.

You can create worker nodes in your EKS cluster using one of the following methods:

1. **Amazon EKS Node Groups**: You can use EKS node groups to create and manage a group of worker nodes. EKS node groups are a recommended way to manage worker nodes as they are integrated with EKS and provide features like automatic scaling, automated node updates, and simplified node management.

2. **Self-Managed Nodes**: You can create and manage your own EC2 instances as worker nodes and join them to your EKS cluster manually. This method provides more control and flexibility but requires more manual management.

The number and type of worker nodes you create will depend on your specific workload requirements. You can scale the worker node group up or down based on your application's resource needs. EKS allows you to have flexibility in managing your worker nodes to ensure your cluster's performance, scalability, and cost-effectiveness.