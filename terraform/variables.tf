variable "subscription_id" {
  description = "Identifiant de la souscription Azure utilisee pour le deploiement."
  type        = string
}

variable "location" {
  description = "Region Azure ou les ressources seront creees."
  type        = string
  default     = "germanywestcentral"
}

variable "project_name" {
  description = "Nom court du projet, utilise dans le nommage des ressources."
  type        = string
  default     = "hackathondevops"
}

variable "environment" {
  description = "Nom de l'environnement cible."
  type        = string
  default     = "dev"
}

variable "kubernetes_version" {
  description = "Version Kubernetes souhaitee pour AKS."
  type        = string
  default     = "1.33.7"
}

variable "node_count" {
  description = "Nombre de noeuds AKS pour le node pool systeme."
  type        = number
  default     = 1
}

variable "vm_size" {
  description = "Type de VM utilise pour les noeuds AKS."
  type        = string
  default     = "Standard_DC2s_v3"
}
