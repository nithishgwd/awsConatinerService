package main

import (
    "context"
    "log"
    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/eks"
    "github.com/aws/aws-sdk-go-v2/service/eks/types"
)

func main() {
    // Load AWS configuration
    cfg, err := config.LoadDefaultConfig(context.TODO(),
        config.WithRegion("us-east-1"), // Replace with your desired AWS region
    )
    if err != nil {
        log.Fatalf("Error loading AWS config: %v", err)
    }

    // Create an Amazon EKS client
    svc := eks.NewFromConfig(cfg)

    // Create an EKS cluster
    createClusterInput := &eks.CreateClusterInput{
        Name: aws.String("my-eks-cluster"), // EKS cluster name
        RoleArn: aws.String("arn:aws:iam::123456789012:role/eks-service-role"), // IAM role for EKS service
        ResourcesVpcConfig: &types.VpcConfigRequest{
            SubnetIds: []string{"subnet-12345678", "subnet-87654321"}, // Subnet IDs
            SecurityGroupIds: []string{"sg-12345678"}, // Security Group IDs
        },
        // Add more configuration as needed
    }

    _, err = svc.CreateCluster(context.TODO(), createClusterInput)
    if err != nil {
        log.Fatalf("Error creating EKS cluster: %v", err)
    }

    // Create a managed node group
    createNodegroupInput := &eks.CreateNodegroupInput{
        ClusterName: aws.String("my-eks-cluster"), // EKS cluster name
        NodegroupName: aws.String("my-nodegroup"), // Node group name
        NodeRole: aws.String("arn:aws:iam::123456789012:role/eks-node-role"), // IAM role for nodes
        Subnets: []string{"subnet-12345678", "subnet-87654321"}, // Subnet IDs
        // Add more configuration as needed
    }

    _, err = svc.CreateNodegroup(context.TODO(), createNodegroupInput)
    if err != nil {
        log.Fatalf("Error creating managed node group: %v", err)
    }

    log.Println("EKS cluster and managed node group created successfully.")
}
