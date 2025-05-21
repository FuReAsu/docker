#cryptomodule-policy.hcl
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}