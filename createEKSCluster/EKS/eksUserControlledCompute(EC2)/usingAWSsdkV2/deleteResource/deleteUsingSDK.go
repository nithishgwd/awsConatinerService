package main

import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/eks"
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

	// Specify the EKS cluster and node group names
	clusterName := "my-eks-cluster"
	nodegroupName := "my-nodegroup"

	// Delete the managed node group
	_, err = svc.DeleteNodegroup(context.TODO(), &eks.DeleteNodegroupInput{
		ClusterName:   aws.String(clusterName),
		NodegroupName: aws.String(nodegroupName),
	})
	if err != nil {
		log.Fatalf("Error deleting managed node group: %v", err)
	}

	// Wait for the node group to be deleted (optional but recommended)
	err = svc.WaitUntilNodegroupInactive(context.TODO(), &eks.DescribeNodegroupInput{
		ClusterName:   aws.String(clusterName),
		NodegroupName: aws.String(nodegroupName),
	})
	if err != nil {
		log.Fatalf("Error waiting for node group to be deleted: %v", err)
	}

	log.Printf("Managed node group '%s' deleted successfully.", nodegroupName)

	// Delete the EKS cluster
	_, err = svc.DeleteCluster(context.TODO(), &eks.DeleteClusterInput{
		Name: aws.String(clusterName),
	})
	if err != nil {
		log.Fatalf("Error deleting EKS cluster: %v", err)
	}

	// Wait for the cluster to be deleted (optional but recommended)
	err = svc.WaitUntilClusterDeleted(context.TODO(), &eks.DescribeClusterInput{
		Name: aws.String(clusterName),
	})
	if err != nil {
		log.Fatalf("Error waiting for cluster to be deleted: %v", err)
	}

	log.Printf("EKS cluster '%s' deleted successfully.", clusterName)
}
