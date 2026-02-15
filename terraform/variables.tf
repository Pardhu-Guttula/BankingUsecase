variable "sql_admin_username" {
  description = "Admin username for the SQL server."
  type        = string
}

variable "sql_admin_password" {
  description = "Admin password for the SQL server."
  type        = string
  sensitive   = true
}