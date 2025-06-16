path "secret/data/platform/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}

path "secret/metadata/platform/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
