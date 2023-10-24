1. About
    `--fargate` flag implies that you intend to use AWS Fargate as the compute engine for your pods, and therefore, you won't be managing traditional worker nodes as you would in a typical EKS cluster with EC2 instances.

    Don't need to specify the typical EC2-related attributes since Fargate is responsible for managing the compute resources for your containerized workloads.


2. To create an Amazon EKS cluster with Fargate as the default compute engine using `eksctl` use `--fargate` flag:

```bash
eksctl create cluster --name my-eks-cluster --region us-east-1 --fargate
```

In this command:

- `--name` specifies the name of the EKS cluster.
- `--region` specifies the AWS region for the cluster.
- `--fargate` indicates that you want to use Fargate as the default compute engine for the cluster.

This command will create an EKS cluster where Fargate is the default compute engine for running your Kubernetes pods. With Fargate, you don't need to manage EC2 instances, as AWS handles the underlying infrastructure, allowing you to focus on deploying and managing your containerized applications.

