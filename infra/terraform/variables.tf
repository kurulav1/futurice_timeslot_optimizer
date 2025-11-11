variable "project" {
  type        = string
  description = "Project name prefix"
  default     = "find-optimal-time-slot"
}

variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "eu-north-1"
}

variable "lambda_zip_path" {
  type        = string
  description = "Path to built Lambda zip"
  default     = "../../dist/function.zip"
}

variable "lambda_memory_mb" {
  type        = number
  default     = 512
}

variable "lambda_timeout_seconds" {
  type        = number
  default     = 10
}
