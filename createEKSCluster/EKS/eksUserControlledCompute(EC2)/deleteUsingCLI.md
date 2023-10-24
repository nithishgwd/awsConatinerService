Yes, you can delete the same resources that were deployed using the AWS SDK with the AWS Command Line Interface (CLI). The AWS CLI provides commands to delete Amazon EKS clusters and managed node groups. Here are the corresponding CLI commands:

**Delete an EKS Cluster:**
```bash
aws eks delete-cluster --name your-cluster-name
```

Replace `your-cluster-name` with the name of your EKS cluster.

**Delete a Managed Node Group:**
```bash
aws eks delete-nodegroup --cluster-name your-cluster-name --nodegroup-name your-nodegroup-name
```

Replace `your-cluster-name` with the name of your EKS cluster and `your-nodegroup-name` with the name of your managed node group.

By using these CLI commands, you can delete the same resources created by the AWS SDK for Go in your EKS cluster. Be sure to have the AWS CLI configured with the appropriate credentials and permissions before running these commands.



To delete the CloudFormation stack created by the provided AWS CloudFormation template, you can use the AWS CLI. First, make sure you have the AWS CLI installed and configured with the necessary credentials. Then, use the following command:

```bash
aws cloudformation delete-stack --stack-name stack-name
```

Replace `stack-name` with the actual name of the CloudFormation stack you want to delete. For example:

```bash
aws cloudformation delete-stack --stack-name my-eks-cluster-stack
```

This command will initiate the deletion of the CloudFormation stack, which will remove all the AWS resources created by the stack, including the Amazon EKS cluster and managed node group. Make sure you understand the implications of stack deletion before executing this command, as it will remove all the resources associated with the stack.