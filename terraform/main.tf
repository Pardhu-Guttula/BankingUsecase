provider {
  azurerm = {
    source  = "hashicorp/azurerm"
    version = "~> 4.56.0"
  }}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "self_service_rg" {
  name     = "self-service-rg"
  location = "East US"
}

resource "azurerm_app_service_plan" "service_plan" {
  name                = "self-service-plan"
  location            = azurerm_resource_group.self_service_rg.location
  resource_group_name = azurerm_resource_group.self_service_rg.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "app_service" {
  name                = "self-service-app"
  location            = azurerm_resource_group.self_service_rg.location
  resource_group_name = azurerm_resource_group.self_service_rg.name
  app_service_plan_id = azurerm_app_service_plan.service_plan.id
}

resource "azurerm_storage_account" "storage_account" {
  name                     = "selfservicestorage"
  resource_group_name      = azurerm_resource_group.self_service_rg.name
  location                 = azurerm_resource_group.self_service_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "storage_container" {
  name                  = "selfservicecontainer"
  storage_account_name  = azurerm_storage_account.storage_account.name
  container_access_type = "private"
}

resource "azurerm_sql_server" "sql_server" {
  name                         = "selfservicesqlserver"
  resource_group_name          = azurerm_resource_group.self_service_rg.name
  location                     = azurerm_resource_group.self_service_rg.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "sql_database" {
  name                = "selfservicedb"
  resource_group_name = azurerm_resource_group.self_service_rg.name
  location            = azurerm_resource_group.self_service_rg.location
  server_name         = azurerm_sql_server.sql_server.name
  requested_service_objective_name = "S1"
}

resource "azurerm_logic_app" "logic_app" {
  name                = "selfservicelogicapp"
  resource_group_name = azurerm_resource_group.self_service_rg.name
  location            = azurerm_resource_group.self_service_rg.location
}

resource "azurerm_servicebus_namespace" "servicebus_namespace" {
  name                = "selfserviceservicebus"
  resource_group_name = azurerm_resource_group.self_service_rg.name
  location            = azurerm_resource_group.self_service_rg.location
  sku                 = "Standard"
}

resource "azurerm_function_app" "function_app" {
  name                = "selfservicefunctionapp"
  location            = azurerm_resource_group.self_service_rg.location
  resource_group_name = azurerm_resource_group.self_service_rg.name
  app_service_plan_id = azurerm_app_service_plan.service_plan.id
  storage_account_name = azurerm_storage_account.storage_account.name
  storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key
  version = "~3"
}

resource "azurerm_application_insights" "app_insights" {
  name                = "selfserviceappinsights"
  location            = azurerm_resource_group.self_service_rg.location
  resource_group_name = azurerm_resource_group.self_service_rg.name
  application_type    = "web"
}

resource "azurerm_monitor_diagnostic_setting" "diagnostic_setting" {
  name                        = "selfservicediagnosticsetting"
  target_resource_id          = azurerm_app_service.app_service.id
  log_analytics_workspace_id  = azurerm_application_insights.app_insights.id
  enabled_log {
    category = "AppServiceConsoleLogs"
    enabled  = true
  }
  metric {
    category = "AllMetrics"
    enabled  = true
  }
}