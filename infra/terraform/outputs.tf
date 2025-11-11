output "api_base_url" {
  value = aws_apigatewayv2_stage.prod.invoke_url
}

output "lambda_function_name" {
  value = aws_lambda_function.api.function_name
}
