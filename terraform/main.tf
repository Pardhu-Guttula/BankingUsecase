terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.56.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_app_service_plan" "asp" {
  name                = "app-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "app" {
  name                = "app-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
  site_config {
    always_on = true
  }
}

resource "azurerm_key_vault" "example" {
  name                        = "examplevault"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  soft_delete_enabled         = true
  sku_name                    = "standard"
}

resource "azurerm_api_management" "example" {
  name                = "example-api"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku_name            = "Developer"
  publisher_name      = "pub1"
  publisher_email     = "pub1@contoso.com"
}

resource "azurerm_servicebus_namespace" "example" {
  name                = "example-sb"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"
}

resource "azurerm_sql_server" "example" {
  name                         = "mysqlserver"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = "adminlogin"
  administrator_login_password = "H@Sh1CoR3!"
}

resource "azurerm_sql_database" "example" {
  name                = "exampledb"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  server_name         = azurerm_sql_server.example.name
  edition             = "Basic"
}

resource "azurerm_cosmosdb_account" "example" {
  name                = "example-cosmosdb"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  consistency_policy {
    consistency_level = "Session"
  }
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_monitor" "example" {
  name                = "example-monitor"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_security_center_contact" "example" {
  email   = "email@contoso.com"
  phone   = "123456789"
  name    = "default"
}

resource "azurerm_log_analytics_workspace" "example" {
  name                = "example-law"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
}

resource "azurerm_application_insights" "example" {
  name                = "example-ai"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}

resource "azurerm_sentinel" "example" {
  monitoring_workspace_id = azurerm_log_analytics_workspace.example.id
}
