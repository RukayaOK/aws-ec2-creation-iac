variable "aws_region" {
  description = "The AWS region"
  type        = string
}

variable "instance_ami" {
  description = "The AMI (Amazon Machine Image) that identifies the instance"
  type        = string
  default     = "ami-01419b804382064e4"
}

variable "instance_type" {
  description = "The instance type to be used"
  type        = string
  default     = "t2.micro"
}

variable "key_pair_name" {
  description = "The name of the SSH key to associate to the instance. Note that the key must exist already."
  type        = string
  default     = ""
}