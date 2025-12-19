variable "region" {
  type = string
  default = "ap-south-1"
}

variable "project_name" {
  type = string
  default = "gembid"
}

variable "db_username" {
  type = string
  default = "admin"
}

variable "db_password" {
  type = string
  description = "Set a strong DB password via tfvars or environment variable"
}
