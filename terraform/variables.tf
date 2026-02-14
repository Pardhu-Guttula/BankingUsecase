variable "sql_admin_login" {
  description = "The login name for the SQL administrator."
  type        = string
}

variable "sql_admin_password" {
  description = "The password for the SQL administrator."
  type        = string
  sensitive   = true
}

variable "log_analytics_workspace_id" {
  description = "The ID of the Log Analytics workspace."
  type        = string
}
