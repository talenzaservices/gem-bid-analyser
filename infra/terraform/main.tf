terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_ecr_repository" "backend" {
  name = "${var.project_name}-backend"
  image_tag_mutability = "MUTABLE"
  force_delete = true
}

resource "aws_ecr_repository" "frontend" {
  name = "${var.project_name}-frontend"
  image_tag_mutability = "MUTABLE"
  force_delete = true
}

resource "aws_rds_cluster" "postgres_cluster" {
  engine = "aurora-postgresql"
  engine_version = "13.6"
  cluster_identifier = "${var.project_name}-db-cluster"
  master_username = var.db_username
  master_password = var.db_password
  skip_final_snapshot = true
}

resource "aws_ecs_cluster" "ecs" {
  name = "${var.project_name}-ecs-cluster"
}

# Note: For simplicity this Terraform creates ECR repos, an Aurora cluster and an ECS cluster.
# You will need to add task definitions, IAM role attachments and ALB resources per your security needs.
