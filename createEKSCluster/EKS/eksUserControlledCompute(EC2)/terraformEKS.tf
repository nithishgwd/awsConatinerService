# Define the AWS provider and specify the desired region.
provider "aws" {
  region = "us-east-1"  # Replace with your desired region
}

# Create an Amazon EKS cluster.
resource "aws_eks_cluster" "my_eks" {
  name = "my-eks-cluster"  # EKS cluster name
  role_arn = aws_iam_role.my_eks_cluster.arn

  vpc_config {
    security_group_ids = [aws_security_group.node_group_sg.id]
    subnet_ids = [
      aws_subnet.public_subnet1.id,
      aws_subnet.public_subnet2.id,
      aws_subnet.private_subnet1.id,
      aws_subnet.private_subnet2.id
    ]
  }
}

# Create a security group for the EKS node group.
resource "aws_security_group" "node_group_sg" {
  name_prefix = "node-group-sg-"
  vpc_id = aws_vpc.my_vpc.id
  # Define your security group rules here
}

# Create the EKS node group.
resource "aws_eks_node_group" "my_nodegroup" {
  cluster_name    = aws_eks_cluster.my_eks.name
  node_group_name = "my-nodegroup"  # Node group name
  node_role_arn   = aws_iam_role.node_instance_role.arn
  subnet_ids      = [aws_subnet.private_subnet1.id, aws_subnet.private_subnet2.id]
  instance_types  = ["t2.small"]  # EC2 instance type
  capacity_type   = "ON_DEMAND"  # Use on-demand instances

  scaling_config {
    desired_size = 3  # Desired number of nodes
    min_size     = 1  # Minimum number of nodes
    max_size     = 5  # Maximum number of nodes
  }

  remote_access {
    ec2_ssh_key = "my-key-pair"  # Replace with your SSH key
  }
}

# Define the IAM role for the EKS cluster.
resource "aws_iam_role" "my_eks_cluster" {
  name = "my-eks-cluster-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "eks.amazonaws.com"
        }
      }
    ]
  })
}

# Define the IAM role for EKS node instances.
resource "aws_iam_role" "node_instance_role" {
  name = "my-node-instance-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })

  managed_policy_arns = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  ]
}

# Define the Amazon VPC.
resource "aws_vpc" "my_vpc" {
  cidr_block = "192.168.0.0/16"  # VPC CIDR block
  enable_dns_support = true
  enable_dns_hostnames = true

  tags = {
    Name = "my-eks-cluster-VPC"
  }
}

# Define the public subnets.
resource "aws_subnet" "public_subnet1" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "192.168.0.0/18"  # CIDR block for the public subnet
  availability_zone       = "us-east-1a"     # Availability zone
  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet 1"
  }
}

resource "aws_subnet" "public_subnet2" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "192.168.64.0/18"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet 2"
  }
}

# Define the private subnets.
resource "aws_subnet" "private_subnet1" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "192.168.128.0/18"
  availability_zone       = "us-east-1a"
  tags = {
    Name = "Private Subnet 1"
  }
}

resource "aws_subnet" "private_subnet2" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "192.168.192.0/18"
  availability_zone       = "us-east-1b"
  tags = {
    Name = "Private Subnet 2"
  }
}

# Output variables.
output "eks_cluster_name" {
  value = aws_eks_cluster.my_eks.name
}

output "nodegroup_name" {
  value = aws_eks_node_group.my_nodegroup.node_group_name
}
