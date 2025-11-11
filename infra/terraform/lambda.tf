locals {
  function_name = "${var.project}-api"
}

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${local.function_name}"
  retention_in_days = 14
}

resource "aws_lambda_function" "api" {
  function_name = local.function_name
  role          = aws_iam_role.lambda_exec.arn
  runtime       = "python3.10"
  handler       = "app.main.handler"
  filename      = var.lambda_zip_path
  source_code_hash = filebase64sha256(var.lambda_zip_path)
  timeout       = var.lambda_timeout_seconds
  memory_size   = var.lambda_memory_mb
  environment {
    variables = {
      PYTHONPATH = "/var/task"
    }
  }
  depends_on = [aws_cloudwatch_log_group.lambda]
}
