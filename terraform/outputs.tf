output "resource_group_name" {
  description = "Nom du Resource Group cree."
  value       = azurerm_resource_group.main.name
}

output "aks_cluster_name" {
  description = "Nom du cluster AKS cree."
  value       = azurerm_kubernetes_cluster.main.name
}

output "acr_login_server" {
  description = "Adresse du registre ACR a utiliser pour pousser les images."
  value       = azurerm_container_registry.main.login_server
}

output "application_insights_connection_string" {
  description = "Connection string a reutiliser pour exporter les signaux vers Azure Monitor."
  value       = azurerm_application_insights.main.connection_string
  sensitive   = true
}
