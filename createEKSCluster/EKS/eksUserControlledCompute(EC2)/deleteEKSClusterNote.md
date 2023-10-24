When you delete an Amazon EKS cluster using `eksctl`, it primarily focuses on cleaning up the EKS-specific resources like the EKS control plane, managed node groups, and any Fargate profiles associated with the cluster. However, it does not automatically delete any external AWS resources that you might have created outside of the EKS cluster itself.

For example, if you created an AWS Network Security Group (NSG) or Security Group with inbound rules to allow traffic to one of the EKS nodes, `eksctl` won't automatically delete this NSG or Security Group when you delete the EKS cluster. You need to explicitly manage and delete such resources.

Here are some common resources that `eksctl` doesn't automatically delete and you would need to handle separately if you have created them:

1. **Network Security Groups (NSGs) or Security Groups:** Any NSGs or Security Groups associated with your EKS nodes or instances won't be deleted. You'll need to remove them manually.

2. **Amazon EC2 Instances:** If you have EC2 instances running outside of the managed node groups, you'll need to terminate these instances manually.

3. **Amazon RDS Databases, S3 Buckets, and Other AWS Resources:** EKS deletion doesn't affect resources outside the EKS cluster. You must manually manage and delete them if you no longer need them.

4. **Load Balancers:** If you've created AWS Elastic Load Balancers (ELBs) or Network Load Balancers (NLBs) associated with your EKS cluster, you'll need to delete them separately.

5. **Elastic File Systems (EFS), EBS Volumes:** EKS deletion doesn't delete these resources.

Remember to be cautious when deleting resources as it can lead to data loss or disrupt existing services. Ensure you have backups or a plan in place before deleting critical resources.

In summary, `eksctl` primarily focuses on cleaning up EKS-specific resources, but it's your responsibility to manage and delete other AWS resources that you've created outside of the EKS cluster if you no longer need them.